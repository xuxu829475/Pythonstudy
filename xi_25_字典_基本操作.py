# python中的字典 相当于 java中的map 键值对
# 字典是一个无序的数据集合
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75,
            "weight": 75.5}

print(xiaoming)
# 查
print(xiaoming["name"])
# 增、改
# 这样的操作如果字典里没有是会新增一对键值对，如果K已存在就修改value的值
xiaoming["company"] = "阿里"
print(xiaoming)
xiaoming["company"] = "阿里.蚂蚁"
print(xiaoming)
# 删
# 指定删除
xiaoming.pop("company")
print(xiaoming)

# 清空
xiaoming.clear()
print(xiaoming)
