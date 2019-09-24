#/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import json
from common.ConfigeReader import ReadConfig
from common.CreateIdNum import CreateNameAndIdNum

class RequestInterface:
    def __init__(self,option):
        self.readConfig = ReadConfig()
        self.headers = self.readConfig.getInterFaceData("header")
        self.headers = json.loads(self.headers)
        self.url = self.geturl(option)
        self.timeOut=self.readConfig.getInterFaceData("timeout")
    def geturl(self,option):
        return self.readConfig.getInterFaceData(option)
    def setHeader(self,key,value):
        self.headers[key]=value

    #设置接口请求参数
    def setParams(self,option,key:list= None,value:list=None):
        #先获取配置的固定参数
        self.params = self.readConfig.getInterFaceData(option)
        self.params = json.loads(self.params)
        if key and value:
            #设置其中的动态变量
            for k,val in zip(key,value):
                self.params[k]=val
    def getParams(self):
        return self.params
    def get(self):
        try:
            response = requests.get(self.url,headers = self.headers,params=self.params,timeout=float(self.timeOut))
            return response
        except TimeoutError as e:
            print(e)
            return None
    def post(self):
        try:
            respons = requests.post(url = self.url,headers = self.headers,json=self.params,timeout=float(self.timeOut))
            return respons
        except TimeoutError as e:
            print(e)
            return None
#设置jwt
def setJwt(option,key:[],value:[]):
    rs = RequestInterface("loginUrl")
    rs.setParams(option,key,value)
    rs.readConfig.setInterFaceData("jwt",rs.post().json()['data']['jwt'])
    print(rs.post().json())
#获取jwt
def getJwt():
    jwt = ReadConfig().getInterFaceData('jwt')
    return jwt
#创建订单
def postCreatOrd():
    rs=RequestInterface("creatOrdUrl")
    rs.setParams("creatOrdParams")
    jwt = getJwt()
    rs.setHeader("jwt",jwt)
    print(rs.post())
#进行实名认证
def OCRAuth():
    rs=RequestInterface("OCRUrl")
    # 生成姓名和身份证，保存在ResultData
    CreateNameAndIdNum()
    # 获取姓名和身份证
    userName = ReadConfig().getResData("realname")
    IdNum = ReadConfig().getResData("idnum")
    rs.setParams("OCRParams",["realName","idNum"],[userName,IdNum])
    jwt = getJwt()
    rs.setHeader("jwt", jwt)
    print(rs.post())




if __name__ == "__main__":
    # rs = RequestInterface("loginUrl")
    # rs.setParams("login_params",["loginName","blackBox"],["15201735590","15201735590"])
    # rs.readConfig.setInterFaceData("jwt",rs.post().json()['data']['jwt'])
    # print(rs.post().json())
    OCRAuth()
