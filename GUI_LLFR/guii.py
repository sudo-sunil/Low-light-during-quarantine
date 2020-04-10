# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guii.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os

import sys

from PIL import Image, ImageTk
import glob




import lbp_face_recognition
import gabor_face_recognition
import numpy as np
import cv2
import glob
import os.path

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon




class Ui_MainWindow(object):
    def __init__(self):
        lbp_face_recognition.train()
        #gabor_face_recognition.train()
        self.path = None
        self.clahedpath = None
        self.match_path = None
        self.videopath = None
       
        
        
    def selectimage_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        print(self.path)
        self.clahedpath = None
        self.match_path = None
        self.setupUi(MainWindow)


    def selectvideofile(self):
        print("select video Button pressed")
        filename1 = QFileDialog.getOpenFileName()
        self.videopath = filename1[0]
        print(self.videopath)
        self.setupUi(MainWindow)



        
    def processClick(self):
        print("process clicked")
        img = cv2.imread(self.path)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
        image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        cv2.imwrite('C:/Users/Anton/OneDrive/Documents/GitHub/Low-light-during-quarantine/GUI_LLFR/clahe/clahe.jpeg',image)
        self.clahedpath = 'C:/Users/Anton/OneDrive/Documents/GitHub/Low-light-during-quarantine/GUI_LLFR/clahe/clahe.jpeg'
        self.setupUi(MainWindow)
        
    def extractfaces_img(self):
        print("extractfaces clicked")
        
        maximum_avg=0
        imgs = [item for i in [glob.glob('./resource/pantar_logs/*.%s' % ext) for ext in ["jpg","pgm","png","bmp","jpeg"]] for item in i]
        for img in imgs:
            percent_1 = lbp_face_recognition.hist_get(self.clahedpath,img)
            #percent_2 = gabor_face_recognition.get_hist(self.clahedpath,img)

            avg = percent_1 
            if(avg > maximum_avg):
                maximum_avg = avg
                self.match_path = img
                if(maximum_avg<0.6):
                    self.match_path='./resource/notfound.png'
            print self.path,self.clahedpath,img,self.match_path
        self.setupUi(MainWindow)      
    

        
    def setupUi(self, MainWindow):

 
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 692)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.left = QtWidgets.QFrame(self.frame)
        self.left.setGeometry(QtCore.QRect(0, 0, 371, 431))
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")


        self.process = QtWidgets.QPushButton(self.left)
        self.process.setGeometry(QtCore.QRect(20, 210, 130, 30))
        self.process.setObjectName("process")
        


        self.extractfaces = QtWidgets.QPushButton(self.left)
        self.extractfaces.setGeometry(QtCore.QRect(20, 350, 130, 30))
        self.extractfaces.setObjectName("extractfaces")


        self.selectimage = QtWidgets.QPushButton(self.left)
        self.selectimage.setGeometry(QtCore.QRect(160, 0, 120, 30))
        self.selectimage.setObjectName("selectimage")


        self.extractfacesimg = QtWidgets.QLabel(self.left)
        self.extractfacesimg.setGeometry(QtCore.QRect(160, 300, 120, 120))
        self.extractfacesimg.setObjectName("extractfacesimg")
        self.extractfacesimg.setPixmap(QtGui.QPixmap(self.match_path))        
        self.extractfacesimg.setScaledContents(True)


        self.processimg = QtWidgets.QLabel(self.left)
        self.processimg.setGeometry(QtCore.QRect(160, 170, 120, 120))
        self.processimg.setObjectName("processimg")
        self.processimg.setPixmap(QtGui.QPixmap(self.clahedpath))        
        self.processimg.setScaledContents(True)

        
        self.selectimgimg = QtWidgets.QLabel(self.left)
        self.selectimgimg.setGeometry(QtCore.QRect(160, 40, 120, 120))
        self.selectimgimg.setObjectName("selectimgimg")
        self.selectimgimg.setPixmap(QtGui.QPixmap(self.path))        
        self.selectimgimg.setScaledContents(True)
        

        
        self.right = QtWidgets.QFrame(self.frame)
        self.right.setGeometry(QtCore.QRect(370, 0, 421, 431))
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")

        
        self.selectvideotext = QtWidgets.QLineEdit(self.right)
        self.selectvideotext.setGeometry(QtCore.QRect(120, 20, 271, 31))
        self.selectvideotext.setObjectName("selectvideotext")
        self.selectvideotext.setText(self.videopath)

        
        self.totalfaces = QtWidgets.QLineEdit(self.right)
        self.totalfaces.setGeometry(QtCore.QRect(120, 70, 271, 41))
        self.totalfaces.setObjectName("totalfaces")

        
        self.extractfaces_2 = QtWidgets.QPushButton(self.right)
        self.extractfaces_2.setGeometry(QtCore.QRect(10, 80, 100, 30))
        self.extractfaces_2.setObjectName("extractfaces_2")

        
        self.imgdisplay = QtWidgets.QScrollArea(self.right)
        self.imgdisplay.setGeometry(QtCore.QRect(10, 160, 401, 251))
        self.imgdisplay.setWidgetResizable(True)
        self.imgdisplay.setObjectName("imgdisplay")

        
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 399, 249))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")


        self.imgdisplay.setWidget(self.scrollAreaWidgetContents_2)


        self.extractuniquefaces = QtWidgets.QPushButton(self.right)
        self.extractuniquefaces.setGeometry(QtCore.QRect(150, 120, 130, 30))
        self.extractuniquefaces.setObjectName("extractuniquefaces")


        self.selectvideo = QtWidgets.QPushButton(self.right)
        self.selectvideo.setGeometry(QtCore.QRect(10, 20, 100, 30))
        self.selectvideo.setObjectName("selectvideo")


        self.bottom = QtWidgets.QFrame(self.frame)
        self.bottom.setGeometry(QtCore.QRect(0, 430, 791, 261))
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")


        self.finddetails = QtWidgets.QPushButton(self.bottom)
        self.finddetails.setGeometry(QtCore.QRect(340, 0, 101, 30))
        self.finddetails.setObjectName("finddetails")


        self.detailimg = QtWidgets.QScrollArea(self.bottom)
        self.detailimg.setGeometry(QtCore.QRect(0, 40, 781, 201))
        self.detailimg.setWidgetResizable(True)
        self.detailimg.setObjectName("detailimg")


        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 199))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        self.detailimg.setWidget(self.scrollAreaWidgetContents)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        MainWindow.setTabOrder(self.selectimage, self.selectimgimg)
        MainWindow.setTabOrder(self.selectimgimg, self.process)
        MainWindow.setTabOrder(self.process, self.processimg)
        MainWindow.setTabOrder(self.processimg, self.extractfaces)
        MainWindow.setTabOrder(self.extractfaces, self.extractfacesimg)
        MainWindow.setTabOrder(self.extractfacesimg, self.selectvideo)
        MainWindow.setTabOrder(self.selectvideo, self.selectvideotext)
        MainWindow.setTabOrder(self.selectvideotext, self.extractfaces_2)
        MainWindow.setTabOrder(self.extractfaces_2, self.totalfaces)
        MainWindow.setTabOrder(self.totalfaces, self.extractuniquefaces)
        MainWindow.setTabOrder(self.extractuniquefaces, self.imgdisplay)
        MainWindow.setTabOrder(self.imgdisplay, self.finddetails)
        MainWindow.setTabOrder(self.finddetails, self.detailimg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Low Light Face Recognition"))


        self.process.setText(_translate("MainWindow", "Process"))
        self.process.clicked.connect(self.processClick)


        self.extractfaces.setText(_translate("MainWindow", "Extract Faces"))
        self.extractfaces.clicked.connect(self.extractfaces_img)

        
        self.selectimage.setText(_translate("MainWindow", "Select Image"))
        self.selectimage.clicked.connect(self.selectimage_handler)

        
        self.extractfaces_2.setText(_translate("MainWindow", "Extract Faces"))


        self.extractuniquefaces.setText(_translate("MainWindow", "Extract Unique Faces"))


        self.selectvideo.setText(_translate("MainWindow", "Select Video"))
        self.selectvideo.clicked.connect(self.selectvideofile)


        self.finddetails.setText(_translate("MainWindow", "Find Details"))

   
        
      
       

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
