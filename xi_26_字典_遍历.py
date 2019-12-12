# python中的字典 相当于 java中的map 键值对
xiao_ming = {"name": "小明",
             "age": 18,
             "gender": True,
             "height": 1.75,
             "weight": 75.5}

for k in xiao_ming:
    print(k)
    print(xiao_ming[k])

xiao_hong = {"name": "小红",
             "age": 17,
             "gender": False,
             "height": 1.60,
             "weight": 50}

# 列表和字典组合使用的场景
card_list = [xiao_ming, xiao_hong]
for card in card_list:
    print(card)
    for k in card:
        print(card[k])
