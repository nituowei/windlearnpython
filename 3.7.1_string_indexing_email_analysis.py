#email 的字符串分析

email = 'windniabc@gmail.com'
index = email.index('@')
print(index)

# 获取email 的用户名, 也就是 @ 前面的字符
user_name = email[0 : index] 
# 这里的[0:index] 也可以省略第一个 0, 直接写成 [ : index]
# 第一个参数不写, 就代表从第一个字符开始, 也就是 0.
# 但是如果是第二个参数不写, 就代表到最后一个字符结束, 也就是 -1. 下面有应用
print(f'Your uesr name is "{user_name}"')

# 获取email 的域名, 也就是 @ 后面的字符
domain_name = email[index + 1:]
# 这里必须注意, 这是依然是正向数, 也就是从index + 1 dao 到最后一个字符.
# 但是如果你错误的认为是倒数,写了[index + 1 : -1], 那么会漏掉最后一个字符, 因为正向数是会忽略最后一个字符的.
# 因此, 如果要用 -1, 那么第一个字符也得是负数才行. 但是这需要知道倒着数的话, 第一个参数是倒数第几个.
# 在这里, 直接不写第二个参数即可, 表示从某个参数到最后一个参数. 也能获取域名.
print(f'Your email domain name is "{domain_name}"')
