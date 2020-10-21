import os
import xlrd
import xlwt
import shutil


def write(arg):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('原华美', cell_overwrite_ok=True)
    for i in range(len(arg)):
        for j in range(len(arg[i])):
            sheet.write(i, j, arg[i][j])
            # print(arg[i][j])
    book.save('/home/microsweet/youtian/save.xls')

def read(path, index):
     # todo: read excel
    arr = []
    # path = ""
    # sheetName = "原华美"
    workbook = xlrd.open_workbook(path)
    # worksheet = workbook.sheet_by_name(sheetName)
    worksheet = workbook.sheet_by_index(index)
    rows = worksheet.nrows
    for row in range(rows):
        # if row<3:
            # continue
        # print(worksheet.row_values(row))
        arr.append(worksheet.row_values(row))
    return arr

def workData():
    dataSet = read("/home/microsweet/youtian/0--导出数据汇总.xlsx", 1)
    # print(dataSet)
    workdata = read("/home/microsweet/youtian/原华盛.xls", 1)
    # todo: work data
    for i in range(len(workdata)):
        row = workdata[i]
        a = split(row[25])
        if a is not None:
            row[25] = a[0]
            row.append(a[1])
        else:
            row.append("")
        
        searchData = [row[15], row[13]]
        b = finder(dataSet, searchData)
        # print(b)
        if b is not None:
            row.append(b[0])
            row.append(b[1])
            row.append(b[2])

        workdata[i] = row
        

    # write excel
    write(workdata)

def split(arg):
    r = arg.split("（")
    if len(r)==2:
        # print(r[1])
        # r[1] = r[1][:len(r[1])-1]
        tempa = r[1][:len(r[1])-1]
        tempb = tempa.split('月')
        # print(tempb)
        if len(tempb[0])==1:
            tempb[0] = "0" + tempb[0]
        tempc = tempb[1].split("日")
        if len(tempc[0])==1:
            tempc[0] = "0"+tempc[0]
        if tempa == "1月31、12月15日前":
            r[1] = tempa
        else:
            r[1] = "2020" + tempb[0] + tempc[0] + tempc[1]
        return  r
    else:
        return None

def finder(dataSet, searchData):
    for i in range(len(dataSet)):
        # print(dataSet)
        if searchData[0]==dataSet[i][3] :
            # print(searchData[0])
            # print(searchData[1])
            # print(dataSet[i][4])
            # print("---")
            if searchData[1]==dataSet[i][4]:
                return dataSet[i]
    return None

workData()
