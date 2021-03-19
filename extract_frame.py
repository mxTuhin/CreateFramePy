import cv2

cam= cv2.VideoCapture('PreVid.mp4')
i=0
while(cam.isOpened()):
    ret, frame = cam.read()
    if ret == False:
        break
    cv2.imwrite('images/PreImg-'+str(i)+'.jpg',frame)
    i+=1

cam.release()
cv2.destroyAllWindows()