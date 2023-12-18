Проект "BatchBar", созданный на Python с использованием фреймворка Qt,  
представляет собой решение для управления инвентарем электронных компонентов.  
Он автоматизирует процесс сканирования штрих-кодов на катушках с компонентами,  
что позволяет быстро и эффективно перемещать их в соответствующие локации в базе данных. 

Основная особенность этой программы - возможность обрабатывать перемещения партиями,  
что значительно ускоряет процесс и сокращает нагрузку на базу данных.  

Это позволяет достигать стопроцентной точности в отслеживании перемещений катушек,
обеспечивая эффективное управление запасами и повышая производительность рабочих процессов.

В целом, "BatchBar" представляет собой высокоэффективный инструмент для управления складом,  
который может значительно улучшить операционные процессы.

Эта программа была написана в рамках работы на линии повехностного монтажа  
с целью повышения качества и скорости работы

Перед началом работы необходимо заполнить файл конфигурации `conf.json`, он создается при первом запуске
Поля:
- MDB_PATH - путь к БД (\\\\someserver\DBfld\database.mdb
- SMB_USERNAME - Имя пользователя для входа в SMB (Олег)
- SMB_PASSWORD - Пароль SMB (password)
- USER - ФИО, будет записано в поле USER при присвоении (Иванов Иван Иванович)
- TURN_SOUND_OFF - true/false (Выключать звук при выходе - true)
