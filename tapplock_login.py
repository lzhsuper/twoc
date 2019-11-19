import os
import sys
import time
import re
import threading


class tapplock(threading.Thread):
    def __init__(self, driver, android_version):
        self.driver = driver
        self.android_version = android_version
        # self.android = android

    # driver = appium_start()
    # driver.implicitly_wait()

    def taptest(self):
        # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        a1 = 848 / 1080
        b1 = 1976 / 2208
        # 获取当前手机屏幕大小X,Y
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        return self.driver.tap([(a1 * X, b1 * Y)])

    def read(self):
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/back').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
        time.sleep(0.5)

    def login(self, password, ifnew):
        while True:
            try:
                time.sleep(0.5)
                username = self.driver.find_element_by_id('com.intelligent.tapp.test:id/email')
                break
            except:
                while True:
                    try:
                        # self.taptest()
                        self.driver.find_element_by_id('com.intelligent.tapp.test:id/next').click()
                        break
                    except:
                        time.sleep(0.5)
                        pass
        username.send_keys('877840950@qq.com')
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/password').send_keys(password)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/login').click()
        if ifnew == True:
            try:
                self.driver.find_element_by_accessibility_id('Setting')
                print('修改后密码验证成功！')
            except:
                print('修改后密码验证失败！')
        else:
            # print(self.android_version)
            if self.android_version == 10:
                while True:
                    try:
                        self.driver.find_element_by_id(
                            'com.android.permissioncontroller:id/permission_allow_always_button').click()
                        break
                    except:
                        try:
                            self.driver.find_element_by_id(
                                'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
                            break
                        except:
                            pass
                        pass
            elif self.android_version == 9:
                while True:
                    try:
                        self.driver.find_element_by_id(
                            'com.android.packageinstaller:id/permission_allow_button').click()
                        break
                    except:
                        pass

        time.sleep(2)

        # driver.find_element_by_id('com.intelligent.tapp.test:id/add').click()
        # time.sleep(2)
        # read(driver)
        # 跳过教程
        # driver.find_element_by_id('com.intelligent.tapp.test:id/menuSkip').click()
        # time.sleep(0.2)
        # driver.find_element_by_id('com.intelligent.tapp.test:id/md_button_positive').click()
        # time.sleep(1)

    def addlock(self):
        # 未绑定tapplock情况，添加新锁

        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/add').click()
                break
            except:
                pass
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
        time.sleep(0.5)
        test_one = []
        try:
            self.driver.find_element_by_id('com.intelligent.tapp.test:id/retry')
            print('正在查找新锁...')

        except:
            pass

        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/retry')
            except:
                try:
                    name_action = self.driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.F'
                        'rameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.'
                        'recyclerview.widget.RecyclerView/android.widget.RadioButton')
                    name = name_action.text
                    test_one.append(name)
                    if len(test_one) > 0:
                        print('已搜索到设备%s' % name)
                    elif test_one == 0:
                        print('未搜索到可用设备')
                    break
                except:
                    print('设备搜索功能已关闭,已自动开启')
                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/menuAdd').click()
                    time.sleep(0.5)
                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/ok').click()
                    time.sleep(0.5)

        name_action.click()
        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/name')
                break
            except:
                pass
        text = input('请输入当前锁编号名称:')
        while True:
            try:
                name = self.driver.find_element_by_id('com.intelligent.tapp.test:id/name')
                name.clear()
                name.send_keys(text)
                break
            except:
                pass
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/next').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/next').click()
        time.sleep(1)
        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/menuSkip').click()
                break
            except:
                self.driver.tap([(42, 122)])
                pass
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_button_positive').click()
