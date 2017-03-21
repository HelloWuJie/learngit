import random
secret = random.randint(1,10)
number = secret
count = 0
while count < 5:
    count=count + 1
    rest = 5 - count
    tmp = int(input('猜一猜我心中的数字：'))
    if tmp > number:
        print('太大了!')
        print('您还有%d次机会\n'%rest)
    elif tmp < number:
        print('太小了!')
        print('您还有%d次机会\n'%rest)
    else:
        print('恭喜你，答对了!\n')
        break

print ('游戏结束，谢谢参与！\n')
