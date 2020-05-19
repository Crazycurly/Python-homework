from . import purchase

def interface():
    while(1):
        code = input("歡迎進入材料系統，請輸入操作指令:")

        if code == "1":
            purchase.add_product()
        elif code == "2":
            print("離開材料系統\n")
            break
        else:
            print("錯誤的代號！")
