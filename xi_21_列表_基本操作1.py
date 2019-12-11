# python中的列表相当于java中的数组

name_list = ["张三", "李四", "王五"]
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

# 增加
# append 在末尾添加数据
name_list.append("王小二")
print(name_list)
# insert 在指定的索引位置添加数据
name_list.insert(1, "小哥哥")
print(name_list)

# extend 将另外一个列表的内容追加到本列表后面
temp_list = ["小红", "小明"]
name_list.extend(temp_list)
print(name_list)

# 删除
# remove 从列表中删除指定数据
name_list.remove("小红")
print(name_list)

# pop 不传下标默认删除列表最末尾的数据
# 如果有下标就删除对于下标的数据
name_list.pop()
print(name_list)
name_list.pop(0)
print(name_list)

"""
 注意如果使用del关键字将变量删除，后续代码中就不能在使用此变量
 因为此变量在内存中已经被删除了
"""
# del 关键字本质上是将一个变量从内存中删除
del name_list[1]
print(name_list)

# clear 清空列表
name_list.clear()
print(name_list)
