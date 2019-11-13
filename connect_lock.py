import sys
import threading
import random
# sys.path.append('..')
# from common.app_star import devices_find
from twoc.tapplock_login import tapplock
import time


class driver_by:
    def __init__(self):
        pass

    def driver_id(self, driverid):
        while True:
            try:
                driverid = self.driver.find_element_by_id(driverid)
                break
            except:
                pass
        return driverid

    def driver_xpath(self, path):
        while True:
            try:
                driverpath = self.driver.find_element_by_xpath(path)
                break
            except:
                pass
        return driverpath


class open_tapplock(driver_by):
    def __init__(self, driver):
        self.driver = driver

    def navigation(self):

        '导航点击'

        while True:
            try:
                unlock = self.driver.find_element_by_id('com.intelligent.tapp.test:id/unlock')
                break
            except:
                pass
        unlock.click()
        time.sleep(1)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/fingerprint').click()
        time.sleep(1)
        unlock.click()
        time.sleep(1)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/fingerprint').click()
        time.sleep(1)

    def connectlock(self):

        "此功能用于存在已绑定tapplock情况下，连接及蓝牙开锁"

        try:
            self.driver.find_element_by_id('com.intelligent.tapp.test:id/background')
            # print('1')
        except:
            return False
        # 连接设备
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/background').click()
        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/setting')
                break
            except:
                pass

        connect_text = self.driver.find_element_by_id('com.intelligent.tapp.test:id/condition').text
        if connect_text == 'Disconnected':
            print('警告：设备处于断开连接状态 （ps：将主动进行连接尝试,请开启硬件连接！）')
            self.driver.find_element_by_id('com.intelligent.tapp.test:id/snackbar_action').click()
            print('设备连接中...')
            while True:
                try:
                    connect_text = self.driver.find_element_by_id('com.intelligent.tapp.test:id/condition').text
                    # print(connect_text)
                    if connect_text == 'Connect':
                        print('连接成功！即将进入蓝牙开锁...')
                        break
                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/snackbar_action').click()

                except:
                    pass

        elif connect_text == 'Connect':
            print('已连接设备！即将进入蓝牙开锁...')

    def openlock(self):

        "本函数用作蓝牙开锁功能"

        while True:
            time.sleep(4)
            while True:
                try:
                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/unlock').click()
                    break
                except:
                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/background').click()

            result = input('请输入开锁结果(Y/N):')
            if result == 'Y':
                print('开锁成功，继续指纹录入流程...')
                break
            elif result == 'N':
                print('\033[1;31;0m')  # 下一目标输出背景为黑色，颜色红色高亮显示
                print('*' * 39)
                print('* \033[7;31m 蓝牙开锁失败！即将检查连接状态... \033[1;31;0m *')  # 字体颜色红色反白处理
                print('*' * 39)
                print('\033[0m')
                # electricity = self.driver.find_element_by_id('com.intelligent.tapp.test:id/battery').text
                # print(electricity)
                ifconnnect = self.driver.find_element_by_id('com.intelligent.tapp.test:id/condition').text
                if ifconnnect == 'Connect':
                    while True:
                        result = input('连接状态正常，请手动尝试查找其它原因！是否继续尝试开锁？(Y/N)')
                        if result == 'Y':
                            break
                        elif result == 'N':
                            return
                        else:
                            pass
                elif ifconnnect == 'Disconnected':
                    print('连接已断开，请重新连接！')
                    while True:
                        try:
                            connect_text = self.driver.find_element_by_id('com.intelligent.tapp.test:id/condition').text
                            # print(connect_text)
                            if connect_text == 'Connect':
                                print('连接成功，正在重新开锁，请稍后...')
                                time.sleep(4)
                                break
                            else:
                                pass
                        except:
                            pass
            else:
                pass
        return

    def driver_id(self, driverid):
        while True:
            try:
                driverid = self.driver.find_element_by_id(driverid)
                break
            except:
                pass
        return driverid

    def fingerprint(self):

        "本函数作为指纹录入及开锁"
        print('* * * * * * * * * * * * *\n'
              '* I.左手      1.大拇指  *\n'
              '*             2.食指    *\n'
              '* II.右手     3.中指    *\n'
              '*             4.无名指  *\n'
              '*             5.小拇指  *\n'
              '* * * * * * * * * * * * *')
        self.used_finger = []
        time.sleep(1)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/fingerprint').click()
        time.sleep(1)
        self.driver_id('com.intelligent.tapp.test:id/thumb').click()
        YN = ''
        while True:
            if YN == 'N' or YN == 'n':
                print('已存在指纹：' + (','.join(list(set(self.used_finger)))))
                break
            try:
                time.sleep(2)
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_button_positive').click()
                print('请于设备开始录入指纹...')
                self.used_finger.append('I-1')
                while True:
                    success = False
                    try:
                        time.sleep(1)
                        self.driver.find_element_by_id('com.intelligent.tapp.test:id/videoView')
                        pass
                    except:
                        while True:
                            try:
                                self.driver.find_element_by_id(
                                    'com.intelligent.tapp.test:id/md_button_positive').click()
                                break
                            except:
                                success = True
                                print('录入指纹成功')
                                # result = input('录入指纹成功，请尝试指纹' +(','.join(list(set(self.used_finger))))+ '解锁，并输入解锁结果(Y/N):')
                                break
                        if success == True:
                            break
                        else:
                            pass
            except:
                self.used_finger.append('I-1')
                br = ''
                while True:
                    if br == 'b':
                        break
                    YN = input('已存在指纹' + (','.join(list(set(self.used_finger)))) + '，是否继续录入指纹（Y/N）:')
                    if YN == 'Y':
                        while True:
                            while True:
                                result_finger = input('\033[0;37m请选择\033[1;36m序号\033[0;37m（例：I-1）:')
                                if len(result_finger) == 4:
                                    if result_finger[2] == '-':
                                        if result_finger[3] in ('1', '2', '3', '4', '5'):
                                            break

                                elif len(result_finger) == 3:
                                    if result_finger[0] == 'I' and result_finger[1] == '-' and result_finger[
                                        2] in ('1', '2', '3', '4', '5'):
                                        break
                                else:
                                    pass

                            result_finger = str(result_finger)
                            self.used_finger.append(result_finger)
                            h, f = result_finger.split('-')
                            f = int(f)
                            # print(h,type(h))
                            # print(f, type(f))
                            if h == 'II':
                                self.driver.find_element_by_accessibility_id('Right').click()
                                if f == 1:
                                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/thumb').click()
                                    br = 'b'
                                    break

                                elif f == 2:
                                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/index').click()
                                    br = 'b'
                                    break

                                elif f == 3:
                                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/middle').click()
                                    br = 'b'
                                    break

                                elif f == 4:
                                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/ring').click()
                                    br = 'b'
                                    break

                                elif f == 5:
                                    self.driver.find_element_by_id('com.intelligent.tapp.test:id/little').click()
                                    br = 'b'
                                    break

                            elif f == 1:
                                br = 'b'
                                break

                            elif f == 2:
                                self.driver.find_element_by_id('com.intelligent.tapp.test:id/index').click()
                                br = 'b'
                                break

                            elif f == 3:
                                self.driver.find_element_by_id('com.intelligent.tapp.test:id/middle').click()
                                br = 'b'
                                break

                            elif f == 4:
                                self.driver.find_element_by_id('com.intelligent.tapp.test:id/ring').click()
                                br = 'b'
                                break

                            elif f == 5:
                                self.driver.find_element_by_id('com.intelligent.tapp.test:id/little').click()
                                br = 'b'
                                break
                            elif f <= 5:
                                self.used_finger.append(result_finger)
                    elif YN == 'N':
                        # result = input('已有指纹'+(','.join(list(set(self.used_finger))))+'，请尝试指纹解锁，并输入解锁结果(Y/N):')
                        break
                    else:
                        # YN = input('已存在指纹'+(','.join(list(set(self.used_finger))))+'，是否继续录入指纹（Y/N）:')
                        pass

        while True:
            result = input('录入指纹成功，请尝试指纹' + (','.join(list(set(self.used_finger)))) + '解锁，并输入解锁结果(Y/N):')
            if result == 'Y':
                print('指纹开锁成功！')
                print('即将进入指纹删除流程...')
                break
            elif result == 'N':
                print('\033[1;31;0m')  # 下一目标输出背景为黑色，颜色红色高亮显示
                print('*' * 20)
                print('* \033[7;31m 指纹开锁失败！ \033[1;31;0m *')  # 字体颜色红色反白处理
                print('*' * 20)
                print('\033[0m')
                print('即将进入指纹删除流程...')
                break
            else:
                print('请输入开锁结果(Y/N):')

    def finger_delete(self):

        '''进行指纹删除'''

        self.driver.find_element_by_accessibility_id('Delete').click()
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/thumb').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_button_positive').click()
        print('正在删除指纹：I-1 ...')
        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/progress')
            except:
                break
        while True:
            time.sleep(0.5)
            self.driver.find_element_by_id('com.intelligent.tapp.test:id/thumb').click()
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_button_positive').click()
                pass
            except:
                self.driver.find_element_by_accessibility_id('Navigate up').click()
                print('指纹删除成功！请使用 I-1 进行解锁！')
                break
        while True:
            fin_delete = input('指纹验证是否正常(Y/N)：')
            if fin_delete == 'Y':
                print('验证成功！将进入设置锁信息 ...')
                break
            elif fin_delete == 'N':
                print('\033[1;31;0m')  # 下一目标输出背景为黑色，颜色红色高亮显示
                print('*' * 20)
                print('* \033[7;31m 删除锁指纹失败！ \033[1;31;0m *')  # 字体颜色红色反白处理
                print('*' * 20)
                print('\033[0m')
                break
            else:
                pass


