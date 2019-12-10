# 1.0
row = 1
while row <= 9:
    print("*" * row)
    row += 1

# 2.0在默认情况下，print函数在输出时会再末尾加上换行 再末尾加上 end="" 就不会换行了
row = 1
while row <= 9:
    col = 1
    while col <= row:
        if col == row:
            print("*")
        else:
            print("*", end="")
        col += 1

    row += 1
# 3.0
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1

# 这个案例有点懵，主要是演示嵌套循环和过度到乘法表