# test_for_rootcode
Данный проект визуализирует на графике траекторию движения маятника Фуко с помощью библиотеки matplotlib, загружая данные из БД PostgreSQL.

Для корректной работы необходима установка следующих библиотек:
* psycopg2
* numpy
* matplotlib
* pandas
* openpyxl

### Настройки
Для подключения к базе данных необходимо ввести данные своего локального сервера в файле *db_info.py*. При желании можно изменить настройки маятника в файле *data.xlsx*. После запуска файла должен появиться динамический график. 