class lockset(threading.Thread):

    def __init__(self, driver, android_version):
        self.driver = driver
        self.android_version = android_version

    def driver_xpath(self, path):
        while True:
            try:
                driverpath = self.driver.find_element_by_xpath(path)
                break
            except:
                pass
        return driverpath

    def driver_id(self, driverid):
        while True:
            try:
                driverid = self.driver.find_element_by_id(driverid)
                break
            except:
                pass
        return driverid

    def lockset_picture(self):

        "本函数为头像更换"

        # self.driver.find_element_by_id('com.intelligent.tapp.test:id/background').click()
        # time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/setting').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/avatar').click()
        time.sleep(1)
        if self.android_version == 10:
            self.driver_id('com.android.permissioncontroller:id/permission_allow_button').click()
        elif self.android_version == 9:
            self.driver_id('com.android.packageinstaller:id/permission_allow_button').click()
        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/btn_ok').click()
                break
            except:
                self.driver.tap([(random.sample(range(240, 850), 1)[0], random.sample(range(300, 900), 1)[0])])

    def lockset_name(self):

        '''本函数用于更改用户名称'''

        self.value = input('请输入锁名:')
        self.value = str(self.value)
        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/lockNameLabel').click()
                break
            except:
                pass
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_input_message').clear()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_input_message').send_keys(self.value)
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_button_positive').click()
        time.sleep(1)
        time.sleep(0.5)
        if self.driver.find_element_by_id('com.intelligent.tapp.test:id/lockName').text == self.value:
            print('更改锁名成功！')
        else:
            print('用户名信息与输入不一致！')

    def morse_code(self):

        '''本函数用来更改摩斯密码'''

        password = [''] * 12
        location = random.sample(range(12), 6)
        for i in location:
            password[i] = 'short'
        for j in range(12):
            if password[j] == '':
                password[j] = 'long'
        print('本次设置morse password内容为:\033[1;36m %s' % ','.join(password))

        self.driver.find_element_by_id('com.intelligent.tapp.test:id/morse').click()
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/menuNext').click()
        for click in password:
            time.sleep(0.5)
            if click == 'short':
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/shortCode').click()
            elif click == 'long':
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/longCode').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/save').click()
        print(self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_text_message').text)
        time.sleep(0.5)
        self.driver.find_element_by_id('com.intelligent.tapp.test:id/md_button_positive').click()
        time.sleep(0.5)
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        time.sleep(0.5)
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        time.sleep(0.5)
        self.driver.find_element_by_accessibility_id('Navigate up').click()

        while True:
            fin_delete = input('morse密码验证是否正常(Y/N)：')
            if fin_delete == 'Y':
                print('验证成功！将进入...页面 ...')
                break
            elif fin_delete == 'N':
                print('\033[1;31;0m')
                print('*' * 20)
                print('* \033[7;31m 莫斯码开启失败！ \033[1;31;0m *')
                print('*' * 20)
                print('\033[0m')
                break
            else:
                pass

    def delete_lock(self):
        self.driver_id('com.intelligent.tapp.test:id/lockHomeFragment').click()
        self.driver_id('com.intelligent.tapp.test:id/background').click()
        self.driver_id('com.intelligent.tapp.test:id/setting').click()
        self.driver_id('com.intelligent.tapp.test:id/delete').click()
        self.driver_id('com.intelligent.tapp.test:id/md_button_positive').click()


class share(lockset):

    def __init__(self, driver):
        self.driver = driver

    def add_share(self):
        while True:
            try:
                self.driver.find_element_by_accessibility_id('Shared').click()
                break
            except:
                pass
        time.sleep(0.5)
        self.driver.find_element_by_accessibility_id('Add').click()
        self.driver_id('com.intelligent.tapp.test:id/userLabel').click()
        # self.driver_id('com.intelligent.tapp.test:id/add').click()
        while True:
            try:
                self.driver.find_element_by_xpath("//*[@text='freemrtan@gmail.com']").click()
                break
            except:
                pass
        self.driver_id('com.intelligent.tapp.test:id/lockLabel').click()
        self.driver_xpath("//*[@text='" + self.value + "']").click()
        self.driver_id('com.intelligent.tapp.test:id/accessLabel').click()
        self.driver_id('com.intelligent.tapp.test:id/permanent').click()
        self.driver_id('com.intelligent.tapp.test:id/save').click()
        self.driver_id('com.intelligent.tapp.test:id/retry').click()
        sleep = 0
        while True:
            if sleep > 5:
                print('等待超过5S，且获取不到分享结果，判定为: \033[7;31m 分享失败 \033[1;31;0m !')
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/content')
                print('分享授权成功！')
                break
            except:
                time.sleep(2)
                sleep += 2
                pass


class setting(driver_by):
    def __init__(self, driver, android_version):
        super().__init__()
        self.driver = driver
        self.android_version = android_version

    def change_name(self):
        firstn = str(input('请输入新 first name:'))
        lastn = str(input('请输入新 last name:'))
        self.driver_id('com.intelligent.tapp.test:id/name').click()
        self.driver_id('com.intelligent.tapp.test:id/firstName').send_keys(firstn)
        self.driver_id('com.intelligent.tapp.test:id/lastName').send_keys(lastn)
        self.driver_id('com.intelligent.tapp.test:id/md_button_positive').click()
        name = self.driver_id('com.intelligent.tapp.test:id/name').text
        # print(name)
        if name == '%s %s' % (firstn, lastn):
            print('修改新名称成功！')
        else:
            print('\033[7;31m 修改新名称失败 \033[1;31;0m')

    def change_picture(self):
        self.driver.find_element_by_accessibility_id('Setting').click()
        self.driver_id('com.intelligent.tapp.test:id/avatar').click()
        if self.android_version == 10:
            self.driver_id('com.android.permissioncontroller:id/permission_allow_button').click()
        elif self.android_version == 9:
            self.driver_id('com.android.packageinstaller:id/permission_allow_button').click()
        while True:
            try:
                self.driver.find_element_by_id('com.intelligent.tapp.test:id/btn_ok').click()
                break
            except:
                self.driver.tap([(random.sample(range(200, 900), 1)[0], random.sample(range(600, 1200), 1)[0])])

    def change_pwd(self, password, file):
        self.driver_id('com.intelligent.tapp.test:id/changePass').click()
        self.driver_id('com.intelligent.tapp.test:id/oldPass').send_keys(password)
        newpwd = str(input('请输入新密码:'))
        file.seek(0)
        file.truncate()
        file.write(newpwd)
        file.close()
        self.driver_id('com.intelligent.tapp.test:id/newPass').send_keys(newpwd)
        self.driver_id('com.intelligent.tapp.test:id/repeatPass').send_keys(newpwd)
        self.driver_id('com.intelligent.tapp.test:id/save').click()
