import cv2
import numpy as np
import os
import sys

# method to generate frames of random columns
def colGen():
    randImg=np.empty((480,848,3))
    rowMat=np.empty((848,3))
    while (cv2.waitKey(1)):
        rowMat=np.random.randint(low=0,high=256,size=(848,3)) # random MAT generation
        for i in range(480):
            randImg[i]=rowMat
        cv2.imwrite('a.jpg',randImg)
        img=cv2.imread('a.jpg')
        cv2.imshow("random column generation",img)
        if cv2.waitKey(1) & 0xFF == ord('`'):
            cv2.destroyAllWindows()
            break
    os.system("rm -rf a.jpg")

# method to generate frames of random rows
def rowGen():
    randImg=np.empty((480,848,3))
    randVal=np.empty((3))
    while (cv2.waitKey(1)):
        for i in range(480):
            randVal=np.random.randint(low=0,high=256,size=(3)) # random MAT generation
            for j in range(848):
                randImg[i,j]=randVal
        cv2.imwrite('a.jpg',randImg)
        img=cv2.imread('a.jpg')#temp file creation
        cv2.imshow("random row generation",img)
        if cv2.waitKey(1) & 0xFF == ord('`'):
            cv2.destroyAllWindows()
            break
    os.system("rm -rf a.jpg")

# method to generate frames of random pixels
def pixelGen():
    randImg=np.empty((480,848,3))
    while (cv2.waitKey(1)):
        randImg = np.random.randint(low=0, high=256, size=(480,848,3))  # random MAT generation
        cv2.imwrite('a.jpg', randImg)
        img=cv2.imread('a.jpg')
        cv2.imshow("random pixel generation", img)
        if cv2.waitKey(1) & 0xFF == ord('`'):
            cv2.destroyAllWindows()
            break
    os.system("rm -rf a.jpg")

# code to call thw required function through commandline arguments
# 1 - pixel generation
# 2 - column generation
# 3 - row generation
calls={
    1: pixelGen ,
    2: colGen ,
    3: rowGen ,
}
argc,argv=sys.argv

calls[int(argv)]()


