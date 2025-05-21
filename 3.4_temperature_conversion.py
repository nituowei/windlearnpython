# python 温度转换器

import math
# 1. 首先，程序提示用户输入温度单位（摄氏度或华氏度）。
temperature_unit = input("请输入温度单位 (C 或 F): ")
# 2. 然后，程序提示用户输入温度值。
temperature_value = float(input("请输入温度值: "))
# 3. 根据用户输入的温度单位，程序执行相应的转换。
if temperature_unit == 'C':
    # 4. 如果单位是摄氏度，程序将温度值转换为华氏度。
    temperature_value = (temperature_value * 9/5) + 32
    temperature_value = round(temperature_value, 2)
    # 四舍五入到小数点后两位
    temperature_unit = 'F'
    print("转换后的温度是: ", temperature_value, temperature_unit)
elif temperature_unit == 'F':
    # 5. 如果单位是华氏度，程序将温度值转换为摄氏度。
    temperature_value = (temperature_value - 32) * 5/9
    temperature_value = round(temperature_value, 2)
    # 四舍五入到小数点后两位
    temperature_unit = 'C'
    print("转换后的温度是: ", temperature_value, temperature_unit)
else:
    # 6. 如果用户输入的单位不在摄氏度和华氏度中，程序将返回错误信息。
    print(f"您输入的'{temperature_unit}'不是正确的温度单位,请输入C 或 F")
