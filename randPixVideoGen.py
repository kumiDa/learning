import cv2
import numpy as np

while (cv2.waitKey(1)):
    randImg=np.random.randint(low=0,high=256,size=(480,848,3)) # random MAT generation
    cv2.imwrite('a.jpg',randImg)
    img=cv2.imread('a.jpg') # temp file creation
    cv2.imshow("randomVideo",img)
    if cv2.waitKey(1) & 0xFF == ord('`'):
        cv2.destroyAllWindows()
        break
