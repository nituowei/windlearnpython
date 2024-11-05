


"""
import time
import os
import winsound

time_count = int(input("请输入倒计时需要的秒数:"))

for x in range(time_count, 0, -1):
    seconds = x % 60
    minutes = x // 60
    print(f"{seconds,02}:{minutes,02}")\
    time.sleep(1)

print("时间到啦！！！")
os.system('echo \a')
winsound.Beep(1000, 500)  # 频率 1000 Hz，持续时间 500 毫秒
"""

