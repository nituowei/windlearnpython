import time  #引入 time模组

#time.sleep(1) #引入sleep函数，让程式睡眠若干时间，默认单位是S


my_time = int(input("Please input second count: "))

# for x in range(my_time):  #这里是正计时器
#     print(x+1)  #这里+1使得计数从1开始而不是默认的0
#     time.sleep(1)
# print("Time is up!")

# for x in range(my_time,0, -1):  #这里是倒计时器
#     #这里0是指范围的顺序，0其实就是range范围的第一个数字
#     #这里的 -1指的是步进值，这里步进值是 -1，说明每次减少1
#     print(x)
#     time.sleep(1)
# print("Time is up!")

for x in range(my_time, 0, -1):  #需要实现超过60秒就显示一分钟
    #120秒希望显示成：02：00
    seconds = x % 60 #秒数对60取余
    minutes = x // 60
    #这里 两个 // ，原来是int，计算后就不会被自动转成float了。

    #print(f"{minutes:2}:{seconds:2}")
    print(f"{minutes:02}:{seconds:02}") #这个里面的02中的0用处是把缺0的地方补上0
    #print(x+1)
    time.sleep(1)
print("Time is up!")