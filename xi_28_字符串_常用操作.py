# 在python中能用 双引号"" 或者单引号 '' 来定义字符串
# 在开发是绝大多数使用双引号 ""
string = "Hello Python"
#  len 获取字符串长度
print(len(string))

# count 统计某个子字符出现的次数
print(string.count("lo"))

# 某个子字符串出现的位置
# 如何有多个，输出第一次出现的位置
print(string.index("o"))
