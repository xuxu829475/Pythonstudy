# python中的元组 和列表类似，不同之处是元组的 元素不能修改
info_tuple = ("zhangsan", 18, 1.75)
print(info_tuple[0])
print(info_tuple[1])
print(info_tuple[2])

# 创建空元组 ，一般不建议这么操作，因为一旦元组被定义就不能修改了
empty_tuple = ()

# 定义一个只包含一个元素的元组
# single_tuple = (5)  这样是不行，解析器会识别为一个整数
single_tuple = (5,)

# count 指定元素在元组中出现的次数
print(info_tuple.count(18))

# index 取索引值，（已经知道该数据的值，想获取该数组再元组中的索引）
print(info_tuple.index("zhangsan"))

# len 同意元组的长度
print(len(info_tuple))

