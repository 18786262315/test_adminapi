import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from common.Log import Logger
import readConfig
from common.configHttp import ConfigHttp
from datetime import datetime
from xlrd import xldate_as_tuple
localConfigHttp = ConfigHttp()

class Readkey:
    # 从excel文件中读取测试用例
    def __init__(self):
        #测试数据存放位置；
        self.file = 'testFile'
    def get_xls(self,xls_name, sheet_name):
        cls = []
        # get xls file's path
        xlsPath = os.path.join(readConfig.proDir, self.file, xls_name)
        # open xls file
        file = open_workbook(xlsPath)
        # get sheet by name
        sheet = file.sheet_by_name(sheet_name)
        # get one sheet's rows
        nrows = sheet.nrows
        cols = sheet.ncols
        for i in range(nrows):
            #处理获取数据是小数的问题
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype #表格的数据类型
                # print (ctype)
                cell = sheet.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                row_content.append(cell)
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(row_content)
        return cls

    # 从xml文件中读取sql语句
    database = {}
    def set_xml(self):
        if len(self.database) == 0:
            self.sql_path = os.path.join(readConfig.proDir, "testFile", "SQL.xml")
            tree = ElementTree.parse(self.sql_path)
            for db in tree.findall("database"):
                self.db_name = db.get("name")
                # print(db_name)
                table = {}
                for tb in db.getchildren():
                    table_name = tb.get("name")
                    # print(table_name)
                    sql = {}
                    for data in tb.getchildren():
                        sql_id = data.get("id")
                        # print(sql_id)
                        sql[sql_id] = data.text
                    table[table_name] = sql
                self.database[self.db_name] = table

    def get_xml_dict(self,database_name, table_name):
        self.set_xml()
        database_dict = self.database.get(database_name).get(table_name)
        return database_dict

    def get_sql(self,database_name, table_name, sql_id):
        db = self.get_xml_dict(database_name, table_name)
        sql = db.get(sql_id)
        return sql
