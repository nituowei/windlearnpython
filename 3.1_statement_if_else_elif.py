# # if else elif 控制流程
# # Boolean 与布尔类型结合
# for_sale = True  # 定义一个布尔变量 for_sale，初始值为 True
# if for_sale:  #当 for_sale 为 True 时
#     # 这里的代码块会被执行
#     print("This item is for sale.")
# else: #当 for_sale 为 False 时
#     # 这里的代码块会被执行
#     print("This item is not for sale.")

# # if else
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你是成年人。")
# else:
#     print("你是未成年人。")

#elif 是 else if 的缩写
age = int(input("请输入你的年龄:"))
if age < 0:
    print("年龄不能为负数")
elif age < 18:
    print("你是未成年人")
elif age < 65:
    print("你是成年人")
else:
    print("你是老年人")

# 这个代码是一个简单的 Python 程序，它使用了 if-elif-else 语句来根据用户输入的年龄判断用户的年龄段。根据不同的年龄段，程序会打印出相应的消息。