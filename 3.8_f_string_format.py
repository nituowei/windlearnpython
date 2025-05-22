# python 中的 f-string 格式化
# f-string 是 Python 3.6 引入的一种字符串格式化方法,它允许在字符串中嵌入表达式，并在运行时求值
# 语法: f"string {expression}"
# f-string 是一种非常强大和灵活的字符串格式化方法,它可以让你在字符串中嵌入变量和表达式

price_1 = 4.4351   
price_2 = -66
price_3 = 15.11

# print(f"价格 1 为 {price_1}\n"
#       f"价格 2 为 {price_2}\n"
#       f"价格 3 为 {price_3}")  #最后一行不用换行

# # 格式化小数点的精度
# print(f"价格 1 为 {price_1:.2f}\n"
#       f"价格 2 为 {price_2:.2f}\n"
#       f"价格 3 为 {price_3:.2f}")  
# # .2f 表示强制保留两位小数, 多余的部分会四舍五入,少于的部分会补零.

# 为数字添加正号或者负号(混用正负号)
# print(f"价格 1 为 {price_1:+.2f}\n"
#       f"价格 2 为 {price_2:+.2f}\n"
#       f"价格 3 为 {price_3:+.2f}")
# +.2f 中的 + 表示强制显示正号或负号,如果数字为正数,不管原先有没有+号, 都统一显示 + 号,如果数字为负数,则显示 - 号

# 对齐功能 
# < 表示左对齐, > 表示右对齐, ^ 表示居中对齐
#这里的+10.2f中的 10, 表示强制输出结果宽度为10位. 需要注意混用正负号的'+'需要放在对齐符号的后面.
# 比如 <+.2f 是对的, +<.2f 是错的.
print(f"价格 1 为 {price_1:<+10.2f}\n" #输出结果向 左 对齐
      f"价格 2 为 {price_2:>+10.2f}\n" #输出结果向 右 对齐
      f"价格 3 为 {price_3:^+10.2f}") #输出结果 居中 对齐


'''
#以下为 AI 生成的教程
# 1. 基本用法
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Hello, my name is Alice and I am 30 years old.
# 2. 表达式
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}."
print(result)  # The sum of 10 and 5 is 15.
# 3. 调用函数
def square(n):
    return n * n
number = 4
result = f"The square of {number} is {square(number)}."
print(result)  # The square of 4 is 16.
# 4. 格式化数字
pi = 3.141592653589793
result = f"The value of pi is approximately {pi:.2f}." # 保留两位小数
print(result)  # The value of pi is approximately 3.14.
# 5. 多行字符串
multiline_string = f"""
This is a multi-line string.
It can span multiple lines.
"""
print(multiline_string)
# 6. 嵌套 f-string
name = "Bob"
age = 25
nested_greeting = f"Hello, my name is {name} and I am {age} years old. {f'Next year, I will be {age + 1}.'}"
print(nested_greeting)  # Hello, my name is Bob and I am 25 years old. Next year, I will be 26.
# 7. 使用字典
person = {"name": "Charlie", "age": 35}
greeting = f"Hello, my name is {person['name']} and I am {person['age']} years old."
print(greeting)  # Hello, my name is Charlie and I am 35 years old.
# 8. 使用列表
fruits = ["apple", "banana", "cherry"]
greeting = f"My favorite fruits are: {', '.join(fruits)}."
print(greeting)  # My favorite fruits are: apple, banana, cherry.
# 9. 使用条件表达式
is_adult = True
greeting = f"I am {'an adult' if is_adult else 'a minor'}."
print(greeting)  # I am an adult.
# 10. 使用格式化选项
number = 1234567.89
formatted_number = f"{number:,.2f}"  # 使用逗号分隔符和两位小数
print(formatted_number)  # 1,234,567.89
# 11. 使用日期格式化
from datetime import datetime
today = datetime.now()
formatted_date = f"Today's date is {today:%Y-%m-%d}."  # 格式化日期
print(formatted_date)  # Today's date is 2023-10-01.
# 12. 使用自定义格式化函数
def custom_format(value):
    return f"Value: {value}"
value = 42
formatted_value = f"{custom_format(value)}"
print(formatted_value)  # Value: 42
# 13. 使用转义字符
escaped_string = f"She said, \"Hello!\""
print(escaped_string)  # She said, "Hello!"
# 14. 使用原始字符串
raw_string = r"Raw string: \n\t"
print(raw_string)  # Raw string: \n\t
# 15. 使用格式化类型
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __format__(self, format_spec):
        return f"{self.name} ({self.age})"
person = Person("David", 40)
formatted_person = f"Person: {person}"
print(formatted_person)  # Person: David (40)
# 16. 使用格式化选项
class CustomFormatter:
    def __init__(self, value):
        self.value = value

    def __format__(self, format_spec):
        if format_spec == "upper":
            return self.value.upper()
        elif format_spec == "lower":
            return self.value.lower()
        return self.value
custom_value = CustomFormatter("Hello, World!")
formatted_upper = f"Upper: {custom_value:upper}"
formatted_lower = f"Lower: {custom_value:lower}"
print(formatted_upper)  # Upper: HELLO, WORLD!
print(formatted_lower)  # Lower: hello, world!
'''