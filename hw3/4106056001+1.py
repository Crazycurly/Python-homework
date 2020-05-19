class ShoppingCar():
    car = []

    def __init__(self, name):
        self.name = name

    def printCar(self):
        print(self.car)

    def getOwner(self):
        return self.name

    def addProduct(self, name, price, quantity):
        tmp = item(name, price, quantity)
        if self.find_same(tmp):
            self.car[self.car.index(tmp)].quantity += tmp.quantity
        else:
            self.car.append(tmp)

    def find_same(self, item):
        if item in self.car:
            return True
        return False

    def getProduct(self):
        return self.car

    def getDiscount(self):
        dis = [i for i in self.car if i.discount()]
        return dis

    def getCost(self):
        return sum([i.get_price() for i in self.car])

    def removeProduct(self, name, price,quantity):
        tmp = item(name, price, 1)
        if self.find_same(tmp):
            if self.car[self.car.index(tmp)].quantity <= quantity:
                del self.car[self.car.index(tmp)]
            else:
                self.car[self.car.index(tmp)].quantity -= quantity
        else:
            print("無效的刪除")


class item():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def discount(self):
        return self.quantity >= 2

    def get_price(self):
        if self.discount():
            return self.quantity*self.price - (self.quantity/2)*(self.price*0.2)
        else:
            return self.price

obj1 = ShoppingCar("小丸子")
obj1.addProduct("巧克力", 50, 2)
obj1.addProduct("咖啡豆", 120, 3)
obj1.addProduct("草莓果醬", 70, 5)
obj1.addProduct("馬卡龍", 30, 1)
obj1.removeProduct("草莓果醬", 70,2)
obj1.addProduct("馬卡龍", 30, 2)
obj1.removeProduct("咖啡豆", 120,2)
obj1.addProduct("馬卡龍", 40, 2)
obj1.addProduct("咖啡豆", 10, 3)



print(obj1.getOwner(), "的購物車裡面有", obj1.getProduct(), "總共",
      obj1.getCost(), "元 其中", obj1.getDiscount(), "享有第二件打八折的優惠")
