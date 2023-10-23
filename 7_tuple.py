#tuple 元组
#tuple是通过小括号 ( ) 来包含多个变量的
#tuple中的元素是有顺序的，并且不能够被改变
#tuple中的元素无法被添加和删除，相对tuple进行改动，改动后只能重新声明新的tuple
"""
元组(tuple)就像是一盒装好的奶茶,元组中的元素是固定顺序且不可变的。
它就像一个不可变的列表,通常用于存储结构固定的记录,比如人的姓名、年龄、性别等。
适合存储不需要修改的结构化数据。
"""

#声明一个tuple
face_tuple = ("😊", "😂", "🤣", "😍",  "😍")

# #用for loop 打印tuple中的每个元素
# for x in face_tuple:
#     print(x, end=" ")
# #output : 😊 😂 🤣 😍
# #这里尤其要注意，tuple和set不同，是有顺序之分的，所以这里的输出是按照原本的顺序的。

#其他操作的话
#添加：和set中的添加元素方法一致，是用add，而不是在list中使用的append

# #计算某个元素数量：count
# count = face_tuple.count( "😍")
# print( count)
# #output :  2

# #索引：index
# index = face_tuple.index( "😍")
# print( index)
# #output :  3
# #这里尽管有两个😍,但是会输出第一次出现的序号.

# #查询bard,给出遍历所有元素并打印出所有元素的方法
#
# # 创建一个空列表来存储😍的序号
# index_list = []  #这时候index_list就已经是一个list了,因为是一个 [ ]
#
# # 遍历元组  - enumerate : 列举,枚举
# for i, item in enumerate(face_tuple):
#     if item == "😍":
#         # 如果找到😍，则将其序号添加到列表中
#         index_list.append(i)
#
# # 打印😍的序号
# print(index_list)
# # output :  [3, 4]

#这只是众多方法中的一个,但是它使用了list,还有一种直接打印的
# 使用 enumerate() 函数来获取元素的值和序号
for i, item in enumerate(face_tuple):
    if item == "😍":
        # 如果找到😍，则打印其序号
        print(i, end= "  ")
# output :  3  4
#这样果然方便很多.

# #想tuple添加一个元素是不被允许的
# face_tuple.add= ("😘")
# for x in face_tuple:
#     print(x, end=" ")
# #output : 直接报错了，因为tuple根本不支持add
# # Traceback (most recent call last):
# #   File "C:\python\D1\7_tuple.py", line 21, in <module>
# #     face_tuple.add= ("😘 ")
# # AttributeError: 'tuple' object has no attribute 'add'
