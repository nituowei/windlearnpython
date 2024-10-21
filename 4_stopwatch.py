import time  #引入 time模组

#time.sleep(1) #引入sleep函数，让程式睡眠若干时间，默认单位是S


my_time = int(input("Please input second count: "))

# for x in range(my_time):  #这里是正计时器
#     print(x+1)  #这里+1使得计数从1开始而不是默认的0
#     #如果需要每次的结果打印出来之后不要自动换行，就 print(x+1, end=" ")
#     time.sleep(1)
# print("Time is up!")

# for x in range(my_time,0, -1):  #这里是倒计时器
#     #这里的 -1指的是步进值，这里步进值是 -1，说明每次减少1
#     #这里0是指范围的顺序，0其实就是range范围步进值的最后一个结果，即最小值。
#     #我发现在倒数的时候，最小的数字是1，但是在正数的时候 ，最小的数字也就是第一个数字会是1
#     #这个结果可以参见上面的正计时器的结果。
#     print(x)
#     time.sleep(1)
# print("Time is up!")

for x in range(my_time, 0, -1):  #需要实现超过60秒就显示一分钟
    #120秒希望显示成：02：00
    seconds = x % 60 #秒数对60取余
    minutes = x // 60  #取整
    #这里 两个 // ，原来是int，计算后就不会被自动转成float了。

    #print(f"{minutes:2}:{seconds:2}")
    print(f"{minutes:02}:{seconds:02}") #这个里面的02中的0用处是把缺0的地方补上0
    #print(x+1)
    time.sleep(1)
print("Time is up!")


#以下代码加入了try和excep，来确保一些已知的可能会产生的错误有应对的方法
# while True:
#     try:
#         my_count_down = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("输入错误！请输入一个整数。")

# for x in range(my_count_down):
#     print(x+1, flush=True, end=" ")
#     time.sleep(1)

# print(f"time is up")