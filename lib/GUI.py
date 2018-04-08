from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from lib import parser
from lib.parser import *
import urllib.request

iterator = 0
name = ""

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Meme Tinder")
        global iterator
        global name
        MemesTable = get_next_memes()
        iterator = 0
        urllib.request.urlretrieve(MemesTable[iterator].src,
                                   MemesTable[iterator].src[MemesTable[iterator].src.rfind('/') + 1:])

        wid = QWidget()
        layout = QVBoxLayout()

        label = QLabel(MemesTable[iterator].alt)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(25)
        layout.addWidget(label)


        pic = QLabel()
        pic.setPixmap(QPixmap(MemesTable[iterator].src[MemesTable[iterator].src.rfind('/') + 1:]).scaled(720,720,Qt.KeepAspectRatio))
        pic.setAlignment(Qt.AlignCenter)
        layout.addWidget(pic)


        wid2 = QWidget()
        layout2 = QHBoxLayout()

        save = QPushButton("save")
        save.clicked.connect(lambda: saveFunction(MemesTable[iterator].src[MemesTable[iterator].src.rfind('/') + 1:]))
        layout2.addWidget(save)

        dislike = QPushButton("dislike")
        # like.clicked.connect(dislikeFunction())
        layout2.addWidget(dislike)

        next = QPushButton("next")
        next.clicked.connect(lambda: nextF(pic, label, MemesTable))
        layout2.addWidget(next)

        layout.addLayout(layout2)
        wid.setLayout(layout)

        self.setCentralWidget(wid)
        urllib.request.urlcleanup()
        name = MemesTable[iterator].src[MemesTable[iterator].src.rfind('/') + 1:]

    pass


def saveFunction(pic):
    from shutil import copy
    copy("./"+pic, "./pics")


def nextF(pic, name2, MemeTable):
    global iterator
    global name
    import os
    os.remove("./"+MemeTable[iterator].src[MemeTable[iterator].src.rfind('/') + 1:])

    iterator += 1

    if iterator >= len(MemeTable):
        MemeTable = get_next_memes()
        iterator = 0
    name = MemeTable[iterator].src[MemeTable[iterator].src.rfind('/') + 1:]
    urllib.request.urlretrieve(MemeTable[iterator].src,
                               MemeTable[iterator].src[MemeTable[iterator].src.rfind('/') + 1:])
    pic.setPixmap(QPixmap(MemeTable[iterator].src[MemeTable[iterator].src.rfind('/') + 1:]).scaled(720,720,Qt.KeepAspectRatio))
    name2.setText(MemeTable[iterator].alt)


if __name__ == "__main__":
    parser.current_page = get_latest_page()[0]
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

    import os
    os.remove("./" + name)
