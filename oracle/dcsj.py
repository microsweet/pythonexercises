#!/usr/bin/env python3
import cx_Oracle
import os
import openpyxl



def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
    workbook.save(path)
    print("xlsx格式表格写入数据成功！")
 
 
def query_data():
    os.environ['NSL_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    #os.environ['NSL_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'

    oracle_tns = 'system/orcl@192.168.128.3:1521/orcl'
    conn = cx_Oracle.connect(oracle_tns)
    curs = conn.cursor()

    #读取sql
    sql_path = '/home/microsweet/pythonexercises/oracle/dcsql.txt'
    with open(sql_path) as file_object:
        contents = file_object.read()

    #执行sql
    curs.execute(contents)
    #获取数据
    data = curs.fetchall()
    #获取列名
    cols = curs.description

    curs.close()
    conn.close()

    title = []
    for col in cols:
        title.append(col[0])

    exportData = data[:]
    exportData.insert(0, title)

    exportPath = '/home/microsweet/workspace/work/地税/export/'
    exportName = ''
    write_excel_xlsx(exportPath+exportName+'.xlsx', exportName, exportData)
    print('end')

query_data()
