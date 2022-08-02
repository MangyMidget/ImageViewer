# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"Image Viewer/bin/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 1280, 620))
        self.photo.setText("")
        self.current_image = r'Image Viewer/bin/NoDirectoryFound.png'
        self.photo.setPixmap(QtGui.QPixmap(self.current_image))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 620, 450, 100))
        self.back.setObjectName("back")
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setGeometry(QtCore.QRect(830, 620, 450, 100))
        self.forward.setObjectName("forward")
        self.dir_button = QtWidgets.QPushButton(self.centralwidget)
        self.dir_button.setGeometry(QtCore.QRect(450, 620, 381, 101))
        self.dir_button.setObjectName("dir")
        MainWindow.setCentralWidget(self.centralwidget)

        self.dir_button.clicked.connect(self.open_file_dialog)
        self.back.clicked.connect(lambda: self.clicker(0))
        self.forward.clicked.connect(lambda: self.clicker(1))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicker(self, func):
        if self.current_image == r'Image Viewer\bin\NoDirectoryFound.png':
            return

        try:
            index = self.images.index(self.current_image)
        except AttributeError:
            return
        except ValueError:
            return
        print('\nINDEX % s' % index)
        if func == 0: # back
            if index - 1 == -1:
                self.current_image = self.images[-1]
            else:
                self.current_image = self.images[index - 1]
        elif func == 1: # forward
            if index + 1 >= len(self.images):
                self.current_image = self.images[0]
            else:
                self.current_image = self.images[index + 1]
        else: return

        img_path = self.newdir + '/' + self.current_image
        print(img_path)

        self.photo.setPixmap(QtGui.QPixmap(img_path))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer"))
        self.back.setText(_translate("MainWindow", "<-"))
        self.forward.setText(_translate("MainWindow", "->"))
        self.dir_button.setText(_translate("MainWindow", "No Current Directory"))

    def open_file_dialog(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select Image Directory')
        if not filename == '':
            self.open_images(filename)
        else: return

    def open_images(self, dir):
        print('Original Dir %s' % dir)
        self.newdir = dir
        print('New dir %s' % self.newdir)

        files = []
        for file in os.listdir(self.newdir):
            if not os.path.isdir(file): files.append(file)

        self.images = []
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                self.images.append(file)

        if len(self.images) <= 0:
            self.dir_button.setText('No image files')
            self.current_image = r'Image Viewer/bin/NoDirectoryFound.png'
            self.photo.setPixmap(QtGui.QPixmap(self.current_image))
            return

        self.current_image = self.images[0]
        print(self.current_image)
        img_path = self.newdir + '/' + self.current_image
        print(img_path)

        self.dir_button.setText(self.newdir)
        self.photo.setPixmap(QtGui.QPixmap(img_path))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
