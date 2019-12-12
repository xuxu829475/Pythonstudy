# 在python中能用 双引号"" 或者单引号 '' 来定义字符串
# 在开发是绝大多数使用双引号 ""

# isspace 判断字符串是否为空白字符  \r\n\t 等都算空白字符
string1 = " "
print(string1.isspace())

# 判断字符串中是否只包含数字
# 1：这三个方法都不能判断小数
# isdecimal 能识别：全角数字
# isdigit 能识别：全角数字，Unicode字符串
# isnumeric 能识别：全角数字，中文数字
num_str = "1.1"
num_str0 = "\u00b2"
num_str1 = "一千六百八十八"
print(num_str0.isdecimal())
print(num_str0.isdigit())
print(num_str0.isnumeric())
