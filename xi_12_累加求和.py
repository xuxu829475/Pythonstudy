# 计算0-100之间所有数组累加的和
# 定义记录循环次数的变量
i = 0
# 定义最终结果的变量
total = 0
while i <= 100:
    # 赋值运算符
    total += i
    i += 1

print("0-100之间的数字求和的结果为：%d " %total)