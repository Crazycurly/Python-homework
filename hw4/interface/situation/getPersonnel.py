class Personnel_data():
    data = []

    class Personnel():
        def __init__(self, name, emp_id, payment, state):
            self.name = name
            self.emp_id = emp_id
            self.payment = payment
            self.state = state

        def __eq__(self, other):
            return self.emp_id == other.emp_id

        def __str__(self):
            return "姓名: "+str(self.name)+"\n員工ID: "+str(self.emp_id)+"\n薪資: "+str(self.payment)+"\n狀態: "+str(self.state)

        def __repr__(self):
            return str(self)

    def get_Personnel(self):
        return self.data

    def hire(self, name, emp_id, payment, state):
        tmp = self.Personnel(name, emp_id, payment, state)
        if self.find_same(tmp):
            print("聘任失敗，此員工 ID 已存在")
            return False
        else:
            self.data.append(tmp)
            print("聘任成功!!")
            return True

    def resignation(self, emp_id):
        tmp = self.Personnel('name', emp_id, 1, '')

        if self.find_same(tmp):
            if self.data[self.data.index(tmp)].state == '在職':
                self.data[self.data.index(tmp)].state = '離職'
                print('離職成功')
            else:
                print('離職失敗，此員工已離職')
        else:
            print("離職失敗，找不到此員工ID")

    def find_same(self, item):
        if item in self.data:
            return True
        return False

    def find_sameId(self, emp_id):
        tmp = self.Personnel('name', emp_id, 1, '')
        if self.find_same(tmp):
            return self.data[self.data.index(tmp)]
        else:
            return False
