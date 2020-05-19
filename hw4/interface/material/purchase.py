from ..situation import material
from ..situation import money

def add_product():
    print("\n新增欲進貨的商品資訊\n")
    name = input("商品名稱：")
    price = int(input("商品單價："))
    quantity = int(input("商品數量："))

    #check money enough
    if price*quantity < money.get_money():
        material.addProduct(name, price, quantity)
        money.spend_money(price*quantity)
        print("購買成功!!")
    else:
        print("購買失敗，資金不足，剩餘：", money.get_money())
