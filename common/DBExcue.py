#/usr/bin/env python
#-*- coding:utf-8 -*-

import pymysql
from common.ConfigeReader import ReadConfig
import json


class MyDB:
    global config,readConfig
    readConfig = ReadConfig()
    # host = readConfig.getDBData("host")
    # port = readConfig.getDBData("port")
    # userName = readConfig.getDBData("username")
    # passWord = readConfig.getDBData("password")
    # database = readConfig.getDBData("database")

    def __init__(self,db_name):
        self.config = json.loads(readConfig.getDBData(section="DATABASE",option=db_name))
        self.db = None
        self.cursor = None
    def connectDB(self):
        try:
            #链接DB
            self.db = pymysql.connect(**self.config)
            #创建游标
            self.cursor = self.db.cursor()
            print("数据库链接成功")
        except ConnectionError as e:
            print(e)
    def exceuteSQL(self,sql):
        self.connectDB()
        #执行sql
        self.cursor.execute(sql)
        #执行完成之后进行提交
        self.db.commit()
        return self.cursor
    def getAll(self):
        value = self.cursor.fetchall()
        return value
    def getOne(self):
        value = self.cursor.fetchone()
        return value
    def closeDB(self):
        try:
            self.db.close()
        except Exception as e:
            print(e)


def SETHTFen():
    rd = ReadConfig()
    #获取手机号码
    mobile = rd.getResData("mobile")
    #获取 根据手机号码查询userId的sql
    GetUserIdByMobile = rd.getDBData(section="SQL",option="GetUserIdByMobile").format((mobile))
    db_nono = MyDB("dbNonoCofig")
    db_nono.connectDB()
    db_nono.exceuteSQL(GetUserIdByMobile)
    UserId = db_nono.getOne()[0]
    print(UserId)
    db_nono.closeDB()
    db_maiya = MyDB("dbMaiYaCofig")
    SetHTFenSql = rd.getDBData(section="SQL",option="SetHTFen").format(UserId)
    db_maiya.exceuteSQL(SetHTFenSql)
    db_maiya.closeDB()

if __name__ == "__main__":
    # db = MyDB()
    # db.connectDB()
    # sql = "SELECT * FROM db_nono.borrows_repayment WHERE bo_id = '1406534664' LIMIT 1"
    # db.exceuteSQL(sql)
    # print(db.getOne())
    # db.closeDB()
    SETHTFen()
