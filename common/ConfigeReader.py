#/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import codecs

import importlib

importlib.reload(sys)

import configparser #Configeparser 模块在python中用来读取配置文件，配置文件的格式跟windows下的ini配置文件相似，可以包含或多个节点（section）
#每个节点可以有多个参数（健=值）。使用的配置文件的好处就是不用在程序中写死，可以使程序更灵活

#根目录common
proDir = os.path.split(os.path.realpath(__file__))[0]
#根目录
rootDir = os.path.split(proDir)[0]
#配置文件目录
conDir = os.path.join(rootDir,"Config")
# ResultData  /Users/user/PycharmProjects/maiyaapp-android-uiautotest/Config/ResultData
resDataFD = os.path.join(conDir, "ResultData")
#InterFaceConf配置的路径
interFaceFD = os.path.join(conDir,"InterFaceConf")
#DataBases 配置文件路径
DBFD = os.path.join(conDir,"DBConfig")
#MailConfig 配置文件路径
MCFD = os.path.join(conDir,"MailConfig")
class ReadConfig:
    def __init__(self):

        #读取resultData文件
        with open(resDataFD) as file:
            ResData = file.read()
        #读取InterFaceConf文件
        with open(interFaceFD,'r') as file:
            InterFaceData = file.read()
        #读取数据库文件配置
        with open(DBFD,'r') as file:
            DBData = file.read()
        #读取邮件配置文件配置
        with open(MCFD,"r") as file:
            MCData = file.read()
        for data,DataFD in zip([ResData,InterFaceData,DBData,MCData],[resDataFD,interFaceFD,DBFD,MCFD]):
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                with open(DataFD,'w') as file:
                    file.write(data)
        #创建读取resultData 的configparser对象
        self.RESCF = configparser.ConfigParser()
        self.RESCF.read(resDataFD,encoding='utf-8')
        #创建读取InterFaceData的configparser对象
        self.InterFaceCF = configparser.ConfigParser()
        self.InterFaceCF.read(interFaceFD,encoding='utf-8')
        #创建读取DBFD 的configparser对象
        self.DBCF = configparser.ConfigParser()
        self.DBCF.read(DBFD,encoding="utf-8")
        #创建读取MCFD的configpaser对象
        self.MCCF = configparser.ConfigParser()
        self.MCCF.read(MCFD,encoding="utf-8")
    def getResData(self,option,section="ResDate"):
        value = self.RESCF.get(section,option)
        return value
    def setResData(self,option,value,section='ResDate'):
        self.RESCF.set(section,option,value)
        self.RESCF.write(open(resDataFD,"w",encoding='utf-8'))
    def getInterFaceData(self,option,section="HTTP"):
        value = self.InterFaceCF.get(section,option)
        return value
    def setInterFaceData(self,option,value,section="HTTP"):
        self.InterFaceCF.set(section,option,value)
        self.InterFaceCF.write(open(interFaceFD,'w',encoding='utf-8'))
    def getDBData(self,option,section="DATABASE"):
        value = self.DBCF.get(section,option)
        return value
    def setDBData(self,option,value,section="DATABASE"):
        self.DBCF.set(section,option=option,value=value)
        self.DBCF.write(open(DBFD,"w",encoding="utf-8"))
    #####获取邮件配置#####
    def getMCData(self,option,section="EMAIL"):
        value = self.MCCF.get(section=section,option=option)
        return value
    def setMCData(self,option,value,section="EMAIL"):
        self.MCCF.set(section=section,option=option,value=value)
        self.MCCF.write(open(MCFD,'w',encoding="utf-8"))


if __name__ == "__main__":
    rd = ReadConfig()
    print(rd.getMCData("sender"))
    rd.setMCData(option="sender",value="goujingwei")




