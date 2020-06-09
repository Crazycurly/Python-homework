import sys,random,time,random
from threading import Thread
from queue import Queue

from Ui_main import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QMessageBox,QPushButton
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.start()

    def gen_btn(self):
        btn_list = []
        for i in range(len(self.pc_card)):
            widget = QPushButton(str(i), self.horizontalLayoutWidget)
            btn_list.append(widget)
            widget.setMinimumSize(QtCore.QSize(40, 40))
            widget.setMaximumSize(QtCore.QSize(40, 40))
            font = QtGui.QFont()
            font.setFamily("微軟正黑體")
            font.setPointSize(12)
            widget.setFont(font)
            widget.setAutoExclusive(False)
            self.horizontalLayout_pc.addWidget(widget)
            widget.clicked.connect(self.draw)
            # widget.setParent(None)
        for i in self.human_card:
            widget = QPushButton(i, self.horizontalLayoutWidget)
            btn_list.append(widget)
            widget.setMinimumSize(QtCore.QSize(40, 40))
            widget.setMaximumSize(QtCore.QSize(40, 40))
            font = QtGui.QFont()
            font.setFamily("微軟正黑體")
            font.setPointSize(12)
            widget.setFont(font)
            widget.setAutoExclusive(False)
            self.horizontalLayout_human.addWidget(widget)
        return btn_list

    def clean_btn(self):
        for i in self.btn_tmp:
            i.setParent(None)

    def draw(self,tmp):
        sender = self.sender()
        tmp = int(sender.text())
        print(tmp)
        self.printf('玩家抽編號 '+str(tmp)+' 的牌')
        self.clean_btn()
        self.human_card.append(self.pc_card[tmp-1])
        del self.pc_card[tmp-1]
        self.human_card, pc_card = self.pair(self.human_card, self.pc_card)
        self.print_card(self.human_card, pc_card)

        if self.chk_end(self.human_card, self.pc_card):
            self.close()

        print('\n輪到電腦抽牌...')
        self.printf('\n輪到電腦抽牌...')
        r = random.randint(0, len(self.human_card)-1)
        self.printf('電腦抽走編號 '+self.human_card[r]+' 的牌')
        self.pc_card.append(self.human_card[r])
        del self.human_card[r]
        self.human_card, self.pc_card = self.pair(self.human_card, self.pc_card)
        self.print_card(self.human_card, self.pc_card)
        self.btn_tmp = self.gen_btn()

        if self.chk_end(self.human_card, self.pc_card):
            self.close()




    def printf(self, mypstr):
        self.textBrowser.append(str(mypstr))

    def start(self):
        self.human_card, self.pc_card = self.gen_card()
        self.print_card(self.human_card, self.pc_card)
        self.printf('整理牌中...')
        self.human_card, self.pc_card = self.pair(self.human_card, self.pc_card)
        self.print_card(self.human_card, self.pc_card)
        self.btn_tmp = self.gen_btn()

    def gen_card(self):
        card = []
        for suit in ['S', 'H', 'D', 'C']:
            for rank in range(1, 14):
                card.append(suit+str(rank))
        card.append('J1')
        card.append('J2')
        random.shuffle(card)
        return(card[:27], card[27:])

    def print_card(self,human_card, pc_card):

        print('玩家的牌:', end=' ')
        tmp = '玩家的牌:\n'
        for i in human_card:
            print(i, end=' ')
            tmp += i +','

        print('\n電腦的牌:', end=' ')
        tmp += '\n電腦的牌:'
        # for i in pc_card:
        #     print(i, end=' ')
        # print('\n')

        for i in range(len(pc_card)):
            print(i+1, end=' ')
            tmp += str(i+1)+','
        print('\n')
        self.printf(tmp)

    def pair(self,human_card, pc_card):
        q = Queue()
        t1 = Thread(target=self.pair_job, args=(human_card, q))
        t2 = Thread(target=self.pair_job, args=(pc_card, q))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return(q.get(), q.get())

    def pair_job(self,card, q):
        dropped_cards = []
        tmp = sorted(card, key=lambda card: card[1:])

        if 'J1' in tmp:
            tmp.remove('J1')
        if 'J2' in tmp:
            tmp.remove('J2')

        for i in range(len(tmp) - 1):
            if tmp[i] and tmp[i][1:] == tmp[i + 1][1:]:
                dropped_cards += [tmp[i], tmp[i + 1]]
                tmp[i] = tmp[i + 1] = None
        # print(dropped_cards)
        card = [card for card in card if card not in dropped_cards]
        q.put(card)

    def chk_end(self,human_card, pc_card):
        if human_card == []:
            print('玩家勝利!!')
            QMessageBox.information(self,"恭喜","玩家勝利!!",QMessageBox.Ok)
            return 1
        elif pc_card == []:
            print('電腦勝利!!')
            QMessageBox.information(self,"恭喜","電腦勝利!!",QMessageBox.Ok)

            return 1
        else:
            return 0


if __name__ == "__main__":

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
