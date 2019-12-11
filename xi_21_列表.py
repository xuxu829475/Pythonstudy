# python中的列表相当于java中的数组

name_list = ["张三","李四","王五"]
# 取值
print(name_list)
print(name_list[0])
print(name_list[1])
print(name_list[2])
# 去索引 知道数据的内容，想取数据再列表中的位置
print(name_list.index("李四"))
# 修改
name_list[2] = "赵六"
print(name_list[2])