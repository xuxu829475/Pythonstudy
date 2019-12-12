# 在python中能用 双引号"" 或者单引号 '' 来定义字符串
# 在开发是绝大多数使用双引号 ""

poem = ["登鹳雀楼",
                "王之涣",
            "白日依山尽",
                "黄河入海流",
                    "欲穷千里目",
        "更上一层楼"]

for string in poem:
    print(string)

# 居中对齐 10：宽度
for string in poem:
    print("|%s|" % string.center(10, " "))

for string in poem:
    print("|%s|" % string.ljust(10, " "))

for string in poem:
    print("|%s|" % string.rjust(10, " "))
