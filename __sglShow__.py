#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import os
from PIL import Image, ImageQt
import __sepia__

#img_list = []
class example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
#        self.initUI(img_list)
        self.layer_check = 0

    def initUI(self, img_list):
        if self.layer_check:
            self.my_list = img_list
            self.my_img = self.my_list[0]
            self.pixmap = QtGui.QPixmap(self.my_img)
            self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatioByExpanding)
            self.lbl.setPixmap(self.pixmap)
            self.centerOnScreen()

        else:
            self.col = QtGui.QColor(0, 0, 0)
            self.main_box = QtWidgets.QHBoxLayout(self)
            self.side_box = QtWidgets.QVBoxLayout(self)
            self.main_box.addLayout(self.side_box)
            self.rot_box = QtWidgets.QHBoxLayout(self)
            self.side_box.addLayout(self.rot_box)
            rot_cwb = QtWidgets.QPushButton(self)
            rot_cwb.setIcon(QtGui.QIcon(QtGui.QPixmap('Right_rotate.png')))
            self.rot_box.addWidget(rot_cwb)
#            rot_cwb.move(0, 0)
            rot_cwb.clicked.connect(self.imgRot_rtl)
            rot_ucwb = QtWidgets.QPushButton(self)
            rot_ucwb.setIcon(QtGui.QIcon(QtGui.QPixmap('Left_rotate.png')))
            self.rot_box.addWidget(rot_ucwb)
            rot_ucwb.clicked.connect(self.imgRot_ltr)
            rot_cwb.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            rot_ucwb.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sepiab = QtWidgets.QPushButton('Sepia Image', self)
            self.side_box.addWidget(sepiab)
            sepiab.clicked.connect(self.sepia_img)
            self.side_box.addStretch()
            self.lbtex = QtWidgets.QLabel(self)
            self.side_box.addWidget(self.lbtex)
            self.lbtex.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#            self.side_box.addStretch()
            self.vbox = QtWidgets.QVBoxLayout(self)
            self.main_box.addLayout(self.vbox)
            self.lbl = QtWidgets.QLabel(self)
            self.lbl.setAlignment(QtCore.Qt.AlignCenter)
            self.vbox.addWidget(self.lbl)

            self.hbox =  QtWidgets.QHBoxLayout(self)
            self.vbox.addLayout(self.hbox)

#            self.all_layouts = self.layout().count()
            self.my_list = img_list
            self.my_img = self.my_list[0]

            prevb = QtWidgets.QPushButton('<< &Previous', self)
            self.hbox.addWidget(prevb)

#            prevb.move(30, 130)
            prevb.clicked.connect(self.setPrev)

            nextb = QtWidgets.QPushButton('&Next >>', self)
            self.hbox.addWidget(nextb)

#            nextb.move (130,130)
            nextb.clicked.connect(self.setPrev)
            nextb.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            prevb.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            
    #        self.square = QFrame(self)
            #self.square.setGeometry(150, 20, 100, 100)
            #self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

    #        self.setGeometry(300, 300, 280, 170)

            self.pixmap = QtGui.QPixmap(self.my_img)
            self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatioByExpanding)
            self.lbl.setPixmap(self.pixmap)
            self.pil_img = Image.open(self.my_img)
            self.lbtex.setText("Format: "+self.pil_img.format+"\n"+ "Size: "+"%dx%d" % self.pil_img.size+"\n" + "Mode: "+self.pil_img.mode)
            self.setLayout(self.main_box)
            self.setWindowTitle("Image Viewer")

            self.setGeometry(0, 0, 300, 250)

    #        self.hbox.setAlignment(QtCore.Qt.AlignCenter)
    #        self.vbox.setAlignment(QtCore.Qt.AlignCenter)
            self.show()
    #        self.all_layouts = self.layout().count()
#            print("firstly, all layouts = ", self.all_layouts)
            self.layer_check = self.layout().count()
            self.centerOnScreen()


    def centerOnScreen (self):
            '''centerOnScreen()
    Centers the window on the screen.'''
            resolution = QtWidgets.QDesktopWidget().screenGeometry()
            self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                      (resolution.height() / 2) - (self.frameSize().height() / 2)) 


    def setPrev(self):
        source = self.sender()
#        self.pixmap = QtGui.QPixmap(self.my_img)
#        self.lbl = QtWidgets.QLabel(self)
#        self.lbl.setPixmap(self.pixmap)
#        self.hbox.addWidget(self.lbl)
#        self.setLayout(self.hbox)
#        self.lbl.show()

        length = len(self.my_list)
#        print(length)
#        print(self.my_img)
        if source.text() == '&Next >>':
#            print(self.my_list.index(self.my_img))
            now_index = self.my_list.index(self.my_img)
            next_index = (now_index + 1) % length
#            print(now_index, next_index)
            self.my_img = self.my_list[next_index]
            self.pixmap = QtGui.QPixmap(self.my_img)      
            self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatioByExpanding)
            self.lbl.setPixmap(self.pixmap)
            self.pil_img = Image.open(self.my_img)
            self.lbtex.setText("Format: "+self.pil_img.format+"\n"+ "Size: "+"%dx%d" % self.pil_img.size+"\n" + "Mode: "+self.pil_img.mode)

#            self.all_layouts = self.layout().count()
#            print('secondly, all layouts = ', self.all_layouts)
#            self.hbox.addWidget(self.lbl)
#            self.lbl.show()

        elif source.text() == '<< &Previous':
            now_index = self.my_list.index(self.my_img)
            prev_index = (now_index - 1) % length
#            print(now_index, prev_index)
            self.my_img = self.my_list[prev_index]
            self.pixmap = QtGui.QPixmap(self.my_img)      
            self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatioByExpanding)
            self.lbl.setPixmap(self.pixmap)
            self.pil_img = Image.open(self.my_img)
            self.lbtex.setText("Format: "+self.pil_img.format+"\n"+ "Size: "+"%dx%d" % self.pil_img.size+"\n" + "Mode: "+self.pil_img.mode)


    def imgRot_rtl (self):
        # Rotate from initial image to avoid cumulative deformation from
        # transformation
        transform = QtGui.QTransform().rotate(90)
        self.pixmap = self.pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatioByExpanding)
        self.lbl.setPixmap(self.pixmap)
#        self.lbl.show()

    def imgRot_ltr (self):
        # Rotate from initial image to avoid cumulative deformation from
        # transformation
        transform = QtGui.QTransform().rotate(-90)
        self.pixmap = self.pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatioByExpanding)
        self.lbl.setPixmap(self.pixmap)

    def sepia_img(self):
        pil_img = self.my_img
        sepiaImg = __sepia__.create_sepia(pil_img)
        self.pixmap = QtGui.QPixmap.fromImage(sepiaImg)
        self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatioByExpanding)
        self.lbl.setPixmap(self.pixmap)


if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)

    pics_dir = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', QtCore.QDir.homePath(), QtWidgets.QFileDialog.ShowDirsOnly)

    included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
    flist = [fn for fn in os.listdir(pics_dir)
              if any(fn.endswith(ext) for ext in included_extensions)]


    img_list = []
    for n in flist:
        img = pics_dir+"/"+str(n)
        img_list.append(img)

    img_list.sort(reverse=False)

    ex = example()
#    ex.initUI(img_list)
    ex.initUI(img_list)
    sys.exit(app.exec_())
