# 在python中能用 双引号"" 或者单引号 '' 来定义字符串
# 在开发是绝大多数使用双引号 ""

string = "   hello          "
print(string)
# 去除空白字符
print(string.strip())

# 拆分
string1 = "白日依山尽,黄河入海流"
poem_list = string1.split(",")
print(poem_list)

# 合并
string2 = "欲穷千里目,更上一层楼"
string3 = string1.join(string2)
print(string3)


# 截取（切片）
string = "0123456789"
# 截取2-5的字符串
print(string[2:6])
# 截取2-末尾的字符串
print(string[2:])
# 截取从开始 - 5的字符串
print(string[0:6])
print(string[:6])
# 截取完整的字符串
print(string[:])
# 从开始位置每隔一个字符截取字符串
print(string[::2])
# 从索引 1 开始，每隔一个取一个
print(string[1::2])
# 从2~末尾 -1 的字符串
print(string[2:-1])
# 截取末尾两个字符
print(string[-2:])
# 字符串的逆序（面试）
print(string[-1::-1])
print(string[::-1])
