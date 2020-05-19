from ..situation import material
from ..situation import money

def sale():
    print("<<新增欲銷售的商品資訊>>")
    name = input("商品名稱：")
    price = int(input("商品售價："))
    quantity = int(input("商品數量："))

    if(material.sale_Product(name,price,quantity)):
        money.spend_money(price*quantity)
