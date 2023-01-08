import time
import os
import threading


class TimeCmp:
    def __init__(self, TimeStart, TimeEnd):
        self.TimeStart = TimeStart
        self.TimeEnd = TimeEnd

    def Cmp(self):
        LocalTime = time.localtime(time.time())
        self.__TimeNow_1 = LocalTime.tm_hour*3600+LocalTime.tm_min*60+LocalTime.tm_sec
        self.__TimeStart_1 = 3600 * \
            self.TimeStart[0]+60*self.TimeStart[1]+self.TimeStart[2]
        self.__TimeEnd_1 = 3600 * \
            self.TimeEnd[0]+60*self.TimeEnd[1]+self.TimeEnd[2]

        if self.__TimeNow_1 > self.__TimeStart_1 and self.__TimeNow_1 < self.__TimeEnd_1:
            return True
        else:
            return False


def run():
    TimeStart = (6, 0, 0)
    TimeEnd = (18, 00, 00)
    SystemCmd = 'shutdown /s /c "系统将在60s后关机！" /t 60'
    while True:
        TimeCmpResult = TimeCmp(TimeStart, TimeEnd)
        shutdown = not TimeCmpResult.Cmp()
        if shutdown:
            print("电脑将在60s后关机！")
            os.system(SystemCmd)
            exits = input('按<e>取消：')
            if exits == 'e':
                password = input('请输入密码：')
                if password == 'wwrz201803':
                    os.system('shutdown /a')
                else:
                    print('密码错误！')
        else:
            print("Computer is on")
            pass
        time.sleep(float(600))


if __name__ == "__main__":
    run()
