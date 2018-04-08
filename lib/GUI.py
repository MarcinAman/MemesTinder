from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from collections import namedtuple

import sys
memeList = []

Meme = namedtuple("Meme", "Name pic")

m = Meme("Name", "test.jpg")
m2 = Meme("Name2", "test2.jpg")
memeList.append(m)
memeList.append(m2)




class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.setWindowTitle("Meme Tinder")

        wid = QWidget()
        layout = QVBoxLayout()
        iterator = 0

        label = QLabel(memeList[iterator][0])
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(25)
        layout.addWidget(label)

        pic = QLabel()
        pic.setPixmap(QPixmap("../pics/" + memeList[iterator][1]))
        pic.setAlignment(Qt.AlignCenter)
        layout.addWidget(pic)

        wid2 = QWidget()
        layout2 = QHBoxLayout()

        like = QPushButton("like")
        # like.clicked.connect(likeFunction())
        layout2.addWidget(like)

        dislike = QPushButton("dislike")
        # like.clicked.connect(dislikeFunction())
        layout2.addWidget(dislike)

        next = QPushButton("next")
        next.clicked.connect(lambda: nextF(pic, label, iterator))
        layout2.addWidget(next)

        layout.addLayout(layout2)
        wid.setLayout(layout)
        self.setCentralWidget(wid)

    pass


def nextF(pic,name, iterator):

    iterator += 1
    iterator %= len(memeList)
    pic.setPixmap(QPixmap("../pics/" + memeList[iterator][1]))
    name.setText(memeList[iterator][0])


if  __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()