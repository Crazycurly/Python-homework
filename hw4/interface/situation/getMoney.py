class Money:
    def __init__(self):
        self._money = 100000

    def get_money(self):
        return self._money

    def spend_money(self, num):
        self._money -= num

    def earn_money(self, num):
        self._money += num