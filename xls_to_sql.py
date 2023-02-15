import psycopg2
import db_info
import numpy as np
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
                     'g FLOAT NOT NULL,' \
                     'L FLOAT NOT NULL,' \
                     'init_x FLOAT NOT NULL,' \
                     'init_y FLOAT,' \
                     'init_xdot FLOAT,' \
                     'init_ydot FLOAT,' \
                     'omega FLOAT NOT NULL,' \
                     'lambda FLOAT NOT NULL);'

insert_query = 'INSERT INTO foucault_consts(g, L, init_x, init_y, init_xdot, ' \
               'init_ydot, omega, lambda) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

file = 'data.xlsx'
xl = pd.read_excel(file)
args = tuple([np.float64(xl[header][0]) for header in xl])

with table.cursor() as cursor:
    cursor.execute(drop_table_query)
    cursor.execute(create_table_query)
    cursor.execute(insert_query, args)
    table.commit()
