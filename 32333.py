import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2

cam1Set='nvarguscamerasrc sensor_id=0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam1=cv2.VideoCapture(cam1Set)



while True:
    ret, frame1=cam1.read()
    cv2.imshow('piCam',frame1)
    cv2.moveWindow('piCam',0,0)

  



    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.DestroyAllWindows