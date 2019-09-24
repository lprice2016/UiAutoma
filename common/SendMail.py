#/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import glob
import zipfile
from report import checkReportFile
from common.utils.Driver import Driver

from common.ConfigeReader import ReadConfig
from report import zip_report,getZipFilePath

import threading



class Email:
    def __init__(self):
        global host,user,password,port,sender,title,content

        host = ReadConfig().getMCData("mailhost")
        user = ReadConfig().getMCData("mailuser")
        port = int(ReadConfig().getMCData("port"))
        sender = ReadConfig().getMCData("sender")
        title = ReadConfig().getMCData("subject")
        password = ReadConfig().getMCData("mailpass")
        content = ReadConfig().getMCData("content")
        self.receiverValue = ReadConfig().getMCData("receiver")
        self.inOff = ReadConfig().getMCData("onoff")
        self.receiverList = []
        #获取收件人列表
        for receiver in str(self.receiverValue).split("/"):
            self.receiverList.append(receiver)
        #定义邮件发送时间
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.subject = title + ' ' +date
            self.msg =MIMEMultipart("mixed")
    def configHeader(self):
        self.msg["subject"] = self.subject
        self.msg["from"] = sender
        self.msg['to'] = ";".join(self.receiverList)
    def configContent(self):
        contenPlan = MIMEText(content,"plain","utf-8")
        self.msg.attach(contenPlan)

    def configZipFile(self):
        #如果邮件附件不为空，则发送附件信息
        reportPath = getZipFilePath(Driver.d.info['productName'])
        #reportPath = checkReportFile("R7Plus")
        #reportPath = getZipFilePath("R7Plus")
        if reportPath is not None:
            # zipPath = os.path.join(reportPath,)
            reportFile = MIMEApplication(open(reportPath,'rb').read())
            reportFile['Content-Type'] = 'applocation/octet-stream'
            reportFile['Content-Disposition'] = 'attachment;filename = "R7Plus.zip"'
            self.msg.attach(reportFile)
    def configHtml(self):
        reportHtml = getZipFilePath(Driver.d.info['productName'])
        #reportHtml = getZipFilePath("R7Plus")
        attr1 = MIMEText(open(reportHtml, 'rb').read(), 'base64', 'utf-8')
        attr1["Content-Type"] = 'application/octet-stream'
        fileName = "R7Plus" + ".html"
        attr1["Content-Disposition"] = 'attachment; filename={}'.format(fileName)
        self.msg.attach(attr1)
    def sendEmail(self):
        self.configHeader()
        self.configContent()
        self.configHtml()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiverList, self.msg.as_string())
            smtp.quit()
        except Exception as ex:
            print(ex)

class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass
    @staticmethod
    def getEmail():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email

if __name__ == "__main__":
    email = Email()
    email.sendEmail()
    # zip_report("R7Plus")
    # print(getZipFilePath("R7Plus"))
