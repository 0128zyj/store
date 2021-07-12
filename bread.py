from threading import Thread
import time
bread = 0
money = 3000
class Cook(Thread):
    cook = ""
    def run(self) -> None:
        global bread
        while True:
            if bread < 500:
                bread = bread + 1
                print(self.cook,"造了一个面包，还剩",bread,"个面包。")
            else:
                time.sleep(3)
                if bread <= 500:
                    continue
                else:
                    break
class Buy(Thread):
    customer = ""
    def run(self) -> None:
        global money
        global bread
        while True:
            if bread == 0:
                time.sleep(3)
            else:
                money = money - 3
                bread = bread - 1
                print(self.customer, "买了一个面包，还剩", money, "元，",bread,"个面包")
                if money <= 0:
                    break
                else:
                    continue


c1 = Cook()
c2 = Cook()
c3 = Cook()
c1.cook = "厨师1号"
c2.cook = "厨师2号"
c3.cook = "厨师3号"
c1.start()
c2.start()
c3.start()

b1 = Buy()
b2 = Buy()
b3 = Buy()
b4 = Buy()
b5 = Buy()
b1.customer = "顾客1号"
b2.customer = "顾客2号"
b3.customer = "顾客3号"
b4.customer = "顾客4号"
b5.customer = "顾客5号"
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()








