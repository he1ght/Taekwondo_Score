# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default_score.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        AssertMsg = QtWidgets.QMessageBox.question(self, '버튼 조작', '좌 - 청 1점 증가\n우 - 홍 1점 증가\n상 - 리셋\n하 - 직전 행동 되돌리기', QtWidgets.QMessageBox.Yes)

        self.blue_score = 0
        self.red_score = 0
        self.stack = []
        self.MaxHistory = 16

        self.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        print(self.rect())
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        font = QtGui.QFont()
        font.setPointSize(200)
        font.setBold(True)

        self.Chung = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Chung.setFont(font)
        self.Chung.setAlignment(QtCore.Qt.AlignCenter)
        self.Chung.setObjectName("Chung")
        self.Chung.setStyleSheet("""QLabel { background-color: blue; color: white }""")
        self.Chung.setText(str(self.blue_score))
        self.horizontalLayout.addWidget(self.Chung)

        self.Hong = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Hong.setFont(font)
        self.Hong.setAlignment(QtCore.Qt.AlignCenter)
        self.Hong.setTextFormat(QtCore.Qt.AutoText)
        self.Hong.setObjectName("Hong")
        self.Hong.setStyleSheet("""QLabel { background-color: red; color: white }""")
        self.Hong.setText(str(self.red_score))
        self.horizontalLayout.addWidget(self.Hong)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "태권도 점수판"))

    def closeEvent(self, event):
        quit_msg = "정말 종료하시겠습니까?"
        reply = QtWidgets.QMessageBox.question(self, '종료 메세지', quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        print(self.stack)
        currentKey = event.key()
        if currentKey == QtCore.Qt.Key_Escape:
            self.close()
        elif currentKey == QtCore.Qt.Key_Left:
            # 청
            self.blue_score+=1
            self.Chung.setText(str(self.blue_score))
            self.stack.append(currentKey)
            if self.stack.__len__() == self.MaxHistory:
                print(self.stack.pop(0))
        elif currentKey == QtCore.Qt.Key_Right:
            # 홍
            self.red_score+=1
            self.Hong.setText(str(self.red_score))
            self.stack.append(currentKey)
            if self.stack.__len__() == self.MaxHistory:
                print(self.stack.pop(0))
        elif currentKey == QtCore.Qt.Key_Up or currentKey == QtCore.Qt.Key_Return:
            # 리셋
            self.blue_score=0
            self.Chung.setText(str(self.blue_score))
            self.red_score=0
            self.Hong.setText(str(self.red_score))
            self.stack = []
        elif currentKey == QtCore.Qt.Key_Down or currentKey == QtCore.Qt.Key_Tab:
            # undo
            if not self.stack:
                pass
            else:
                before = self.stack.pop()
                if before == QtCore.Qt.Key_Left:
                    # 청
                    self.blue_score -= 1
                    self.Chung.setText(str(self.blue_score))
                elif before == QtCore.Qt.Key_Right:
                    # 홍
                    self.red_score -= 1
                    self.Hong.setText(str(self.red_score))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window=Ui_MainWindow()
    window.setWindowIcon(QtGui.QIcon("logo.png"))
    #window.showMaximized()
    window.showFullScreen()
    app.exec_()

