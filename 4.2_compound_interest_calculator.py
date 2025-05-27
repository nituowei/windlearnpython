# python 计算复利的程序
# 公式: 总金额 = 本金 * (1 + 利率) ** 年数
# 这里的利率是一个小数, 比如 5% 就是 0.05, 需要用 float 格式 或者转换输入为 float 格式.

#一下为自己思路编写的代码, 考虑到了确保输入的问题.
#先设好变量
principal = 0 
rate = 0 
years = 0

while True:
    try:
        while principal <= 0:  # 确保本金大于0
            principal = float(input("请输入本金: "))  # 输入本金
            if principal <= 0:
                print("本金必须大于0，请重新输入。")
            else :
                principal = principal  # 如果输入有效，跳出循环
        break  # 如果输入有效，跳出循环
    except ValueError:
        print("输入无效，请确保输入的是数字, 请重新输入。") # 处理输入错误的情况
while True:
    try:
        while rate <= 0:  # 确保年利率不为负数
            rate = float(input("请输入年利率（例如5%输入0.05）: "))  # 输入年利率
            if rate < 0:
                print("年利率不能为负，请重新输入。")
            else:
                rate = rate
        break  # 如果输入有效，跳出循环
    except ValueError:
        print("输入无效，请确保输入的是数字且利率不能为负, 请重新输入。") # 处理输入错误的情况
while True:
    try:
        while years <= 0:  # 确保投资年数大于0
            years = int(input("请输入投资整年数,例如三年就输入3）: "))  # 输入投资年数
            if years <= 0:
                print("投资年数必须大于0，请重新输入。")
            else:
                years = years
        break  # 如果输入有效，跳出循环
    except ValueError:
        print("输入无效，请确保输入的是整数, 请重新输入。") # 处理输入错误的情况
# 计算总金额
amount = principal * (1 + rate) ** years
# 打印结果
print(f"总金额为: {amount:.2f} 元")  # 保留两位小数



# #一下为LLM生成

# amount = 0  
# principal = 0 
# rate = 0 

# while True:
#     try:
#         principal = float(input("请输入本金: "))  # 输入本金
#         if principal <= 0:
#             print("本金必须大于0，请重新输入。")
#             continue
#         rate = float(input("请输入年利率（例如5%输入0.05）: "))  # 输入年利率
#         if rate < 0:
#             print("年利率不能为负，请重新输入。")
#             continue
#         years = int(input("请输入投资年数: "))  # 输入投资年数
#         if years <= 0:
#             print("投资年数必须大于0，请重新输入。")
#             continue
#         break  # 如果输入有效，跳出循环
#     except ValueError:
#         print("输入无效，请确保输入的是数字。")
# # 计算总金额
# amount = principal * (1 + rate) ** years
# # 打印结果
# print(f"总金额为: {amount:.2f} 元")  # 保留两位小数


# while True:
#     print("请输入本金:")
#     principal = float(input())
#     print("请输入利率:")
#     rate = float(input())
#     print("请输入年数:")
#     years = int(input())
#     amount = principal * (1 + rate) ** years
#     print("总金额为:", amount)
#     print("是否继续?(y/n)")
#     choice = input()
#     if choice == 'n':
#         print("程序结束")
#         break
#     elif choice != 'y':
#         print("输入错误，请输入 y 或 n")
#         continue
#     # 如果用户输入 y，就继续循环，重新输入本金、利率和年数
#     # 如果用户输入 n，就结束程序