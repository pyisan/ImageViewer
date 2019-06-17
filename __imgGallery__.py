from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os
from PyQt5.QtGui import QPixmap


class ImageGallery(QWidget):

    def __init__(self):
        super().__init__()
#        self.setWindowTitle("Image Gallery")
        self.setLayout(QGridLayout(self))
#        self.show()

    def populate(self, img_list, size, imagesPerRow=3, flags=Qt.KeepAspectRatioByExpanding):
        row = col = 0
        old_layout = self.layout()
#        print("Layout Count: ", old_layout.count())
        if old_layout.count() > 0:
            for i in reversed(range(old_layout.count())):
                old_layout.itemAt(i).widget().setParent(None)
#            old_layout.deleteLater()
#            self.setLayout(QGridLayout(self))
        pics = img_list
        for pic in pics:
            label = ImageLabel("")
            pixmap = QPixmap(str(pic))
            pixmap = pixmap.scaled(size, flags)
            label.setPixmap(pixmap)
            self.layout().addWidget(label, row, col)
            col +=1
            if col % imagesPerRow == 0:
                row += 1
                col = 0



class ImageLabel(QLabel):
    """ This widget displays an ImagePopup when the mouse enters its region """
    def enterEvent(self, event):
        self.p = ImagePopup(self)
        self.p.show()
        event.accept()


class ImagePopup(QLabel):
    """
    The ImagePopup class is a QLabel that displays a popup, zoomed image
    on top of another label.
    """
    def __init__(self, parent):
        super().__init__()

        thumb = parent.pixmap()
        imageSize = thumb.size()
        imageSize.setWidth(imageSize.width()*2)
        imageSize.setHeight(imageSize.height()*2)
        self.setPixmap(thumb.scaled(imageSize,Qt.KeepAspectRatioByExpanding))


        position = self.cursor().pos()
        position.setX(position.x() - thumb.size().width())
        position.setY(position.y() - thumb.size().height())
        self.move(position)


        self.setWindowFlags(Qt.Popup | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint)
    #sleep(4)
    def leaveEvent(self, event):

        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    pics_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', QDir.homePath(), QFileDialog.ShowDirsOnly)

    #pics_dir = os.path.expanduser('~/Pictures') or QDir.currentPath()

    included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
    flist = [fn for fn in os.listdir(pics_dir)
              if any(fn.endswith(ext) for ext in included_extensions)]


    img_list = []
    for n in flist:
        img = pics_dir+"/"+str(n)
        img_list.append(img)
    img_list.sort()

    i = ImageGallery()
    i.populate(img_list, QSize(100, 70))

    i.show()

    sys.exit(app.exec_())

