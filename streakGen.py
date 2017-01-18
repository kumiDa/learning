import numpy as np
import cv2

cap = cv2.VideoCapture(0) # capturing stream from the webcam
dict=[]
while(cap.isOpened()):
    # reading the capture.
    ret, frame = cap.read()
    if ret==True:
        dict.append(np.mean(frame,axis=0,dtype=int)) #generating mean rgb values for streak generation
        cv2.imshow('frame',np.array(dict,dtype=int)) #display of the frame buildup
        #end the buildup by pressing '`'
        if cv2.waitKey(1) & 0xFF == ord('`'):
            # print np.array(dict) #the rgb MAT generation for debugging
            cv2.imwrite('frame.jpg', np.array(dict, dtype=int))
            cv2.destroyAllWindows()
            break
    else:
        break

#display the generated strek image from the capture
img=cv2.imread('frame.jpg')
cv2.imshow('generated streak image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()