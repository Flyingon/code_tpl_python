# -*- coding:utf-8 -*-
'''
delete outdate files
'''
from datetime import datetime, timedelta
import os
import time
import shutil
import datetime


def delDir(dir, datatime01):
    # 获取文件夹下所有文件和文件夹
    files = os.listdir(dir)
    for file in files:
        # filepath = os.path.join(dir , file)#路径拼接
        filePath = dir + "/" + file
        # 判断是否是文件
        if os.path.isfile(filePath):
            # 最后一次修改的时间
            last1 = os.stat(filePath).st_mtime  # 获取文件的时间戳
            filetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last1))  # 将时间戳格式化成时间格式的字符串
            # 删除七天前的文件
            if (datatime01 < filetime):  # datatime01是当前时间7天前的时间，filetime是文件修改的时间，如果文件时间小于(早于)datatime01时间，就删除
                os.remove(filePath)
                print(filePath + " was removed!")
        elif os.path.isdir(filePath):
            # 如果是文件夹，继续遍历删除
            delDir(filePath, datatime01)
            # 如果是空文件夹，删除空文件夹
            if not os.listdir(filePath):
                os.rmdir(filePath)
                print(filePath + " was removed!")


def cleandir(path, duration):
    time_now = time.time()
    for root, dirs, files in os.walk(path):
        for name in files:
            mtime = os.stat(os.path.join(root, name)).st_mtime
            if time_now - mtime > 3600 * 24 * duration:
                print(name)
                os.remove(os.path.join(root, name))
        for dirname in dirs:
            if (datetime.datetime.now() - datetime.datetime.strptime(dirname, '%Y%m%d')).days > duration:
                print(dirname)
                shutil.rmtree(os.path.join(root, dirname))


if __name__ == '__main__':
    # 获取路径
    path = "C:/Users/qmw/Desktop/shicedata"
    # 获取过期时间
    starttime = datetime.datetime.now()
    d1 = starttime + timedelta(days=-7)
    # d2 = starttime - timedelta(days=7) #获取7天前的时间
    date1 = str(d1)
    index = date1.find('.')  # 第一次出现的位置
    datatime01 = date1[:index]
    while True:
        delDir(path, datatime01)
        time.sleep(100)
