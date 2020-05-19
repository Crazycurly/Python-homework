class Material_data():
    data = []

    class Material():
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def __eq__(self, other):
            return self.name == other.name

        def __str__(self):
            return "商品名稱: "+str(self.name)+"\n商品價格: "+str(self.price)+"\n商品數量: "+str(self.quantity)

        def __repr__(self):
            return str(self)

    def get_Material(self):
        return self.data

    def addProduct(self, name, price, quantity):
        tmp = self.Material(name, price, quantity)
        #check if existing quantity increase else append
        if self.find_same(tmp):
            self.data[self.data.index(tmp)].quantity += tmp.quantity
        else:
            self.data.append(tmp)

    def sale_Product(self, name, price, quantity):
        tmp = self.Material(name, price, 1)
        if self.find_same(tmp):
            if self.data[self.data.index(tmp)].quantity < quantity:
                print("銷售失敗，商品數量不足，剩餘:",
                      self.data[self.data.index(tmp)].quantity)
                return False
            else:
                self.data[self.data.index(tmp)].quantity -= quantity
                print("銷售成功，剩餘:", self.data[self.data.index(tmp)].quantity)
                return True
        else:
            print("銷售失敗，找不到商品")
            return False

    def find_same(self, item):
        if item in self.data:
            return True
        return False
