#!/usr/bin/env python3
import cx_Oracle
import os

os.environ['NSL_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# os.environ['NSL_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'

oracle_tns = 'system/orcl@192.168.128.251:1521/orcl'

conn = cx_Oracle.connect(oracle_tns)

curs = conn.cursor()

sql1 = "SELECT CADASTRALNO FROM GRID_SYSDB.UPDATE1017"
curs.execute(sql1)
djhs = curs.fetchall()

for djh in djhs:
    realareasql = "SELECT n.REALAREA FROM GRID_SYSDB.BBS_DRAWRISK n WHERE n.CADASTRALNO='" + djh[
        0] + "'"
    curs.execute(realareasql)
    realarea = curs.fetchall()
    if len(realarea) > 1:
        print(djh)

curs.close()
conn.close()
print('end')
