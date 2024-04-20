#This program detects faces in video , with a green rectangle 
#this script plays a video ,can change the colors of the video into gray and other colors based on
#your preference and can slow/fast down the video with cv2.waitKey() function


import cv2
import time

cap = cv2.VideoCapture('ban.mkv')

#counting video iteration
iteration_count = 0
face_cascade_model =  cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    
    iteration_count = iteration_count + 1
    
    check , frame = cap.read()
    print(check)
    print(frame)
    face_figures = face_cascade_model.detectMultiScale(frame, 
                                                   scaleFactor=1.05,
                                                   minNeighbors=5,
                                                   )
    
    for x, y, w, h in face_figures:
        c = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow('Capture' , frame)
    key =  cv2.waitKey(1)
    
    if key == ord('q'):
        break
  
print(c)  
print(iteration_count)
cap.release()
cv2.destroyAllWindows

