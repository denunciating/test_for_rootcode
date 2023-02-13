import psycopg2
import db_info
import pandas as pd
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


try:
    connection = psycopg2.connect(
        host=db_info.host,
        user=db_info.user,
        password=db_info.password
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    create_db_query = 'CREATE DATABASE foucault'
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
except:
    print('DB creation is failed. ')


table = psycopg2.connect(
    host=db_info.host,
    user=db_info.user,
    password=db_info.password,
    database='foucault'
)
drop_table_query = 'DROP TABLE IF EXISTS foucault_consts'
create_table_query = 'CREATE TABLE IF NOT EXISTS foucault_consts(' \
                     'g NUMERIC(7,3) NOT NULL,' \
                     'L NUMERIC(7,3) NOT NULL,' \
                     'init_x NUMERIC(5,3) NOT NULL,' \
                     'init_y NUMERIC(5,3),' \
                     'init_xdot NUMERIC(5,3),' \
                     'init_ydot NUMERIC(5,3),' \
                     'omega NUMERIC(17,12) NOT NULL,' \
                     'lambda NUMERIC(17,12) NOT NULL);'

insert_query = 'INSERT INTO foucault_consts(g, L, init_x, init_y, init_xdot, ' \
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
