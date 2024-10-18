"""
x=5
y=12
age=x + y
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
x = 1
x = x + 1 # equals : x += 1
x += 1 # x-=1 ,  x *=1 , x /= 1 etc will work as expected.
print(x)


#python中的运算符
x = 1
x = x + 1 # equals : x += 1
x += 1 # x-=1 ,  x *=1 , x /= 1 etc will work as expected.
print(x)
'''