# python中的逻辑运算符有and、or和not。它们用于连接布尔表达式并返回布尔值。
# 逻辑运算符的优先级从高到低依次为：not、and、or。
# 逻辑运算符的优先级决定了在没有括号的情况下，表达式的计算顺序。
# 逻辑运算符的优先级可以通过括号来改变。

# # and 运算符的左右两边的条件都要为true, 结果才为true. 任意一边为false, 结果就为false.
# temp = int(input("请输入当前的温度:"))
# if temp > 30 and temp < 40:
#     print("天气炎热")
# elif temp > 20 and temp < 30:
#     print("天气温暖")
# elif temp > 10 and temp < 20:
#     print("天气凉爽")
# elif temp > 0 and temp < 10:
#     print("天气寒冷")
# else:
#     print("天气极端")

# # or 运算符的左右两边的条件只要有一边为true, 结果就为true. 两边都为false, 结果才为false.
# #如果输入的不是整数,提醒用户重新输入.
# while True:
#     try:
#         temp = int(input("请输入当前的温度:"))
#         break
#     except ValueError:
#         print("输入无效，请输入一个整数。")

# if temp > 30 or temp < 0:
#     print("天气极端")
# else:
#     print("天气正常")

# not 运算符用于反转布尔值, 如果条件为true, 结果为false. 如果条件为false, 结果为true.
while True:
    try:
        temp = int(input("请输入当前的温度:"))
        break
    except ValueError:
        print("输入无效，请输入一个整数。")

if not (temp > 30 or temp < 0):
    print("天气正常")
else:
    print("天气极端")