#this script is a motion detector , detects when an object entred into a frame and 
#when the object existed with graph representations

import cv2 
import time
from datetime import datetime
import pandas as pd

first_frame = None
status_list = []
time_ = []
df = pd.DataFrame(columns = ['Start','End'])


capture = cv2.VideoCapture('me.mp4')

while True:
    check , frame = capture.read()
    
    status = 0
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    
    '''capturing first_frame of the video'''
    if first_frame  is None:
        first_frame = gray
        continue
    
    '''comparing first_frame and second_frame of the video'''
    current_frame = cv2.absdiff(first_frame,gray)
    
    '''Detecting motions in the video using threshold method'''
    threshold_frame = cv2.threshold(current_frame ,40 ,255, cv2.THRESH_BINARY)[1]
    
    '''Deleting the black holes in the white area in the video using the dilate function'''
    threshold_frame = cv2.dilate(threshold_frame,None ,iterations=2)
    
    '''Finding the contours of the images in video using the findContours() funtion
         and storing them in a variable '''
    (cnts,_) = cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    
    
    '''Finding contours greater than 1000 pixels'''
    
    for contours in cnts:
        if cv2.contourArea(contours) < 1000:
            continue
        status = 1
        
        (x, y, w, h) = cv2.boundingRect(contours)
        cv2.rectangle(frame , (x,y),(x+w , y+h) , (0,255,0) , 3)
        
        '''Creating conditionals to check the time an object enters and exits the video or camera'''
        status_list = status_list[-2:]
        
        if status_list[-1] == 1 and status_list[-2]== 0:
            time_.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2]== 1:
            time_.append(datetime.now())    
               
            
    
    status_list.append(status)
    #cv2.imshow('Original',frame)
    # cv2.imshow('First Frame',first_frame)
    # cv2.imshow('Second Frame',current_frame)
    # cv2.imshow('Motion Detection', threshold_frame)
    cv2.imshow('Color Frame',frame)
    
    
    key = cv2.waitKey(10)
    if key ==  ord('q'):
        if status == 1:
            time_.append(datetime.now())
        break
    
#print(status) 
print(status_list)
print(time_)

for i  in range(0, len(time_),2):
    df = df._append({'Start': time_[i] , 'End': time_[i+0]},ignore_index=True)
    
df.to_csv('Time_.csv')

capture.release()
cv2.destroyAllWindows