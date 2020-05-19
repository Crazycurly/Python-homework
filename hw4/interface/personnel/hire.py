from ..situation import personnel
from ..situation import money

def hire():
    print("\n新增欲聘任的人事資訊\n")
    name = input("姓名：")
    emp_id = input("員工id：")
    payment = int(input("薪資："))
    state = input("狀態：")

    #check id format
    if len(emp_id) != 4:
        print("聘任失敗，此 ID 不符合格式(4位數)")
        return

    #check state
    if state == '在職':
        #check money enough
        if payment < money.get_money():
            if personnel.hire(name,emp_id,payment,state):
                money.spend_money(payment)
            return
        else:
            print("聘任失敗，資金不足，剩餘：", money.get_money())
            return
    else:
        personnel.hire(name,emp_id,payment,state)
        return
    return
