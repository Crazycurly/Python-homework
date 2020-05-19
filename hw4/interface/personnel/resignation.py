
from ..situation import personnel

def resignation():
    emp_id = input("輸入離職者的id：")

    if len(emp_id) != 4:
        print("離職失敗，此 ID 不符合格式(4位數)")
    else:
        personnel.resignation(emp_id)
    return
