import pdfplumber
import pandas as pd

path = '/home/microsweet/Documents/pdf/登记表1.pdf'

if __name__ == '__main__':
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        #print(text)
        tables = page.extract_tables()
        print(page.extract_tables())
        print(len(tables))
        #table是一个list 每行是一条数据
        for t in tables:
            print('t.size:'+str(len(t)))
            for row in t:
                #打印每行的第二列
                print(row[1])
            # 得到的table是嵌套list类型，转化成DataFrame更加方便查看和分析
            #df = pd.DataFrame(t[1:], columns=t[0])
            #print(df) 
