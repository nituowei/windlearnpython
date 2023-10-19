#python中的集合类型  list, sets, tuple
#dictionary下个章节讲解
#list  把多个数值存储到一个变量中

#通过中括号来包含多个变量
fruits = ["apple", "orange", "banana", "coconut"]

# #通过索引（从第一个0，1，2...）的形式来读取
# print(fruits[3]) #这里3就代表是第四个,所以输出coconut

# #通过for循环,将list中的所有的元素打印出来
# for f in fruits:
#     print(f)

# #添加元素的方式: append - 附加
# fruits.append("kivi")
# print(fruits)
# #输出的结果 ['apple', 'orange', 'banana', 'coconut', 'kivi']

# #移除元素的方式: remove - 移除
# fruits.remove("banana")
# print(fruits)
# #输出的结果 ['apple', 'orange', 'coconut']

# #对list中的元素进行索引: index - 索引
# #索引的目的是想知道元素所在的位置,也就是元素是第几个
# print(fruits.index("banana"))
# #输出的结果: 2 (也就是第三个)

# #list也可以传入同样的值,即允许重复的元素出现
# fruits.append("apple")
# print(fruits)
# #输出的结果['apple', 'orange', 'banana', 'coconut', 'apple']
# #当然,apple是新加入的,自然在最后一位

# #那我想知道list中某个元素出现过多少次,或者说某个元素共有多少个重复的元素
# #需要使用count方法
# fruits.append("apple")
# fruits.append("apple")
# fruits.append("apple")
# print(fruits.count("apple"))
# #输出的结果: 4

# #对list中的元素进行逆向排序
# #使用reverse 方法 - 逆转
# print(fruits)
# fruits.reverse()
# print(fruits)
# #输出的结果:
# # ['apple', 'orange', 'banana', 'coconut']
# # ['coconut', 'banana', 'orange', 'apple']

