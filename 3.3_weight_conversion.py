# python 体重转换器, 转换公斤和磅.
import math
# 1. 首先，程序提示用户输入体重单位（公斤或磅）。
weight_unit = input("请输入体重单位 (kg 或 lb): ")
# 2. 然后，程序提示用户输入体重值。
weight_value = float(input("请输入体重值: "))
# 3. 根据用户输入的体重单位，程序执行相应的转换。
if weight_unit == 'kg':
    # 4. 如果单位是公斤，程序将体重值转换为磅。
    weight_value = weight_value * 2.20462
    weight_value = round(weight_value, 2)
    # 四舍五入到小数点后两位
    weight_unit = 'lb'
elif weight_unit == 'lb':
    # 5. 如果单位是磅，程序将体重值转换为公斤。
    weight_value = weight_value / 2.20462
    weight_value = round(weight_value, 2)
    # 四舍五入到小数点后两位
    weight_unit = 'kg'
else:
    # 6. 如果用户输入的单位不在公斤和磅中，程序将返回错误信息。
    weight_value = "请输入正确的体重单位"
# 7. 最后，程序将输出转换后的体重值和单位。
print("转换后的体重是: ", weight_value, weight_unit)
