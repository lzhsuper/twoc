import sys
import time
from appium import webdriver
import os
import subprocess
import re
import socket
import threading

sys.path.append('..')
from twoc.tapplock_login import tapplock
from twoc.connect_lock import open_tapplock
from twoc.connect_lock import lockset
from twoc.connect_lock import share
from twoc.connect_lock import setting


class Appium_star(tapplock, open_tapplock):
    "启动app"

    def appium_start(self, i, j, times, android_version):
        i = str(i)
        j = str(j)
        # time.sleep(times)
        config = {
            'platformName': 'Android',  # 平台
            'platformVersion': 9,  # 系统版本
            'deviceName': i,  # 测试设备ID
            'appPackage': 'com.intelligent.tapp.test',
            'appActivity': 'com.intelligent.tapp.ui.user.splash.SplashActivity',
            # 'app': 'C:\\Users\\Tapplock\\AppData\\Local\\Programs\\Python\\untitled\\venv\\Lib\\site-packages\\python-appium\\tests\\twoc\\two_c.apk',
            # apk路径
            'newCommandTimeout': 30,
            # 'automationName': 'Appium',
            'unicodeKeyboard': True,  # 编码,可解决中文输入问题
            'resetKeyboard': True,
            'automationName': 'uiautomator2',
            'udid': i
        }
        # if times > 0:
        #     del config['automationName']
        while True:
            try:
                driver = webdriver.Remote('http://localhost:' + str(j) + '/wd/hub', config)
                break
            except:
                pass
        # print(str(j))
        file = open(
            'C:/Users/Tapplock/AppData/Local/Programs/Python/untitled/venv/Lib/python-appium/tests/twoc/password.txt',
            'r+')
        password = file.read()
        tapplock(driver, android_version).login(password, ifnew=False)  # 登陆用户
        if open_tapplock(driver).connectlock() == False:  # 判断是否有锁/并连接
            tapplock(driver, android_version).addlock()  # 添加锁
            open_tapplock(driver).connectlock()  # 判断是否有锁/并连接
        open_tapplock(driver).openlock()  # 蓝牙开锁
        open_tapplock(driver).fingerprint()  # 指纹录入及开锁
        open_tapplock(driver).finger_delete()  # 指纹删除
        lockset(driver, android_version).lockset_picture()  # 头像设置
        lockset(driver, android_version).lockset_name()  # 锁名设置
        lockset(driver, android_version).morse_code()  # morse密码设置
        lockset(driver, android_version).delete_lock()  # 删除锁
        share(driver).add_share()  # 分享授权
        setting(driver, android_version).change_picture()  #更改头像
        setting(driver,android_version).change_name()  #更改username
        setting(driver,android_version).change_pwd(password,file)  #更改密码
        tapplock(driver,android_version).login(password,ifnew=True)  #登陆验证修改后密码


class devices_find(Appium_star, threading.Thread):
    "利用adb获取设备devices name"

    def __init__(self):
        pass

    def check_port(self, port):

        """检测端口是否被占用"""

        host = '127.0.0.1'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            s.shutdown(2)
            # print('port %s is uesd !' % port)
            return False

        except:
            # print('port %s is available!' % port)
            return True

    def devices_result(self):
        # Appium_star.__init__()
        cmd_devices = 'adb devices'
        cmd_appium = 'appium'
        name = os.popen(cmd_devices)
        name = name.read()
        self.result = re.findall(r'\n(.*)\t', name)
        self.android_sum = []
        for device in self.result:
            android_result = re.findall('(.*)\\n',
                                        os.popen('adb -s ' + device + ' shell getprop ro.build.version.release').read())
            android_result = ','.join(android_result)
            self.android_sum.append(android_result)
        self.result_len = len(self.result)
        self.duankou_num = []
        port_star = 4723
        for i in range(self.result_len):
            os.popen(cmd_appium)
            port_star += i * 2
            if self.check_port(port_star) == True:
                self.duankou_num.append(str(port_star))
            else:
                while True:
                    if self.check_port(port_star) == True:
                        self.duankou_num.append(str(port_star))
                        break
                    elif self.check_port(port_star) == False:
                        port_star += 2

        # duankou_name = ' '.join(duankou_num)
        print('当前共有 %s 台设备，请开启以下端口以供服务运行:%s' % (self.result_len, ','.join(self.duankou_num)))
        # while True:
        #      result = input('完成操作(Y/N)')
        #      if  result == 'Y' or result == 'y':
        #          break
        #      else:pass
        self.result_and_duankou = dict(zip(self.result, self.duankou_num))
        # print(self.result_and_duankou)
        # print(self.result)

        for i in range(len(self.result_and_duankou)):
            # print(i)
            # print(self.result[int(i)], self.result_and_duankou[self.result[i]])
            t = threading.Thread(target=Appium_star.appium_start, args=(
            self, self.result[int(i)], self.result_and_duankou[self.result[i]], int(i) * int(i),
            int(self.android_sum[i])))
            # Appium_star.appium_start(self,self.result[int(i)],self.result_and_duankou[self.result[i]])
            # t.setDaemon(True)
            # print(self.result[int(i)],self.result_and_duankou[self.result[i]],int(i)*int(i))
            t.start()
            # t.join()
        # return self.result_and_duankou,self.result


if __name__ == '__main__':
    devices_find = devices_find()
    devices_find.devices_result()
