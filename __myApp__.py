from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os
from PyQt5.QtGui import QPixmap
import __sglShow__
import __imgGallery__


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myLayout = QVBoxLayout(self)
        self.scroll_area = QScrollArea()
        self.myLayout.addWidget(self.scroll_area)
        self.setCentralWidget(self.scroll_area)
        self.setWindowTitle("Image Viewer")
        self.setLayout(self.myLayout)
        self.createMenus()
        self.a = int(input('Please Select: 1) Gallery 2)Slide: '))
        if self.a == 1:
            self.ImgGallery()
        elif self.a == 2:
            self.SglShow()
        else:
            print('Please select 1 for Gallery View or 2 for Slide View')
            return
#        self.setCentralWidget(self.ImgGallery)
        self.setGeometry(0, 0 , 400, 350)
        self.show()
#        self.ImgGallery.populate(img_list)

    def open (self):
        pics_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', QDir.homePath(), QFileDialog.ShowDirsOnly)


        included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
        flist = []
        flist = [fn for fn in os.listdir(pics_dir)
                  if any(fn.endswith(ext) for ext in included_extensions)]


        img_list = []
        for n in flist:
            img = pics_dir+"/"+str(n)
            img_list.append(img)

        img_list.sort()
#        self.imgGallery.update()
        if self.a == 1:
            self.imgGallery.populate(img_list, QSize(70, 50))
        else:
            self.sglShow.initUI(img_list)
        return img_list


    def createMenus(self):
        menuBar = self.menuBar()
        file_menu = menuBar.addMenu('&File')
        openAct = QAction('&Open', self, shortcut = 'Ctrl+O', triggered = self.open)
        file_menu.addAction(openAct)
        exitAct = QAction('&Quit', self, shortcut = 'Ctrl+Q', triggered = self.close)
        file_menu.addAction(exitAct)
#        action = file_menu.exec_(self.mapToGlobal(event.pos()))

        view_menu = menuBar.addMenu('&View')
        zoomMenu = QMenu('&Zoom', self)
        zoominAct = QAction('Zoom&In', self)
        zoomMenu.addAction(zoominAct)        
        view_menu.addMenu(zoomMenu)

#        if action == exitAct:
#            qApp.quit()

    def ImgGallery(self):
        self.imgGallery =  __imgGallery__.ImageGallery()

        self.scroll_area.setWidget(self.imgGallery)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setWidgetResizable(True)
#        self.setCentralWidget(self.imgGallery)
#        self.imgGallery.populate(img_list)

    def SglShow(self):
        self.sglShow = __sglShow__.example()
        self.setCentralWidget(self.sglShow)
#        self.sglShow().initUI(img_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    myapp = ImageViewer()
    sys.exit(app.exec_())
