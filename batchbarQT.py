import json
import os
import re
import sys
from datetime import datetime
from time import time
import asyncio
import signal
import py_win_keyboard_layout
import pyautogui
import pyodbc
from PySide6.QtCore import Qt, QUrl, QEvent, QObject, Signal, Slot
from PySide6.QtAsyncio import QAsyncioEventLoopPolicy
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication

from smbclient import register_session

from main_widget import Ui_Form1

from io import StringIO

time_start = time()
VER = '2.0'
JSON_CONFIG_FILENAME = 'conf.json'
TXT_FILENAME = 'bars.txt'
FOLDERNAME = 'archive'
SQL_QUERY = """UPDATE CarrierTable
           SET Location=?, `Aux 3`=?, LastChanged=?
           WHERE CarrierId=?;"""

SQL_QUERY_SET_LOST = """UPDATE CarrierTable
           SET Location=?, `Aux 3`=?, LastChanged=?
           WHERE Location=?;"""
BAD_LOC = 'LOST'

SQL_QUERY_GET_LOC = """SELECT ComponentName, CarrierId
                       FROM CarrierTable
                       WHERE Location=?;"""

SQL_QUERY_CARRIER_COUNT = """SELECT Quantity
                             FROM CarrierTable
                             WHERE CarrierId=?;"""

CONF_DICT = {
    "MDB_PATH": r"",
    "SMB_USERNAME": "",
    "SMB_PASSWORD": "",
    "USER": "",
    "TURN_SOUND_OFF": True
}
GOOD_regex = re.compile(r'^R\d{6}$|^\$LC.+$')
ALERT_FILENAME = "alert.wav"


def vol_up():
    pyautogui.press('volumeup', presses=50)


def vol_down():
    pyautogui.press('volumedown', presses=50)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class barcode_file():
    def __init__(self, TXT_FILENAME):
        self.filename = TXT_FILENAME
        self.foldername = FOLDERNAME
        self.barcode = None
        if not os.path.exists(self.foldername):
            os.makedirs(self.foldername)
        self.update()
        try:
            self.con, self.cur = self.connect_DB()
        except Exception as err:
            print(err)

    def write(self, listbar):
        with open(self.filename, 'w') as f:
            for i in listbar:
                f.write(f'{i}\n')

    def update(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'a+') as f:
                pass
        with open(self.filename, 'r') as f:
            self.lines = f.readlines()
            for line in range(len(self.lines)):
                self.lines[line] = self.lines[line].strip()
            self.len_good = len(self.lines) > 0
            self.len = str(len(self.lines))
        if self.len_good:
            self.state = 'Готов к работе'
        else:
            self.state = 'Файл пуст'

    def clear(self):
        if main_window.msg_ask_yesno(text='Переместить в архив?', title=' '):
            open(self.filename, 'w').close()
            main_window.update_file()
            main_window.ui.listWidget_scan_show.clear()
            main_window.ui.tabWidget.setCurrentIndex(0)
            main_window.ui.lineEdit_scan_input.setFocus()

    def preprocess(self, mode=None, location=None):
        if not os.path.exists(self.foldername):
            os.makedirs(self.foldername)
        date_time_executed = datetime.now()
        file_new = os.path.realpath(self.foldername)
        file_new += date_time_executed.strftime(f'/%d.%m.%Y(%HH%MM%SS).txt')
        last_smd = None
        smd_dict = {}
        if mode == 'BATCH':
            def_loc = location
        elif mode == 'SINGLE':
            def_loc = None
        else:
            raise Exception('wrong mode specified')
        for barcode in self.lines:
            if barcode.startswith('R'):
                last_smd = barcode.replace("R", "")
                smd_dict[last_smd] = def_loc
            elif barcode.startswith('$LC') and mode == 'SINGLE':
                smd_dict[last_smd] = barcode.replace("$LC", "")
        with open(file_new, 'w') as outfile:
            for i in smd_dict:
                outfile.write(f'{i};{smd_dict[i]}\n')
        return file_new

    def connect_DB(self):
        try:
            register_session("smtdev", username=config.smb_username, password=config.smb_password)
            driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
            conn = pyodbc.connect(f'Driver={driver};DBQ={config.mdb_path}')
            cur = conn.cursor()
            return conn, cur
        except Exception as e:
            main_window.error('Не удалось подключиться к БД SMT', e)
            return

    def browse_loc(self, loc):
        try:
            ret = self.cur.execute(SQL_QUERY_GET_LOC, loc).fetchall()
            txt = ''
            for cell in ret:
                txt += ' '.join(cell) + '\n'
            return (txt)
        except pyodbc.DatabaseError as e:
            main_window.error('Ошибка БД', e)

    async def get_smd_count(self):
        try:
            carrier = self.barcode.strip()
            if carrier.startswith('R'):
                carrier = carrier.replace('R', '')
                ret = self.cur.execute(SQL_QUERY_CARRIER_COUNT, carrier).fetchall()
                txt = str(ret[0][0])
            else:
                txt = '----'
            return (txt)
        except Exception as err:
            print(err)
            return 'Ошибка'
            pass
            # main_window.error('Ошибка БД', e)
    def assign_to_lost(self, from_loc):
        conn, cur = self.connect_DB()
        date_time_executed = datetime.now()
        try:
            conn.autocommit = False
            cur.execute(SQL_QUERY_SET_LOST, BAD_LOC, config.user, date_time_executed, from_loc)
        except pyodbc.DatabaseError as e:
            main_window.error('Ошибка присвоения к БД', e)
            cur.rollback()
        else:
            cur.commit()
    def process(self):
        begin = time()
        date_time_executed = datetime.now()
        conn, cur = self.connect_DB()
        file_new = self.preprocess(mode=main_window.mode, location=main_window.loc)

        try:
            bad_cnt = 0
            bad_carriers = []
            carriers = []
            conn.autocommit = False
            for line in open(file_new, mode='r'):
                splitted = line.strip().split(';', 1)
                if splitted[1] != 'None':
                    pass
                    cur.execute(SQL_QUERY, splitted[1], config.user, date_time_executed, splitted[0])
                    carriers.append(line)
                else:
                    bad_cnt += 1
                    bad_carriers.append(splitted[0])
        except Exception as e:
            main_window.error('Ошибка присвоения к БД', e)
            cur.rollback()
        else:
            cur.commit()
            main_window.ui.lineEdit_status.setText("Готово")
            main_window.ui.label_time_elapsed.setText(f'Времени потрачено: {time() - begin:.2f} секунды')
            main_window.ui.textEdit_file.setText(''.join(carriers).replace(';', ' -> '))
            self.clear()

            if bad_cnt > 0:
                main_window.ui.textEdit_file.setText('CARRIERS без локации:\n' + '\n'.join(bad_carriers))
        finally:
            conn.autocommit = True


