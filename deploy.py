# coding=UTF-8
import os

def run(deploy):
    result = deploy.readline(100)
    a = str(result)[-15:]
    pid = a.split('/')[0].strip()
    os.popen('kill -9 ' + str(pid))
    os.popen('nohup java -jar helian-webapp-0.0.1-SNAPSHOT.jar &')

with os.popen('netstat -apn | grep 8183') as deploy:
    run(deploy)
