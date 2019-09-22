#!/usr/bin/env python3
import cx_Oracle
import os

#set nls_lang
os.environ['NLS_LANG']='AMERICAN_AMERICA.AL32UTF8'

#create session
conn = cx_Oracle.connect('system/orcl@10.0.0.16:1521/orcl')

#create cursor
curs = conn.cursor()

#search data by cursor
x = curs.execute("select 1 from dual")

for i in x:
    print(i)

curs.close()
conn.close()
