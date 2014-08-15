import cv2
import numpy as np


#==========================================================Functions============================================
listRect = []
def mergeNear(bx,by,bw,bh):
    currentX, currentY, currentW, currentH = bx, by, bw, bh
    listRect.append([currentX, currentY, currentW, currentH])
    for aRect in listRect:
        [tempX, tempY, tempW, tempH] = aRect
        if (abs(tempX+tempW - currentX)<5):
            tempW = tempW + currentW
            aRect = [tempX, tempY, tempW, tempH]
    
def thresh_callback(thresh):
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        bx,by,bw,bh = cv2.boundingRect(cnt)
        mergeNear(bx,by,bw,bh)
        
        
        cv2.drawContours(drawing,[cnt],0,(255,0,0),1)   # draw contours in green color
        cv2.rectangle(drawing,(bx,by),(bx+bw,by+bh),(0,255,0),1) # draw rectangle in blue color)
    cv2.imshow('output',drawing)
    #cv2.imshow('input',img)



#==========================================================Main============================================
img = cv2.imread('out.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)

thresh_callback(100)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
#==========================================================/Main============================================


