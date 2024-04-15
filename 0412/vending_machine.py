class VendingMachine:
    def __init__(self):
        self.beverage = beverage

    def buy(self):
        pay 한 다음
        음료를 구매한다.

    def pay(self):
        돈을 입력받는다.

class Beverage:
    def __init__(self, name, price, stock):
        self.price = price
        self.stock = stock
        self.name = name

cider = Beverage()
cola = Beverage()
water = Beverage()

machine = VendingMachine(cider, cola, water)


machine.buy()