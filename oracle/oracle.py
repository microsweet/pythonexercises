#!/usr/bin/env python3
import cx_Oracle
import os

os.environ['NSL_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#os.environ['NSL_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'
print(os.path)

oracle_tns = 'system/orcl@192.168.128.251:1521/orcl'

conn = cx_Oracle.connect(oracle_tns)

curs = conn.cursor()

r = curs.execute('select xzbm, xzqmc  from grid_sysdb.county')

#d = curs.fetchall()

rows = []
for i in r:
    print(i[0])
    row = {'xzbm': i[0], 'xzqmc': i[1]}
    rows.append(row)

for i in rows:
    print('xzbm：' + i['xzbm'] + '\t'  + 'xzqmc：' + i['xzqmc'])
#print(curs.rowcount)
#print(rows)

curs.close()
conn.close()
