class Bungeoppang:
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total = 0

    def sell(self):
        print(f"{self.contents} 붕어빵을 {self.price}원에 판매했습니다.")
        self.total += self.price
        self.display_total()

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹었습니다.")

    def display_total(self):
        print(f"총 판매금: {self.total}원")

Bungeo1 = Bungeoppang("슈크림", 2000)
Bungeo2 = Bungeoppang("팥", 1000)
Bungeo3 = Bungeoppang("김치", 1500)

Bungeo3.sell()
Bungeo3.sell()
Bungeo1.eat()
Bungeo2.eat()
Bungeo3.eat()
Bungeo3.sell()
Bungeo1.sell()
Bungeo1.sell()
Bungeo2.sell()
Bungeo3.sell()
Bungeo2.sell()
