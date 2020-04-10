import numpy as np
import cv2


def clahe():
    img = cv2.imread('C:\\Users\\Anton\\OneDrive\\Documents\\GitHub\\Low-light-during-quarantine\\GUI_LLFR\\resource\\testing\\warade_dark.jpeg')
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
    image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    cv2.imwrite('C:/Users/Anton/OneDrive/Desktop/clahe.jpeg',image)
