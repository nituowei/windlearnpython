# python 子串索引其实很简单, 通过符号 []  来获取子串

credit_num = '1234@5678-9012-3456'

first_char = credit_num[0] 
# 获取第一个字符, 注意在 Python 中, 0 表示第一个字符, -1 表示最后一个字符.
print(first_char)

# 获取第二个字符
second_char = credit_num[1] # 1标识第二个字符
print(second_char)

#获取特定范围的字符
# 获取前四个字符
first_four_chars = credit_num[0:4] 
#这里的 0:4 表示从第一个字符到第四个字符, 但是不包括最后一个也就是第四个字符.
#所以理解起来, [0:4] 其实是 [0, 1, 2, 3] 这四个字符, 可以理解[0,4]为实际顺序的[0+1, 4].
#反过来说,如果要第 x个到第 y 个字符, 应该写[x-1,y]
#也就是实际顺序的, 第1个字符到第4个字符.
print(first_four_chars)

#获取第4 个到第 9个字符
the_four_to_nine_chars = credit_num[3:9]
print(the_four_to_nine_chars)

#在从后往前数的时候, 就不是从 0 开始了.
# -1 直接就表示最后一个字符, -2 表示倒数第二个字符. 

#获取最后一个字符
last_char = credit_num[-1]
print(last_char)

#获取倒数第二个字符
second_last_char = credit_num[-2]
print(second_last_char)

#获取倒数第4个到倒数第9个字符
# the_last_four_to_nine_chars = credit_num[-4:-9] # 这么写看似对实际错误.
#注意,虽然是倒数第4 个到倒数第9个字符, 但是[x,y]中的x 和 y 必须满足 x < y
#因此, 要正确获取倒数第4个到倒数第9个字符, 也就是从后往前的时候, 需要数字顺序为也从后往前, 否则会报错.
#所以 , 正确的写法是:
the_last_four_to_nine_chars = credit_num[-9:-4] #这里表示范围的时候, 也从后往前了,其实很有意思
print(the_last_four_to_nine_chars)

# 使用 index()方法, 获取某个字符在变量中的具体位置
index = credit_num.index('@')
print(index) 
# 这里再次强调 正向顺序是从 0 开始的, 也就是如果输出的是 4, 那么表示的是第5个字符.
# 但是实际的程序编写的过程中, 你可以直接使用这个数字来获取字符, 也就是 credit_num[4] 就是 @.
# 因为第五个字符就是程序认为的第4个字符, 也就是 credit_num[4] = '@'  