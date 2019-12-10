# 减少了变量的使用
# 键盘接收的是两个字符串不能进行相乘先转成浮点类型 float
# 输入单价
price = float(input("请输入单价："))
# 输入重量
weight = float(input("请输入重量："))
# 计算价格
money = price * weight
print(money)

print("水果单价为：%f；水果重量为：%f；总价格为：%f" % (price, weight, money))
# 控制小数点显示几位
print("水果单价为：%.2f；水果重量为：%.3f；总价格为：%.4f" % (price, weight, money))
