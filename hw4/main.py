from interface.material import interface as mat
from interface.personnel import interface as per
from interface.sales import interface as sal
from interface.situation import interface as sit


while True:
    code = input("歡迎來到商店管理系統，請輸入系統代號：")

    if code == "1":
        mat.interface()
    elif code == "2":
        per.interface()
    elif code == "3":
        sal.interface()
    elif code == "4":
        sit.interface()
    elif code == "5":
        print("結束商店管理系統的測試！")
        break
    else:
        print("錯誤的代號！")