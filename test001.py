import random

# 生成一个随机数字
number = random.randint(1, 100)

# 玩家最多有5次猜数字的机会
for i in range(5):
    guess = int(input("请输入一个数字（1-100）: "))

    if guess == number:
        print("恭喜你，猜对了！")
        break
    elif guess < number:
        print("你猜的数字小了。")
    else:
        print("你猜的数字大了。")
else:
    print("抱歉，次数用完。正确答案是:", number)