import time

#my_count_down = int(input("Enter a number: "))

while True:
    try:
        my_count_down = int(input("Enter a number: "))
        break
    except ValueError:
        print("输入错误！请输入一个整数。")

for x in range(my_count_down):
    print(x+1, flush=True, end=" ")
    time.sleep(1)

print(f"time is up")
    