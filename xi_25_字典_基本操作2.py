# python中的字典 相当于 java中的map 键值对
xiao_ming = {"name": "小明",
             "age": 18,
             "gender": True,
             "height": 1.75,
             "weight": 75.5}

# 统计数量
print(len(xiao_ming))
# 合并字典
# update 合并字典时被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
tmp_xiao_ming = {"company": "腾讯",
                 "age": 25}
xiao_ming.update(tmp_xiao_ming)
print(xiao_ming)
# 清空
xiao_ming.clear()
print(xiao_ming)
