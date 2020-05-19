from ..situation import personnel


def confirmEmp():
    print("<<確認是否是本店員工>>")
    employeeID = input("請輸入員工 ID：")

    #check id existing
    tmp = personnel.find_sameId(employeeID)
    if type(tmp) != bool:
        if tmp.state == '在職':
            print("員工姓名: "+tmp.name+"  員工ID: "+tmp.emp_id)
            print("員工確認成功")
            return True
        else:
            print("此員工已離職")
            return False
    else:
        print("查無此員工ID")
        return False
    return False
