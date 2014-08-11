import cv2
import numpy as np
from matplotlib import pyplot as plt
#sudo apt-get install python-matplotlib
img = cv2.imread('photo2.JPG',0)

adth = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
blur = cv2.GaussianBlur(adth,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.imshow(th3,'gray')
plt.show()
cv2.imwrite("out.jpg", th3);