import configparser
import sys
import subprocess
import os

if sys.platform in ('darwin', 'Darwin'):
    print(True)

webview = subprocess.Popen('adb shell dumpsys package com.google.android.webview | grep versionName',
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
ret = webview.communicate()[0]
version = bytes.decode(ret).strip().split('=')[1]
version = version.split('.')[0]

print(bytes.decode(ret))
print(version)

cf = configparser.ConfigParser()
cf.read("chromedriver.conf")
secs = cf.sections()
print(secs)
ops = cf.options(secs[0])
print(ops)

kvs = cf.items('52')
print(kvs)
for item in kvs:
    print(item)

str_val = cf.get(version, 'chromedriver')
print(str_val)

cur_dir = os.path.dirname(os.path.abspath(__file__))
if sys.platform in ('darwin', 'Darwin'):
    re_dir = '/mac'
else:
    re_dir = '/linux'
driver_path = cur_dir + re_dir + '/' + str_val + '/chromedriver'
print(driver_path)