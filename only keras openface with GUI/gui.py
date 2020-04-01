import test
from random import choice
from numpy import load
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from matplotlib import pyplot

from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
from keras.models import load_model

import test
import os
import glob
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import Label,Tk
from PIL import Image, ImageTk
import glob
import cv2
from tensorflow.python.client import device_lib

class home:
    
    def __init__(self,master):

        #lbp_face_recognition.train()
        #gabor_face_recognition.train()
        print(device_lib.list_local_devices())
        

        test.load_ram()       

        self.master=master
        self.f=Frame(master,width=1000,height=600)
        self.f.propagate(0)
        self.f.pack()
        self.f["bg"]='#2874A6'
        heading=Label(self.f,text="Low Light Facial Recognition",bg='#2874A6',font=('Times new Roman',-50,'bold')).grid(row=1,column=1,padx=20,pady=50)
        #heading.place(x=350,y=200)
        buttonchoose=Button(self.f,text="Choose Test Image",command=self.choose,font=('times new roman',-20),width=15,height=3).grid(row=2,column=1,padx=20,pady=50)
        buttontest=Button(self.f,text="Find Face",command=self.test,font=('times new roman',-20),width=15,height=3).grid(row=2,column=2,padx=20,pady=50)
        

    def choose(self):
        global path
        path=filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        im = Image.open(path)
        im2 = im.resize((250, 250), Image.ANTIALIAS)
        
        global tkimage1
        tkimage1 = ImageTk.PhotoImage(im2)
        
        myvar1=Label(self.f,image = tkimage1).grid(row=6,column =2)
        myvar1.image = tkimage1
        myvar1.pack()

    def test(self):

        img = cv2.imread(path)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
        image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        path2 = os.path.dirname(path)+"/clahe_out.jpeg"
        cv2.imwrite(path2,image)



        images = Image.open(path2)
        im3 = images.resize((250, 250), Image.ANTIALIAS)
        
        tkimage3 = ImageTk.PhotoImage(im3)
        myvar3=Label(self.f,image = tkimage3).grid(row=6,column =1)
        
        
        match_path = test.match_path(path);
        
##        
##        maximum_avg=0
##        imgs = [item for i in [glob.glob('./resource/pantar_logs/*.%s' % ext) for ext in ["jpg","pgm","png","bmp","jpeg"]] for item in i]
##        for img in imgs:
##            percent_1 = lbp_face_recognition.hist_get(path,img)
##            #percent_2 = gabor_face_recognition.get_hist(path,img)
##
##            avg = percent_1 
##            if(avg > maximum_avg):
##                maximum_avg = avg
##                match_path = img
##                if(maximum_avg<0.6):
##                    match_path='./resource/notfound.png'
##        print path,img,match_path

        print(match_path)
        final_path = '5-celebrity-faces-dataset/train/'+match_path
        
        print(final_path)
        im = Image.open(final_path+"/"+os.listdir(final_path)[0])
        im2 = im.resize((250, 250), Image.ANTIALIAS)
        
        tkimage = ImageTk.PhotoImage(im2)
        myvar1=Label(self.f,image = tkimage1).grid(row=6,column =2)
        myvar2=Label(self.f,image = tkimage).grid(row=6,column =3)
        myvar2.pack()
        
        

root=Tk()
home=home(root)
root.mainloop()
