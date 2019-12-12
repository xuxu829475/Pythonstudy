# python中的元组 和列表类似，不同之处是元组的 元素不能修改
# 元组的应用场景：
#     1.函数的参数和返回值 ：这样一个函数可以接收任意多个参数，或一次返回多个参数
#     2.格式字符串
#     3.让列表不可被修改 ：保护列表数据安全

# 2.格式字符串 应用
info_tuple = ("小明", 18, 1.75)

print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

f_info_tuple = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(f_info_tuple)

# 3.让列表不可被修改 ：将列表转为元组
num_list = [1, 2, 3, 4, 5, 6]
print(type(num_list))
num_tuple = tuple(num_list)
print(type(num_tuple))
# 元组转为列表
num2_list = list(num_tuple)
print(type(num2_list))
