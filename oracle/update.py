#!/usr/bin/env python3
import cx_Oracle
import os

os.environ['NSL_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#os.environ['NSL_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'
print(os.path)

oracle_tns = 'system/orcl@192.168.128.5:1521/orcl'

conn = cx_Oracle.connect(oracle_tns)

curs = conn.cursor()

with open('./update.txt') as file_object:
    sql = file_object.read()
curs.execute(sql)
r = curs.fetchall()

for i in r:
    update_sql = "UPDATE GRID_SYSDB.SP_TASK_DRAW t SET t.bm='"+i[0]+"' WHERE t.SMID="+str(i[2])
    print(update_sql)
    curs.execute(update_sql)
    conn.commit()

curs.close()
conn.close()
print('end')
