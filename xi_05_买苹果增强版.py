# 输入单价
price_str = input("请输入单价：")
# 输入重量
weight_str = input("请输入重量：")
# 计算价格
# 键盘接收的是两个字符串不能进行相乘先转成浮点类型 float
price_float = float(price_str)
weight_float = float(weight_str)

print(price_float * weight_float)
