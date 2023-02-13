import psycopg2
import db_info
import pandas as pd


try:
    connection = psycopg2.connect(
        host=db_info.host,
        user=db_info.user,
        password=db_info.password
    )
    create_db_query = 'CREATE DATABASE IF NOT EXISTS foucault'
    with connection.cursor() as cursor:
        cursor.execute(create_db_query) # Выдает ошибку psycopg2.errors.ActiveSqlTransaction: CREATE TABLESPACE 
except:                                 # cannot run inside a transaction block
    print('DB creation is failed. ')


table = psycopg2.connect(
    host=db_info.host,
    user=db_info.user,
    password=db_info.password,
    database=db_info.database
)
drop_table_query = 'DROP TABLE IF EXISTS foucault'
create_table_query = 'CREATE TABLE IF NOT EXISTS foucault(' \
                     'g NUMERIC(7,3) NOT NULL,' \
                     'L NUMERIC(7,3) NOT NULL,' \
                     'init_x NUMERIC(5,3) NOT NULL,' \
                     'init_y NUMERIC(5,3),' \
                     'init_xdot NUMERIC(5,3),' \
                     'init_ydot NUMERIC(5,3),' \
                     'omega NUMERIC(17,12) NOT NULL,' \
                     'lambda NUMERIC(17,12) NOT NULL);'

insert_query = 'INSERT INTO foucault(g, L, init_x, init_y, init_xdot, ' \
               'init_ydot, omega, lambda) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

file = 'data.xlsx'
xl = pd.read_excel(file)
args = (xl['g'][0], xl['L'][0], xl['init_x'][0], xl['init_y'][0],
             xl['init_xdot'][0], xl['init_ydot'][0],
             xl['omega'][0], xl['lambda'][0])

with table.cursor() as cursor:
    cursor.execute(drop_table_query)
    cursor.execute(create_table_query)
    cursor.execute(insert_query, args)
    table.commit()

