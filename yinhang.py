import random
# 准备数据
bank = {} # 空的数据库
bank_name = "中国工商银行昌平回龙观支行"

def bank_addUser(account,username,identity,password,country,province,street,door):
    # 是否已满
    if len(bank) > 100:
        return 3
    # 是否存在
    if username in bank:
        return 2
    # 正常开户
    bank[identity] = {
        "username":username,
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1

# 用户的开户操作
def addUser():
    identity = input("请输入身份证号：")
    username = input("请输入用户名：")
    password = input("请输入密码：")
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    # 10000000~99999999
    account = random.randint(10000000,99999999)
    status = bank_addUser(account,identity,username,password,country,province,street,door)
    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理!")
    elif status == 2:
        print("对不起，该用户已开户，请不要重复开户！别瞎弄！")
    elif status == 1:
        print("恭喜正常开户！以下是您的个人信息：")
        info = '''
            ------------个人信息------------
            身份证号：%s
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (identity,username,account,country,province,street,door,bank[username]["money"],bank_name))
# 银行存钱
def bank_save(money):
    for i in bank.keys():
        bank[i]["money"] += money
        print(bank[i]["money"])
        return True
    return False
# 用户取钱
def Withdraw():
    global addUser
    for i in bank.keys():
        get_account = input("请输入银行卡号:")
        print("你输入的卡号：", get_account)
        get_password = input("请输入密码:")

        get_account = int(bank[i]["account"])

        if get_account == get_account and get_password == bank[i]["password"]:

            gets_money = int(input("请输入你的取款金额"))
            print(gets_money)

            if gets_money > bank[i]["money"]:
                print("卡内余额不足！无法取出")
            elif gets_money <= bank[i]["money"]:
                bank[i]["money"]  = bank[i]["money"]- gets_money
                print("取款成功","目前余额{}".format(bank[i]["money"]))
            else:
                print("输入非法！请正确输入！")

        elif get_account != get_account and get_password == bank[i]["password"]:
            print("用户输入错误！")
        elif get_account == get_account and get_password != bank[i]["password"]:
            print("用户密码输入错误！")

        else:
            print("该用户不存在")
# 用户存钱
def save():
    money = int(input("请输入您要存的金额："))
    bank_save(money)
# 查询
def find():
    global addUser
    for i in bank.keys():
        get_account = input("请输入银行卡号:")
        print("你输入的卡号：",get_account)
        get_password = input("请输入密码:")

        get_account = int(bank[i]["account"])
        if get_account == get_account and get_password == bank[i]["password"]:

            print("登录成功！,下面显示该用户信息：")
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        银行卡号：%s
                        密码：%s
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            print(info % (i,bank[i]["account"],bank[i]["password"],bank[i]["country"], bank[i]["province"], bank[i]["street"], bank[i]["door"], bank[i]["money"], bank_name))

        elif get_account !=  get_account  and get_password == bank[i]["password"]:
            print("用户输入错误！")
        elif get_account ==  get_account and get_password != bank[i]["password"]:
            print("用户密码输入错误！")
        else:
            print("该用户不存在")
def welcome():
    print("----------------------------------------")
    print("-        中国工商银行账户管理系统V1.0     -")
    print("----------------------------------------")
    print("- 1.开户                               -")
    print("- 2.取钱                               -")
    print("- 3.存钱                               -")
    print("- 4.转账                               -")
    print("- 5.查询                               -")
    print("- 6.Bye!                               -")
    print("-------------------------------------- -")
# 入口程序
while True:
    welcome()
    # 输入用户的业务逻辑
    chose = input("亲输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        Withdraw()
    elif chose == "3":
        save()
    elif chose == "4":
        pass
    elif chose == "5":
        find()
    elif chose == "6":
        break
    else:
        print("输入非法，别瞎弄！重新输入!")