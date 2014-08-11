import cv2
import numpy as np

def thresh_callback(thresh):
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        bx,by,bw,bh = cv2.boundingRect(cnt)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),1)   # draw contours in green color
        cv2.rectangle(drawing,(bx,by),(bx+bw,by+bh),(255,0,0),1) # draw rectangle in blue color)
    cv2.imshow('output',drawing)
    cv2.imshow('input',img)



#==========================================================Main============================================
img = cv2.imread('out.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)

#cv2.namedWindow('input')

#==============================Control Bar=========================
#thresh = 100
#max_thresh = 255
#cv2.createTrackbar('canny thresh:','input',thresh,max_thresh,thresh_callback)
#==============================Control Bar=========================

thresh_callback(100)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()