from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
import sys
import random as r


class Numbers_15(QWidget):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.setWindowTitle('15 PUZZLE GAME')
        self.setFixedSize(500, 550)
        self.setStyleSheet("color: #fff;background-image:url('2.jpg');border-radius: 16px;margin:5px;font: 45pt Agency FB;")

        self.numbers = [['1', '2', '3', '4'],
                        ['5', '6', '7', '8'],
                        ['9', '10', '11', '12'],
                        ['13', '14', '15', '']]
        self.answers = [['1', '2', '3', '4'],
                        ['5', '6', '7', '8'],
                        ['9', '10', '11', '12'],
                        ['13', '14', '15', '']]
        self.img = QLabel(self)
        self.img.setGeometry(-10, -10, 600, 600)
        self.img.setPixmap(QPixmap('1.jpg'))
        self.img.setScaledContents(True)
        self.emp_stl = "background-image:url('1.jpg');box-shadow: rgba(0, 0, 0, 0.17) 0px -23px 25px 0px inset, rgba(0, 0, 0, 0.15) 0px -36px 30px 0px inset, rgba(0, 0, 0, 0.1) 0px -79px 40px 0px inset, rgba(0, 0, 0, 0.06) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;"

        self.border = QLabel(self)
        self.border.setGeometry(0, 0, 500, 460)
        self.border.setStyleSheet(f"{self.emp_stl}; border:3px solid black;")
        self.border1 = QLabel(self)
        self.border1.setGeometry(0, 457, 500, 97)
        self.border1.setStyleSheet(f"{self.emp_stl}; border:3px dashed black;")
        self.Btn_1 = QPushButton("1", self)
        self.Btn_2 = QPushButton("2", self)
        self.Btn_3 = QPushButton("3", self)
        self.Btn_4 = QPushButton("4", self)
        self.Btn_5 = QPushButton("5", self)
        self.Btn_6 = QPushButton("6", self)
        self.Btn_7 = QPushButton("7", self)
        self.Btn_8 = QPushButton("8", self)
        self.Btn_9 = QPushButton("9", self)
        self.Btn_10 = QPushButton("10", self)
        self.Btn_11 = QPushButton("11", self)
        self.Btn_12 = QPushButton("12", self)
        self.Btn_13 = QPushButton("13", self)
        self.Btn_14 = QPushButton("14", self)
        self.Btn_15 = QPushButton("15", self)
        self.Btn_16 = QPushButton("", self)
        self.restart = QPushButton("RESET 🔁", self)
        self.move = QPushButton("MOVE", self)


        self.Btn_1.setGeometry(10, 10, 121, 111)
        self.Btn_2.setGeometry(130, 10, 121, 111)
        self.Btn_3.setGeometry(250, 10, 121, 111)
        self.Btn_4.setGeometry(370, 10, 121, 111)
        self.Btn_5.setGeometry(10, 120, 121, 111)
        self.Btn_6.setGeometry(130, 120, 121, 111)
        self.Btn_7.setGeometry(250, 120, 121, 111)
        self.Btn_8.setGeometry(370, 120, 121, 111)
        self.Btn_9.setGeometry(10, 230, 121, 111)
        self.Btn_10.setGeometry(130, 230, 121, 111)
        self.Btn_11.setGeometry(250, 230, 121, 111)
        self.Btn_12.setGeometry(370, 230, 121, 111)
        self.Btn_13.setGeometry(10, 340, 121, 111)
        self.Btn_14.setGeometry(130, 340, 121, 111)
        self.Btn_15.setGeometry(250, 340, 121, 111)
        self.Btn_16.setGeometry(370, 340, 121, 111)
        self.restart.setGeometry(10, 465, 242, 80)
        self.move.setGeometry(250, 465, 242, 80)

