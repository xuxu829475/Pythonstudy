# python中的列表相当于java中的数组

# 统计
name_list = ["张三", "王五", "张三", "李四"]
# len 查看列表的差多
print(len(name_list))

# count 统计列表中某个元素出现的次数
count = name_list.count("张三")
print(count)

# remove 在列表中有两个相同的元素是 remove默认删除第一个
name_list.remove("张三")
print(name_list)

# 排序
num_list = [1, 5, 2, 3, 6]
# 升序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)
# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)

# 逆序/翻转
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)


