'''
    Jason的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10辣条优惠券（0.3），20机械革命优惠券（0.9）。
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''
import random
# 1.商品
shop = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["辣条",2.5],
    ["老干妈",13],
    ["水杯",30],
    ["拍立得",1000]
]

# 2.初始化您的余额
money = input("请输入您的钱包余额:")
money = int(money)
reb = 0
num = 0

while True :
    if money <= 0 :
        print("请输入大于0的金额！")
        money = input("请输入您的钱包余额:")
        money = int(money)
    else :
        # 2.1抽奖
        rebate = random.randint(0, 29)
        if rebate <= 9:
            reb = 1.75
            print("恭喜！抽中辣条优惠券（0.3）")
        else:
            reb = 1500
            print("恭喜！抽中机械革命优惠券（0.9）")

        break

# 3.准备一个空的购物车
mycart = []

# 买东西

while True :
    # 展示商品
    for index,value in enumerate(shop): # 枚举，将角标和商品整体都打印
        print(index,"  ",value)

    # 请输入您要的商品
    print("余额：",money)
    chose = input("请输入您要的商品：")

    # 看是否存在
    if chose.isdigit():  # 是否能被看成数字：
        chose = int(chose)
        # 看商品是否存在
        if chose > len(shop) - 1:
            print("您要的商品不存在！")
        else:
            if chose == 0 :
                money = money + reb
                # 看钱是否足够
                if money > shop[chose][1] :
                        mycart.append(shop[chose])
                        # 钱减去
                        money = money - shop[chose][1]
                        print("恭喜，成功添加购物车，您的余额还剩：￥",money)
                        num = num + 13500
                        break
                else:
                    money = money - reb
                    print("对不起，穷鬼，余额不足，请到商城购买其他商品！")
            else :
                if chose == 4 :
                    money = money + reb
                    if money > shop[chose][1] :
                            mycart.append(shop[chose])
                            # 钱减去
                            money = money - shop[chose][1]
                            print("恭喜，成功添加购物车，您的余额还剩：￥",money)
                            num = num + 1.75
                            break
                    else:
                        money = money - reb
                        print("对不起，穷鬼，余额不足，请到商城购买其他商品！")
                else:
                    if money > shop[chose][1] :
                            mycart.append(shop[chose])
                            # 钱减去
                            money = money - shop[chose][1]
                            print("恭喜，成功添加购物车，您的余额还剩：￥",money)
                            break
                    else:
                        print("对不起，穷鬼，余额不足，请到商城购买其他商品！")

    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您的输入商品不存在！别瞎弄!")


while True:
    # 展示商品
    for index,value in enumerate(shop): # 枚举，将角标和商品整体都打印
        print(index,"  ",value)

    # 请输入您要的商品
    print("余额：",money)
    chose = input("请输入您要的商品：")

    # 看是否存在
    if chose.isdigit():  # 是否能被看成数字：
        chose = int(chose)
        # 看商品是否存在
        if chose > len(shop) - 1:
            print("您要的商品不存在！")
        else:
            # 看钱是否足够
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                # 钱减去
                money = money - shop[chose][1]
                print("恭喜，成功添加购物车，您的余额还剩：￥",money)
            else:
                print("对不起，穷鬼，余额不足，请到商城购买其他商品！")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您的输入商品不存在！别瞎弄!")

# 打印小票
print("下面是您的购物小条，请拿好：")
for  index,value in enumerate(mycart):
    print(index,"\t",value)
if num == 1.75:
    print("\n",index,"\t","[辣条优惠券,-",num,"]")
elif num == 13500:
    print("\n",index,"\t","['机械革命优惠券',-",num,"]")
print("您的钱包还剩：￥",money)

