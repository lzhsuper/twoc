import socket
import subprocess


class AppiumServer():

    def check_port(self, host, port):
        """检测端口是否被占用"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            s.shutdown(2)
            print('port %s is uesd !' %port)
            port += 2
            self.start_appium(host,port)
        except:
            print('port %s is available!' %port)
            return True

    def start_appium(self,host,port):
        """启动appium 服务"""
        # erromessage=""
        # appium_server_url=""
        # bootstrap_port=str(port+1)

        try:
            if self.check_port(host,port):

                cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' --bootstrap-port ' + str(port)
                print(cmd)

                # p = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                p.wait()

                appium_server_url = 'http://' + host + ':' + str(port) + '/wd/hub'
                print(appium_server_url)

        except Exception as msg:
            erromessage=str(msg)

        return appium_server_url#,erromessage


if __name__ == '__main__':
    s=AppiumServer()
    s.start_appium('127.0.0.1',4723)
    # s.start_appium('127.0.0.1',4725)
