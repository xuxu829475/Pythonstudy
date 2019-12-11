# 定义函数
# 定义了函数后之表示这个函数封装了一段代码，运行此py是没有输出结果的
# 只有在调用时才会执行

name = "我是变量"


def multiple_table():
    """
    函数的说明注释
    python官方规范函数上方留两行空行
    """
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("%d * %d = %d" % (col,row,row*col),end="  ")
            # 为了对齐 \t转义制表符
            print("%d * %d = %d" % (col, row, row * col), end="\t")
            col += 1
        print("")
        row += 1

# 调用  调用必须再函数封装的下方
# multiple_table()
