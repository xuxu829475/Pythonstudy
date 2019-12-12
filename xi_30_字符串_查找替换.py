# 在python中能用 双引号"" 或者单引号 '' 来定义字符串
# 在开发是绝大多数使用双引号 ""

hello_str = "hello python"

# 判断是否以指定字符串开始 区分大小写
print(hello_str.startswith("hello"))

# 判断是否以指定字符串结尾 区分大小写
print(hello_str.endswith("hon"))

# 查找指定字符串 返回下标
# 和index方法相似 如果指定的字符串不存在 index会报错 find 会返回-1
print(hello_str.find("llo"))

# 替换字符串
print(hello_str.replace("python", "world"))
print(hello_str)
# replace替换后会返回一个新的字符串，需要有个变量接受，不会修改原有的字符串
hello_str1 = hello_str.replace("python", "world")
print(hello_str1)
