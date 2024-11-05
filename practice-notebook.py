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
    

