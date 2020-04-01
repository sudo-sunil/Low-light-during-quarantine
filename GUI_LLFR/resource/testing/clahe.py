
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./shwetadark.jpeg')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imwrite('shweta_clahe.jpg',image)

display = [img, image]
label = ['Original Image', 'CLAHE Output']
fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(display[i], cmap = 'gray')
    plt.title(label[i])
plt.show()
