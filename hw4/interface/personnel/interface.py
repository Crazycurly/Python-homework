from .import hire,resignation

def interface():
    while(1):
        code = input("歡迎進入人事系統，請輸入操作指令:")

        if code == "1":
            hire.hire()
        elif code == "2":
            resignation.resignation()
        elif code == "3":
            print("離開人事系統\n")
            break
        else:
            print("錯誤的代號！")