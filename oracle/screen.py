# !/usr/bin/env python3
import sqlite3
import os
import os.path
from shutil import copyfile

# 层级：xx县企业土地核查情况汇总——xx单位——土地税源编号——文件类型

# FileNotFoundError错误的数据
errorRows = []


# 查询需要整理的任务
def query_data():
    mydb = sqlite3.connect("FilePath.db")
    cursor = mydb.cursor()

    # 读取feedbackid
    sql = "select * from feedback"
    cursor.execute(sql)
    rows = cursor.fetchall()[:]

    # 遍历任务rows
    for row in rows:
        # 通过每一条任务查询任务的feedback
        find_files(cursor, row)

    print('end')


# 通过feedbackId查询files
def find_files(cursor, feedbackRow):

    sql = "SELECT t.FILE_ID, t.FILE_PATH, t.STORE_NAME, t.FILE_TYPE " \
          "FROM BS_FILES t WHERE t.FK='" + str(feedbackRow[0]) + "' " \
          "AND t.RELATED_TABLE='GRID_BUSINESS.BS_TASK_P_FEEDBACK'"
    cursor.execute(sql)
    rows = curs.fetchall()[:]
    # 遍历file rows
    for row in rows:
        # 整理文件
        arrangeFile(feedbackRow, row)


# 整理文件
def arrangeFile(taskRow, feedbackRow, fileRow):
    fileTypeName = return_file_type_name(fileRow[3])
    targetPrefix = 'J:/landtax/1128/'
    targetFilePath = ''
    targetFilePath = str(feedbackRow[2]) + '/' \
                   + fileTypeName
    sourceFilePath = fileRow[1].replace('D:', '/J:')
    # 查看是否有目标目录
    dirFlag = os.path.isdir(targetFilePath)
    # 查看是否有源文件
    fileFlag = os.path.isfile(sourceFilePath)
    try:
        if dirFlag == False and fileFlag == True:
            # 没有目标目录，有源文件时执行

            # 创建目标目录
            os.makedirs(targetPrefix + targetFilePath)
            # 复制源文件到目标目录
            copyfile(sourceFilePath,
                     targetPrefix + targetFilePath + '/' + fileRow[2])
            # 更新file表
            # update_bs_file(curs, fileRow, targetFilePath, conn)
        elif dirFlag == True and fileFlag == True:
            # 有目标目录，有源文件时执行

            copyfile(sourceFilePath,
                     targetPrefix + targetFilePath + '/' + fileRow[2])
            # update_bs_file(curs, fileRow, targetFilePath, conn)
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


# 返回文件类型中文名称
def return_file_type_name(fileType):
    if fileType == 'tdzszl':
        return '01-土地证书资料'
    elif fileType == 'htwjzl':
        return '02-合同文件资料'
    elif fileType == 'zbsjzl':
        return '03-坐标数据资料'
    elif fileType == 'dkwzjt':
        return '04-地块位置范围截图资料'
    else:
        print(fileType)
        return fileType


# FileNotFoundError错误的数据
def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    workbook.save(path)
    print("xlsx格式表格写入数据成功！")


query_data()