class create_config():
    config = None

    def __init__(self, JSON_CONFIG_FILENAME, CONF_DICT):
        if not os.path.exists(JSON_CONFIG_FILENAME):
            with open(JSON_CONFIG_FILENAME, 'w', encoding='utf8') as outfile:
                json.dump(CONF_DICT, outfile, ensure_ascii=False, indent=4)
        with open(JSON_CONFIG_FILENAME, 'r', encoding='utf8') as openfile:
            self.config = json.load(openfile)
        self.config['USER'] = f'{self.config["USER"]} BB'
        self.mdb_path = self.config["MDB_PATH"]
        self.smb_username = self.config['SMB_USERNAME']
        self.smb_password = self.config['SMB_PASSWORD']
        self.user = self.config['USER']
        self.turn_sound_off = self.config['TURN_SOUND_OFF']

    def check_conf(self):
        if not all(self.config.values()):
            main_window.msgbox_error(title='ОШИБКА', text='Проверьте конфигурационный файл')


class window1(QWidget):
    locations = {
        -2: 'INTERVAL',
        -3: 'STANOK',
        -4: 'SOBRANO_V_STANOK',
        -5: 'LOST'
    }
    modes = {
        -2: 'BATCH',
        -3: 'SINGLE'
    }

    loc = None
    mode = None
    start_signal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form1()
        self.ui.setupUi(self)
        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile(resource_path(ALERT_FILENAME)))
        # self.effect.setLoopCount(-2)
        self.ui.pushButton_open_archive.clicked.connect(self.open_archive)
        self.ui.pushButton_save_list.clicked.connect(self.save_to_file)
        self.ui.pushButton_scan_delete.clicked.connect(self.delete_rows)
        self.ui.listWidget_scan_show.itemDoubleClicked.connect(self.edit_cell)
        self.ui.lineEdit_scan_input.setFocus()
        # self.ui.lineEdit_scan_input.clicked
        self.ui.lineEdit_scan_input.returnPressed.connect(self.barcodes_append)
        self.ui.pushButton_reload.clicked.connect(self.update_file)  # кнопка обновить
        self.ui.loc_group.buttonClicked.connect(self.loc_callback)  # вызов по радио локаций
        self.ui.mode_group.buttonClicked.connect(self.mode_callback)  # вызов по радио режимов
        self.ui.lineEdit_custom_loc.textChanged.connect(
            self.custom_loc_callback)  # вызов по изменению кастомной локации
        self.ui.pushButton_start.clicked.connect(file.process)
        self.ui.pushButton_clear_file.clicked.connect(file.clear)
        self.ui.lineEdit_custom_loc.returnPressed.connect(self.sel_all)
        self.ui.lineEdit_custom_loc.setHidden(True)  # скрыть текстбокс локации
        self.ui.pushButton_easter.clicked.connect(self.easter)
        self.ui.pushButton_show_loc.clicked.connect(self.show_loc)
        QApplication.instance().focusChanged.connect(self.on_focusChanged)
        self.setWindowTitle(f'BatchBar {config.user}')
        self.installEventFilter(self)
        self.setWindowIcon(QIcon(resource_path('icon.ico')))
        self.loc_callback()  # присвоить стартовую локацию
        self.mode_callback()
        self.update_ready_state()
        self.show()
        self.ui.pushButton_debug.clicked.connect(self.open_debug)
        self.ui.listWidget_scan_show.addItems(file.lines)
        self.ui.tabWidget.setStyleSheet(
            "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.danger_group.setHidden(True)
        self.ui.radioButton_loc_lost.setHidden(True)
        self.ui.checkBox_dangerous.clicked.connect(self.danger_switch)
        self.ui.pushButton_clear_location.clicked.connect(self.assign_lost)
        sys.stdout = self.buf_stdout = StringIO()
        sys.stderr = self.buf_stderr = StringIO()
        print('redirected')

    @Slot()
    def async_start(self):
        self.start_signal.emit()

    async def get_count(self):
        self.ui.textEdit_quantity.setText(await file.get_smd_count())
        # print('async func')
    def assign_lost(self):
        file.assign_to_lost(self.loc)
        self.show_loc()
        self.ui.lineEdit_custom_loc.setText('')
    def danger_switch(self):
        if self.ui.checkBox_dangerous.checkState() == Qt.Checked:
            self.ui.danger_group.setHidden(False)
            self.ui.radioButton_loc_lost.setHidden(False)
        else:
            self.ui.danger_group.setHidden(True)
            self.ui.radioButton_loc_lost.setHidden(True)

    def closeEvent(self, event):
        super().closeEvent(event)

    def open_debug(self):
        self.ui.tabWidget.setTabEnabled(2, True)
        self.ui.tabWidget.setCurrentIndex(2)

        self.ui.textEdit_debug_stdout.setText(self.buf_stdout.getvalue())
        self.ui.textEdit_debug_stderr.setText(self.buf_stderr.getvalue())

    def eventFilter(self, QObject, event):
        if event.type() == QEvent.Type.WindowActivate:
            self.setStyleSheet("* {background : #f0f0f0;}")
            vol_up()
            self.change_layout_en()
        elif event.type() == QEvent.Type.WindowDeactivate:
            self.setStyleSheet("* {background : #ffb7b7;}")
            if config.turn_sound_off:
                vol_down()
        elif event.type() == QEvent.Type.Close:
            if config.turn_sound_off:
                vol_down()

        return False

    def show_loc(self):
        txt = file.browse_loc(self.loc)
        self.ui.textEdit_file.setText(txt)

    def on_focusChanged(self, old, now):
        if self.ui.lineEdit_scan_input == now:
            self.ui.lineEdit_scan_input.setStyleSheet("QLineEdit {background : #00ff08;}")
        elif self.ui.lineEdit_scan_input == old:
            self.ui.lineEdit_scan_input.setStyleSheet("QLineEdit {background : #ff0000;}")

    def update_ready_state(self):
        self.ui.lineEdit_barcode_count.setText(file.len)
        self.ui.lineEdit_status.setText(file.state)
        self.ui.textEdit_file.setText("\n".join(file.lines))
        if self.loc:
            self.ui.pushButton_show_loc.setEnabled(True)
            self.ui.pushButton_clear_location.setEnabled(True)
        else:
            self.ui.pushButton_show_loc.setEnabled(False)
            self.ui.pushButton_clear_location.setEnabled(False)
        if file.len_good and self.loc:
            self.ui.pushButton_start.setEnabled(True)
        else:
            self.ui.pushButton_start.setEnabled(False)

    def update_file(self):
        file.update()
        self.update_ready_state()

    @staticmethod
    def easter():
        config.turn_sound_off = False
        os.startfile('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    @staticmethod
    def change_layout_en():
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)

    @staticmethod
    def open_archive():
        os.startfile(os.path.realpath(file.foldername))

    def mode_callback(self):
        r_id = self.ui.mode_group.checkedId()
        if r_id == -2:
            self.ui.groupBox_loc.setHidden(False)
        else:
            self.ui.groupBox_loc.setHidden(True)
        self.mode = self.modes[r_id]

    def save_to_file(self):
        items = [self.ui.listWidget_scan_show.item(x).text() for x in range(self.ui.listWidget_scan_show.count())]
        print(items)
        file.write(items)
        self.update_file()
        self.ui.tabWidget.setCurrentIndex(1)

    def delete_rows(self):
        list_items = self.ui.listWidget_scan_show.selectedItems()
        if not list_items:
            return
        for item in list_items:
            self.ui.listWidget_scan_show.takeItem(self.ui.listWidget_scan_show.row(item))

    def barcodes_append(self):
        barcode = self.ui.lineEdit_scan_input.text().strip()
        if GOOD_regex.match(barcode):
            self.ui.listWidget_scan_show.addItems([barcode])
            file.barcode = barcode
            self.async_start()
        else:
            print('bad')
            self.effect.play()

        self.ui.lineEdit_scan_input.setText('')

    def edit_cell(self):
        index = self.ui.listWidget_scan_show.currentIndex()
        if index.isValid():
            item = self.ui.listWidget_scan_show.itemFromIndex(index)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
            if not item.isSelected():
                item.setSelected(True)
            self.ui.listWidget_scan_show.edit(index)

    def sel_all(self):
        self.ui.lineEdit_custom_loc.selectAll()

    def custom_loc_callback(self):
        txt = self.ui.lineEdit_custom_loc.text()
        if txt:
            self.loc = txt.replace('$LC', '')
            self.ui.lineEdit_custom_loc.setText(self.loc)
        else:
            self.loc = None
        self.update_ready_state()

    def loc_callback(self):
        r_id = self.ui.loc_group.checkedId()
        if r_id in self.locations:
            self.ui.lineEdit_custom_loc.setHidden(True)
            self.loc = self.locations[r_id]
        else:
            self.ui.lineEdit_custom_loc.setHidden(False)
            self.ui.lineEdit_custom_loc.setFocus()
            self.custom_loc_callback()
        self.update_ready_state()

    @staticmethod
    def msg_ask_yesno(text='', title=''):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.Yes)
        button = msg.exec()
        return button == QMessageBox.StandardButton.Yes

    @staticmethod
    def msgbox_error(title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        _ = msg.exec()
        sys.exit()

    @staticmethod
    def msgbox(title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        _ = msg.exec()

    def error(self, text, e):
        self.msgbox('ОШИБКА', f'{text}\n{e}')


class AsyncHelper(QObject):

    def __init__(self, worker, entry):
        super().__init__()
        self.entry = entry
        self.worker = worker
        if hasattr(self.worker, "start_signal") and isinstance(self.worker.start_signal, Signal):
            self.worker.start_signal.connect(self.on_worker_started)

    @Slot()
    def on_worker_started(self):
        asyncio.ensure_future(self.entry())


'''
QMessageBox.Critical
QMessageBox.Warning
QMessageBox.Information
QMessageBox.Question'''

if __name__ == '__main__':
    print('starting...')
    app = QApplication(sys.argv)
    config = create_config(JSON_CONFIG_FILENAME, CONF_DICT)
    file = barcode_file(TXT_FILENAME)
    main_window = window1()

    async_helper = AsyncHelper(main_window, main_window.get_count)
    config.check_conf()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # ret = app.exec()
    # sys.exit(ret)
    asyncio.set_event_loop_policy(QAsyncioEventLoopPolicy())
    asyncio.get_event_loop().run_forever()
