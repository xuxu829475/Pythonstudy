# 在python中，定义变量是不需要指定变量的类型的
# 在运行的时候，python解释器，会根据赋值语句等会右边的数据
# 自动推导出变量中保存数据的准确类型
# str 字符串类型
name = "小明"
# int整数类型
age = 18
# bool 布尔类型  真 True 假 False
gender = True
# float 浮点类型
height = 1.75

weight = 75
print(name)

# 字符串拼接 两个字符串用 + 相连
last_name = "张"
print(last_name + name)
# 字符串多次输出 用 *
print((last_name + name) * 10)

# input() 键盘输入 输入的结果都是字符串类型
password = input("请输入密码：")
print(password)
