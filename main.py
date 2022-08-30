import json
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import pyperclip
import os

class App(QDialog):
    # ==== 在此配置 ====
    fontsize = 24
    dbfile = 'db.json'

    data = []
    btnList = []

    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        self.loadDB()

        self.title = '简历复制粘贴小助手'
        self.left = 10
        self.top = 10
        self.width = 360
        self.height = 480
        self.initUI()

        self.print()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.show()

    def print(self):

        area = QScrollArea()
        area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        area.setWidgetResizable(False)

        content_widget = QWidget()
        arealayout = QVBoxLayout(content_widget)
        area.setLayout(arealayout)

        layout = QVBoxLayout()
        layout.addWidget(area)
        self.setLayout(layout)

        btn1 = QPushButton('打开配置文件, 默认在项目根下, db.json')
        btn1.clicked.connect(lambda: self.openDBfile())
        arealayout.addWidget(btn1)

        self.btnList = []
        for i in self.data:
            btn1 = QPushButton(i)
            btn1.setStyleSheet(f"QPushButton{{font-size:{self.fontsize}px; padding:5px;max-width:300px;min-height:30px;}}")
            btn1.clicked.connect(self.copytoclipboard(i))
            arealayout.addWidget(btn1)

    def copytoclipboard(self, text):
        def temp():
            pyperclip.copy(text)
            print(text)

        return temp

    def loadDB(self):
        with open(self.dbfile) as f:
            # print(f)
            db = json.load(f)
            self.data = db['data']
            # print(db)

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)

    def openDBfile(self):
        os.system('open ' + self.dbfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
