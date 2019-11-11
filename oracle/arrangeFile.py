#!/usr/bin/env python3
import cx_Oracle
import os
import os.path
import openpyxl
from shutil import copyfile

#层级：xx县企业土地核查情况汇总——xx单位——土地税源编号——文件类型

#FileNotFoundError错误的数据
errorRows = []

#查询需要整理的任务
def query_data():
    os.environ['NSL_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    #os.environ['NSL_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'
    #print(os.path)
    oracle_tns = 'system/orcl@192.168.128.5:1521/orcl'
    conn = cx_Oracle.connect(oracle_tns)
    curs = conn.cursor()

    sql = "SELECT t.TASK_ID, t.OPERATION_OBJ, p.payername, m.xzqmc " \
          "FROM GRID_BUSINESs.BS_TASK_P_TASKS t, " \
          "GRID_SYSDB.BSS_TAXPAYERS_BAKE p, " \
          "grid_sysdb.county m " \
          "WHERE t.OPERATION_OBJ=p.djxh " \
          "AND t.TASK_ID IN (SELECT * FROM GRID_BUSINESS.ARRANGE_TASK) " \
          "and SUBSTR(t.FJBM, 2, 6)=m.XZBM"
    curs.execute(sql)
    rows = curs.fetchall()[:]

    #遍历任务rows
    for row in rows:
        #通过每一条任务查询任务的feedback
        find_feedback(curs, row, conn)

    curs.close()
    conn.close()

    #错误信息写入excel表格
    write_excel_xlsx('/home/microsweet/arrangeFile/errorExcel.xls', 'sheet1', errorRows)
    print('end')

#通过taskiId查询feedback
def find_feedback(curs, taskRow, conn):
    sql = "SELECT t.FEEDBACK_ID, t.TDSYBH FROM GRID_BUSINESS.BS_TASK_P_FEEDBACK t " \
          "WHERE t.TASK_ID='" + str(taskRow[0]) + "'"
    curs.execute(sql)
    rows = curs.fetchall()[:]
    #遍历feedback rows
    for row in rows:
        #查询feedback关联的file
        find_files(curs, taskRow, row, conn)

#通过feedbackId查询files
def find_files(curs, taskRow, feedbackRow, conn):
    sql = "SELECT t.FILE_ID, t.FILE_PATH, t.STORE_NAME, t.FILE_TYPE " \
          "FROM GRID_BUSINESS.BS_FILES t WHERE t.FK='" + str(feedbackRow[0]) + "' " \
          "AND t.RELATED_TABLE='GRID_BUSINESS.BS_TASK_P_FEEDBACK'"
    curs.execute(sql)
    rows = curs.fetchall()[:]
    #遍历file rows
    for row in rows:
        #整理文件
        arrangeFile(taskRow, feedbackRow, row, conn, curs)

#整理文件
def arrangeFile(taskRow, feedbackRow, fileRow, conn, curs):
    fileTypeName = return_file_type_name(fileRow[3])
    targetPrefix = '/home/microsweet/arrangeFile/write/' 
    targetFilePath = ''
    targetFilePath = taskRow[3] + '企业土地核查情况汇总/' \
                   + taskRow[2] + '+' + taskRow[1] + '/' \
                   + str(feedbackRow[1]) + '/' \
                   + fileTypeName
    sourceFilePath = fileRow[1].replace('D:/landtax/uploadFile/basicInfo/','/home/microsweet/arrangeFile/read/')
    #查看是否有目标目录
    dirFlag = os.path.isdir(targetFilePath)
    #查看是否有源文件
    fileFlag = os.path.isfile(sourceFilePath)
    try:
        if dirFlag==False and fileFlag==True:
            #没有目标目录，有源文件时执行

            #创建目标目录
            os.makedirs(targetPrefix + targetFilePath)
            #复制源文件到目标目录
            copyfile(sourceFilePath, targetPrefix + targetFilePath+'/'+fileRow[2])
            #更新file表
            #update_bs_file(curs, fileRow, targetFilePath, conn)
        elif dirFlag==True and fileFlag==True:
            #有目标目录，有源文件时执行

            copyfile(sourceFilePath, targetPrefix + targetFilePath+'/'+fileRow[2])
            #update_bs_file(curs, fileRow, targetFilePath, conn)
    except FileNotFoundError:
        errorRow = []
        errorRow.append(taskRow[1])
        errorRow.append(taskRow[2])
        errorRow.append(taskRow[3])
        errorRow.append(feedbackRow[0])
        errorRow.append(feedbackRow[1])
        errorRow.append(fileRow[0])
        errorRow.append(fileRow[1])
        errorRow.append(fileRow[2])
        errorRow.append(fileRow[3])
        errorRows.append(errorRow)
    except FileExistsError:
        pass


#返回文件类型中文名称
def return_file_type_name(fileType):
    if fileType=='tdzszl':
        return '01-土地证书资料'
    elif fileType=='htwjzl':
        return '02-合同文件资料'
    elif fileType=='zbsjzl':
        return '03-坐标数据资料'
    elif fileType=='dkwzjt':
        return '04-地块位置范围截图资料'
    else:
        print(fileType)
        return fileType

#FileNotFoundError错误的数据
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

#更新file表路径
def update_bs_file(curs, fileRow, targetFilePath, conn):
    target = 'D:/landtax/uploadFile/basicInfo/' + targetFilePath + fileRow[2]
    sql = "UPDATE GRID_BUSINESS.BS_FILES_ARRANGE_1104 t SET t.FILE_PATH='" \
        + target + "' WHERE t.FILE_ID=" + str(fileRow[0])
    curs.execute(sql)
    conn.commit


query_data()
