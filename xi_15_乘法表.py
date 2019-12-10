row = 1
while row <= 9:
    col = 1
    while col <= row:
        # 为了对齐 \t转义制表符
        print("%d * %d = %d" % (col,row,row*col),end="\t")
        # print("%d * %d = %2d" % (col,row,row*col),end="  ")
        col += 1
    print("")
    row += 1
