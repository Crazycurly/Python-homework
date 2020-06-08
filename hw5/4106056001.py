import sys
import os

from Ui_main import *
from Ui_order import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow,QMessageBox
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap


price = 0


class MyWindow(QMainWindow, Ui_MainWindow):
    path = os.path.abspath(os.path.dirname(__file__)) + '\img\\'

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setimage()

        self.label_1.clicked.connect(self.one)
        self.label_2.clicked.connect(self.two)
        self.label_3.clicked.connect(self.thr)
        self.label_4.clicked.connect(self.four)
        self.label_5.clicked.connect(self.five)
        self.label_6.clicked.connect(self.six)
        self.btn_order.clicked.connect(self.order)

    def one(self):
        self.orderWindow = OrderWindow(1, self)
        self.orderWindow.show()

    def two(self):
        self.orderWindow = OrderWindow(2,self)
        self.orderWindow.show()

    def thr(self):
        self.orderWindow = OrderWindow(3,self)
        self.orderWindow.show()

    def four(self):
        self.orderWindow = OrderWindow(4,self)
        self.orderWindow.show()

    def five(self):
        self.orderWindow = OrderWindow(5,self)
        self.orderWindow.show()

    def six(self):
        self.orderWindow = OrderWindow(6,self)
        self.orderWindow.show()

    def order(self):
        global price
        QMessageBox.information(self,"結帳","您的消費總金額是"+str(price)+"元",QMessageBox.Ok)
        self.textBrowser.clear()
        price = 0

    def setimage(self):
        self.label_menu.setPixmap(QPixmap(self.path+'menu.png'))
        self.label_menu.setScaledContents(True)
        self.label_1.setPixmap(QPixmap(self.path+"1.png"))
        self.label_1.setScaledContents(True)
        self.label_2.setPixmap(QPixmap(self.path+"2.png"))
        self.label_2.setScaledContents(True)
        self.label_3.setPixmap(QPixmap(self.path+"3.png"))
        self.label_3.setScaledContents(True)
        self.label_4.setPixmap(QPixmap(self.path+"4.png"))
        self.label_4.setScaledContents(True)
        self.label_5.setPixmap(QPixmap(self.path+"5.png"))
        self.label_5.setScaledContents(True)
        self.label_6.setPixmap(QPixmap(self.path+"6.png"))
        self.label_6.setScaledContents(True)
        self.label_order.setPixmap(QPixmap(self.path+"my_order.png"))
        self.label_order.setScaledContents(True)

    def printf(self, mypstr):
        self.textBrowser.append(mypstr)
        


class OrderWindow(QMainWindow, Ui_OrderWindow):
    path = os.path.abspath(os.path.dirname(__file__)) + '\img\\'

    num = 1
    chk_size = 0
    drink = ['熟成紅茶', '麗春紅茶', '太妃紅茶', '春梅冰茶', '冷露歐蕾', '熟成歐蕾']
    price = [30, 30, 35, 40, 45, 45]

    def __init__(self, index, parent=None):
        super(OrderWindow, self).__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.setimage()
        self.lcdNumber.display(self.num)
        self.index = index

        self.btn_addTo.clicked.connect(self.addTo)
        self.btn_add.clicked.connect(self.add)
        self.btn_sub.clicked.connect(self.sub)

        self.btn_mid.clicked.connect(self.size)
        self.btn_large.clicked.connect(self.size)

        self.comboBox_temp.addItems(['', '常溫', '正常冰', '少冰', '微冰', '去冰'])
        self.comboBox_sweet.addItems(['', '正常糖', '少糖', '半糖', '微糖', '無糖'])

    def setimage(self):
        self.label_size.setPixmap(QPixmap(self.path+'size.png'))
        self.label_size.setScaledContents(True)
        self.label_temp.setPixmap(QPixmap(self.path+'temp.png'))
        self.label_temp.setScaledContents(True)
        self.label_sweet.setPixmap(QPixmap(self.path+'sweet.png'))
        self.label_sweet.setScaledContents(True)

    def size(self):
        sender = self.sender()
        if sender == self.btn_mid:
            self.size = '中'
        else:
            self.size = '大'
        self.chk_size = 1

    def add(self):
        self.num = self.num + 1
        self.lcdNumber.display(self.num)

    def sub(self):
        if self.num > 1:
            self.num = self.num - 1
        self.lcdNumber.display(self.num)

    def addTo(self):
        if self.chk_size == 1 and self.comboBox_temp.currentText() != '' and self.comboBox_sweet.currentText() != '':
            if self.size == '大':
                p = (self.price[self.index-1] + 10)*self.num
            else:
                p = self.price[self.index-1]*self.num
            
            global price
            price += p
            self.parent.printf(self.drink[self.index-1]+" "+self.size+" "+self.comboBox_temp.currentText(
            )+" " + self.comboBox_sweet.currentText()+" "+str(self.num)+"份 $"+str(p))
            self.close()
        else:
            QMessageBox.information(self,"警告","未選擇",QMessageBox.Ok)

        print("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
