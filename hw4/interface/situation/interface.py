from . import material, personnel, money


def interface():
    while True:
        code = input("進入店面情況查尋系統，請輸入操作指令:")
        if code == "1":
            for i in material.get_Material():
                print(i)
                print()
        elif code == "2":
            for i in personnel.get_Personnel():
                print(i)
                print()
        elif code == "3":
            print(money.get_money())
        elif code == "4":
            print("離開店面情況查尋系統!!")
            break
        else:
            print("錯誤的代號！")