# ============================================================================
        self.Btn_1.clicked.connect(lambda: self.play(self.Btn_1))
        self.Btn_2.clicked.connect(lambda: self.play(self.Btn_2))
        self.Btn_3.clicked.connect(lambda: self.play(self.Btn_3))
        self.Btn_4.clicked.connect(lambda: self.play(self.Btn_4))
        self.Btn_5.clicked.connect(lambda: self.play(self.Btn_5))
        self.Btn_6.clicked.connect(lambda: self.play(self.Btn_6))
        self.Btn_7.clicked.connect(lambda: self.play(self.Btn_7))
        self.Btn_8.clicked.connect(lambda: self.play(self.Btn_8))
        self.Btn_9.clicked.connect(lambda: self.play(self.Btn_9))
        self.Btn_10.clicked.connect(lambda: self.play(self.Btn_10))
        self.Btn_11.clicked.connect(lambda: self.play(self.Btn_11))
        self.Btn_12.clicked.connect(lambda: self.play(self.Btn_12))
        self.Btn_13.clicked.connect(lambda: self.play(self.Btn_13))
        self.Btn_14.clicked.connect(lambda: self.play(self.Btn_14))
        self.Btn_15.clicked.connect(lambda: self.play(self.Btn_15))
        self.Btn_16.clicked.connect(lambda: self.play(self.Btn_16))
        self.restart.clicked.connect(self.shuffle_board)

        self.btns = [[self.Btn_1, self.Btn_2, self.Btn_3, self.Btn_4],
                     [self.Btn_5, self.Btn_6, self.Btn_7, self.Btn_8],
                     [self.Btn_9, self.Btn_10, self.Btn_11, self.Btn_12],
                     [self.Btn_13, self.Btn_14, self.Btn_15, self.Btn_16]]
        self.restart.setStyleSheet("background-image:url('2.jpg');color: white;border:3px solid black;font: 30pt Agency FB;")
        self.move.setStyleSheet("background-image:url('2.jpg');color: white;border:3px solid black;font: 30pt Agency FB;")
        self.shuffle_board()
        self.check_win()

    def play(self, cl_btn):
        self.check_empty()
        i, j = 0, 0
        if cl_btn.text() != '':
            for a in range(len(self.btns)):
                for b in range(len(self.btns)):
                    if cl_btn == self.btns[a][b]:
                        i, j = a, b
                        break
            if i - 1 >= 0 and self.btns[i-1][j].text() == '':
                self.btns[i-1][j].setText(cl_btn.text())
                self.btns[i-1][j].setStyleSheet('')
                cl_btn.setText('')
                self.moves += 1
            elif j - 1 >= 0 and self.btns[i][j-1].text() == '':
                self.btns[i][j-1].setText(cl_btn.text())
                self.btns[i][j-1].setStyleSheet('')
                cl_btn.setText('')
                self.moves += 1
            elif i + 1 <= 3 and self.btns[i+1][j].text() == '':
                self.btns[i+1][j].setText(cl_btn.text())
                self.btns[i+1][j].setStyleSheet('')
                cl_btn.setText('')
                self.moves += 1
            elif j + 1 <= 3 and self.btns[i][j+1].text() == '':
                self.btns[i][j+1].setText(cl_btn.text())
                self.btns[i][j+1].setStyleSheet('')
                cl_btn.setText('')
                self.moves += 1
        self.move.setText(f"MOVE :  {self.moves}")
        self.check_win()

    def check_empty(self):
        for i in self.btns:
            for j in i:
                if j.text() == '':
                    j.setStyleSheet(self.emp_stl)

    def shuffle_board(self):
        self.moves = 0
        self.move.setText(f"MOVE :  {self.moves}")
        self.check_empty()
        r.shuffle(self.numbers)
        for i in range(len(self.btns)):
            r.shuffle(self.numbers[i])
            for j in range(len(self.btns)):
                self.btns[i][j].setText(self.numbers[i][j])
                if self.btns[i][j].text() == '':
                    self.btns[i][j].setStyleSheet(self.emp_stl)
                else:
                    self.btns[i][j].setStyleSheet('')
        self.check_empty()

    def check_win(self):
        a = 0
        for i in range(len(self.answers)):
            for j in range(len(self.answers)):
                if self.answers[i][j] == self.btns[i][j].text():
                    a += 1
        if a == 16:
            msg = QMessageBox(self)
            msg.setWindowTitle('YOU WON !!!')
            msg.setGeometry(500, 200, 100, 100)
            msg.setStyleSheet("background-image: url('1.jpg');")
            msg.setText("<h5>SIZ YUTDINGIZ !!! <br>YANA O'YNAYSIZMI ?</h5>")
            msg.show()
            self.shuffle_board()
        self.check_empty()



app = QApplication(sys.argv)
window = Numbers_15()
window.show()
sys.exit(app.exec_())

