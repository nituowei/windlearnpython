# 字符串方法是字符串对象的内置方法，用于处理字符串数据
# python 的常用的字符串方法
# 'len()'：返回字符串的长度 
# 'find()'：返回子字符串在字符串中第一次出现的位置
# 'capitalize()'：将字符串的第一个字符转换为大写字母，其余字符转换为小写字母
# 'upper()'：将字符串转换为大写字母
# 'lower()'：将字符串转换为小写字母
# 'count()'：返回特定子字符串在字符串中出现的次数
# 'replace()'：替换变量中的特定子字符串,并输出一个新的变量,老变量不变.

# 'help(str)'：查看字符串对象的所有方法

#以下是具体示例

# # 使用者的全名
# name = "wind Ni 倪拓威"

# # 使用者的全名的长度
# length_name = len(name)   #返回字符串的长度, 包括空格和中文字符
# print(f"使用者的全名的长度是：{length_name}")

# # 找到第一个空格的位置
# space_pos = name.find(" ")  #返回子字符串在字符串中第一次出现的位置
# print(f"第一个空格的位置是：{space_pos}")  #注意输出的结果是从0开始的,而不是 1

# # 让变量的第一个字母变成大写字母
# name_capitalized = name.capitalize()  #将字符串的第一个字符转换为大写字母，其余字符转换为小写字母
# print(f"把变量name的第一个字母变成大写字母并把其他字母变成小写字母,之后是：{name_capitalized}") 


# # 让变量的所有字母变成大写字母
# name_upper = name.upper()  #将字符串转换为大写字母
# print(f"把变量name的所有字母变成大写字母,之后是：{name_upper}")

# # 让变量的所有字母变成小写字母
# name_lower = name.lower()  #将字符串转换为小写字母
# print(f"把变量name的所有字母变成小写字母,之后是：{name_lower}")

# # 统计变量中某个子字符串出现的次数
# name_count = name.count("n")  #返回特定子字符串在字符串中出现的次数
# print(f"变量name中子字符串n出现的次数是：{name_count}") #这里的n是小写字母n,所以结果不会包含大写的N个数.

# # 替换变量中的某个子字符串为另一个子字符串, 格式为 replace(old, new[, count])
# name_replaced = name.replace(" ", "_") #替换name变量中的空格为下划短线.
# print(f"变量name中空格替换为下划线,之后是：{name_replaced}") 
# #注意这里的replace方法是不会改变原来的变量的,而是返回一个新的变量.

# # 判断字符串中是否包含除字母以外的其他字符
# # name = "wind Ni 倪拓威"
# name = 'WindNi'
# if name.isalpha():  #判断字符串是否只包含字母
#     print("字符串只包含字母")
# else:
#     print("字符串包含除字母以外的其他字符")

# 下面是一个练习, 需要将以上代码先全部注释.
# 对特定场景下使用者输入的内容进行格式的限制.比如这里要求对使用者输入的名称进行限制.
# 1 输入内容不超过 12 个字符
# 2 输入内容不能包含空格
# 3 输入内容不能包含数字
# 4 以上要求有任意一条不满足, 则输出提示信息.
# 4 如果满足以上条件, 输出 欢迎 + 使用者名称.

name = input("请输入您的姓名,并注意以下限制: \n1 输入内容不超过 12 个字符\n2 输入内容不能包含空格\n3 输入内容不能包含字母以外的其他字符\n请开始输入: ")  # 输入使用者的姓名

if len(name) >= 12:  # 判断输入的姓名是否超过 12 个字符
    print("使用者名称不能超过 12个字符, 请重新输入.")
elif " " in name:  # 判断输入的姓名是否包含空格
    print("使用者名称包含空格, 请重新输入.")
elif not name.isalpha():  # 判断输入的姓名是否包含数字
    print("使用者名称包含字母以外的其他字符, 请重新输入.") 
else:
    print(f"欢迎你, {name} !")


'''
以下是 LLM 生成的
1. capitalize()：将字符串的第一个字符转换为大写字母，其余字符转换为小写字母
2. casefold()：将字符串转换为小写字母，适用于不区分大小写的比较
3. center(width[, fillchar])：返回一个指定宽度的字符串，字符串居中，使用指定的填充字符填充
4. count(substring[, start[, end]])：返回子字符串在字符串中出现的次数
5. encode(encoding="utf-8", errors="strict")：将字符串编码为字节串，使用指定的编码格式和错误处理方式
6. endswith(suffix[, start[, end]])：判断字符串是否以指定的后缀结尾
7. expandtabs(tabsize=8)：将字符串中的制表符（\t）替换为指定数量的空格
8. find(substring[, start[, end]])：返回子字符串在字符串中第一次出现的位置，如果未找到则返回 -1
9. format(*args, **kwargs)：格式化字符串，使用指定的参数替换占位符
10. format_map(mapping)：格式化字符串，使用指定的映射对象替换占位符
11. index(substring[, start[, end]])：返回子字符串在字符串中第一次出现的位置，如果未找到则引发 ValueError
12. isalnum()：判断字符串是否只包含字母和数字
13. isalpha()：判断字符串是否只包含字母
14. isascii()：判断字符串是否只包含 ASCII 字符
15. isdecimal()：判断字符串是否只包含十进制数字
16. isdigit()：判断字符串是否只包含数字
17. isidentifier()：判断字符串是否是一个有效的标识符
18. islower()：判断字符串是否只包含小写字母
19. isnumeric()：判断字符串是否只包含数字字符
20. isprintable()：判断字符串是否只包含可打印字符
21. isspace()：判断字符串是否只包含空格字符
22. istitle()：判断字符串是否是标题格式（每个单词的首字母大写）
23. isupper()：判断字符串是否只包含大写字母
24. join(iterable)：将可迭代对象中的字符串连接成一个字符串，使用指定的分隔符
25. ljust(width[, fillchar])：返回一个指定宽度的字符串，字符串左对齐，使用指定的填充字符填充
26. lstrip([chars])：返回一个去除字符串左侧指定字符的字符串
27. partition(sep)：将字符串分为三部分：分隔符前的部分、分隔符和分隔符后的部分
28. replace(old, new[, count])：返回一个替换指定子字符串的新字符串
29. rfind(substring[, start[, end]])：返回子字符串在字符串中最后一次出现的位置，如果未找到则返回 -1
30. rindex(substring[, start[, end]])：返回子字符串在字符串中最后一次出现的位置，如果未找到则引发 ValueError
31. rjust(width[, fillchar])：返回一个指定宽度的字符串，字符串右对齐，使用指定的填充字符填充
32. rsplit(sep=None, maxsplit=-1)：将字符串从右侧分割为多个子字符串，返回一个列表
33. rstrip([chars])：返回一个去除字符串右侧指定字符的字符串
34. split(sep=None, maxsplit=-1)：将字符串分割为多个子字符串，返回一个列表
35. splitlines(keepends=False)：将字符串按行分割为多个子字符串，返回一个列表
36. startswith(prefix[, start[, end]])：判断字符串是否以指定的前缀开头
37. strip([chars])：返回一个去除字符串两侧指定字符的字符串
38. swapcase()：返回一个将字符串中大写字母转换为小写字母，小写字母转换为大写字母的新字符串
39. title()：返回一个将字符串转换为标题格式的新字符串
40. upper()：返回一个将字符串转换为大写字母的新字符串
'''