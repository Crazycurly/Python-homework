from .import confirmEmp,sales

def interface():
    while(1):
        code = input("歡迎進入銷售系統，請輸入操作指令:")

        if code == "1":
            if confirmEmp.confirmEmp():
                sales.sale()
        elif code == "2":
            print("離開銷售系統\n")
            break
        else:
            print("錯誤的代號！")