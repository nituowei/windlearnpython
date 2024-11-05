# python中的集合类型  list, set, tuple
# dictionary下个章节讲解
# list  把多个数值存储到一个变量中
"""
列表(list)是 Python 最常用的类型,就像生活中的购物单一样。它是一串有序可变的元素集合,
可以添加、删除和修改列表中的元素。适合存储需要频繁变动的数据,比如学生姓名列表。
"""

#list是通过中括号 [] 来包含多个变量的
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

"""
students = ["张三", "李四", "王五", "赵六"]

# # print(students[0])
# for x in students:
#     print(x , end=" ")  #output every x and change line

students.append("孙七")
students.remove("王五")

for x in students:
    order = students.index(x) + 1
    # print(students.index(x) + 1) 
    print(f"{x} 在第{order}个位置")
"""

# ----------

"""
students = ["张三", "李四", "王五", "赵六"]

students.append("孙七")
students.remove("王五")
students.append("孙七")
students.append("孙七")
students.append("孙七")

for x in students:
    order = students.index(x) + 1
    # print(students.index(x) + 1) 
    print(f"{x} 在第{order}个位置")

count_name = students.count("孙七")
print(f"孙七出现了{count_name}次")

以上代码有一个功能是输出“孙七”在什么位置，
但是因为有四个孙七，所以第五个以及后面的孙七的位置数字就不对了，
而是错误的显示为第4个，请问怎么样才能让这种相同元素也可以正确的显示各自正确的index信息

------
### 问题分析

当前代码中，`students.index(x)` 方法会返回列表中第一次出现 `x` 的索引位置。因此，对于重复的元素（如 "孙七"），它总是返回第一个 "孙七" 的索引位置，导致后续的 "孙七" 位置显示不正确。

### 解决方案

为了正确显示每个 "孙七" 的位置，可以使用 `enumerate` 函数来遍历列表，这样可以直接获取每个元素的索引和值。

### 修改后的代码

```python
students = ["张三", "李四", "王五", "赵六"]

# 添加和删除学生
students.append("孙七")
students.remove("王五")
students.append("孙七")
students.append("孙七")
students.append("孙七")

# 使用 enumerate 遍历列表，获取每个元素的索引和值
for index, student in enumerate(students):
    order = index + 1
    print(f"{student} 在第{order}个位置")

# 统计 "孙七" 出现的次数
count_name = students.count("孙七")
print(f"孙七出现了{count_name}次")
```

### 代码解释

1. **初始化学生列表**：
   ```python
   students = ["张三", "李四", "王五", "赵六"]
   ```

2. **添加和删除学生**：
   ```python
   students.append("孙七")
   students.remove("王五")
   students.append("孙七")
   students.append("孙七")
   students.append("孙七")
   ```

3. **使用 `enumerate` 遍历列表**：
   ```python
   for index, student in enumerate(students):
       order = index + 1
       print(f"{student} 在第{order}个位置")
   ```
   - `enumerate(students)` 返回一个枚举对象，其中包含每个元素的索引和值。
   - `index` 是当前元素的索引，`student` 是当前元素的值。
   - `order = index + 1` 计算当前元素的位置（从1开始）。

4. **统计 "孙七" 出现的次数**：
   ```python
   count_name = students.count("孙七")
   print(f"孙七出现了{count_name}次")
   ```

这样修改后，每个 "孙七" 的位置都会正确显示。

"""