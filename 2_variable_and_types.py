"""
x=5
y=12
age=x + y
print("My age is " + age + ".")  // TypeError: can only concatenate str (not "int") to str , 需要将int转换为str
print("My age is " + str(age) + ".")
"""


'''
#types

#integer 整数
age = 30

#float
gpa = 3.3

#string
name = 'wind' # string value must be included in " "

#boolean
like_cold = True # letter "T" must be capital.

print(f"I am {age} years old. My GPA is {gpa} . My name is {name}. Do I like cold cola? yes, it is {like_cold}.")
print(type(like_cold))  # print the type of the variable

在这里，f 是 Python 中 f-string 的前缀，用于在字符串中插入变量的值。f-string 是 Python 3.6 版本引入的一种字符串格式化方法，它使得在字符串中插入变量变得更加方便和可读。

在你提供的代码中，f"My GPA {gpa} 分" 这个字符串中，f 前缀表示这是一个 f-string。{gpa} 部分会被替换为变量 gpa 的实际值。整个字符串中的表达式会在运行时被计算和替换。

举个例子，如果 gpa 的值是 3.5，那么这个字符串在运行时就会变成 "My GPA 3.5 分"。

这种方式的字符串插值相比以前的格式化方法（如format方法或百分号占位符）更加简洁、可读，并且更易于理解。
'''

#change types
# age = 21 # age is int
# age = float(age) #age is float now
# print(age)
# print(type(age))


'''
#python中的运算符
#四则
#python中的运算符
x = 1
x = x + 1 # equals : x += 1
x += 1 # x-=1 ,  x *=1 , x /= 1 etc will work as expected.
print(x)
'''

'''
我发现这里没有说一些运算符的作用
比如百分号: %, 意思的取余数. 和调用了math 模块的mod 函数是一样的效果.
另外, 四舍五入的函数是round, 而 ceiling和floor 函数是math模块中的函数. 分别代表向上和向下取整. 
ceiling 是天花板, floor 是地板. 他们分别表示上限和下限.
另外, 还有一个函数是abs, 代表绝对值.
'''
# 取余数


# import math

# x = 10
# y = 3
# # z = x % y
# # print(z,z1)  # 输出 1

# # 四舍五入
# z1 = math.ceil(x / y)
# z2 = math.floor(x / y)
# z3 = round(x / y)
# print(z3)  # 输出 3
# print(z2)  # 输出 3
# print(z1)  # 输出 4
# # 向上取整



#圆周率pi 
import math
print(math.pi)  # 输出 3.141592653589793

#圆的周长和面积
pi = math.pi
radius = input("请输入圆的半径: ")
radius = float(radius)  # 将输入的字符串转换为浮点数
# 计算圆的周长和面积
circumference = 2 * pi * radius
area = pi * (radius ** 2)
print(f"圆的周长为: {(round(circumference, 2))}")
print(f"圆的面积为: {(round(area, 2))}")

