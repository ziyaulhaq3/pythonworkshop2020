import cv2
video =cv2. VideoCapture(r"/home/aiktc/Desktop/zpython/faceDetection.mp4")



check=True
while check:
    check,frame=video.read()
#print(type(video))
#print(type(check))
#print(frame)
    
    face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


    img=frame
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiScale(grey_img,
    scaleFactor=1.6,
    minNeighbors=5)
    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(458,255,569),2)
    #print(type(faces))
    #print(faces)
    resized = cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
    cv2.imshow("Grey",resized)


    key=cv2.waitKey(10)
    if(key==ord('q')):
        break
cv2.destroyAllWindows
video.release()
