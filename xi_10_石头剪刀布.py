# 导入工具包 随机工具包
import random

# 玩家输入 石头（1）、剪刀（2），布（3）
player = int(input("请出拳 石头（1）、剪刀（2），布（3）："))
# 电脑出拳
computer = random.randint(1, 3)

print("玩家出的是 %d；电脑出的是 %d" % (player, computer))

if ((player == 1 and computer == 2)
    or (player == 2 and computer == 3)
    or (player == 3 and computer == 1)):
    print("我赢了，电脑弱爆了")
elif player == computer:
    print("平局，再来一把")
else:
    print("我输了，不好玩，回家写作业了")
