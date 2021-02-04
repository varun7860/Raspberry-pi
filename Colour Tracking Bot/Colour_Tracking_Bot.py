import cv2
import numpy as np
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

Motor_1 = 2
Motor_2 = 3
Motor_3 = 17
Motor_4 = 27

def Forward():
    GPIO.output(Motor_1,GPIO.HIGH)
    GPIO.output(Motor_2,GPIO.LOW)
    GPIO.output(Motor_3,GPIO.HIGH)
    GPIO.output(Motor_4,GPIO.LOW)

def Right():
    GPIO.output(Motor_1,GPIO.LOW)
    GPIO.output(Motor_2,GPIO.HIGH)
    GPIO.output(Motor_3,GPIO.HIGH)
    GPIO.output(Motor_4,GPIO.LOW)

def Left():
    GPIO.output(Motor_1,GPIO.HIGH)
    GPIO.output(Motor_2,GPIO.LOW)
    GPIO.output(Motor_3,GPIO.LOW)
    GPIO.output(Motor_4,GPIO.HIGH)

def Stop():
    GPIO.output(Motor_1,GPIO.LOW)
    GPIO.output(Motor_2,GPIO.LOW)
    GPIO.output(Motor_3,GPIO.LOW)
    GPIO.output(Motor_4,GPIO.LOW)

def Backward():
    GPIO.output(Motor_1,GPIO.LOW)
    GPIO.output(Motor_2,GPIO.HIGH)
    GPIO.output(Motor_3,GPIO.LOW)
    GPIO.output(Motor_4,GPIO.HIGH)

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    red = frame[:,:,2]
    green = frame[:,:,1]
    blue = frame[:,:,0]
    red_only = np.int16(red)-np.int16(green)-np.int16(blue)
    red_only[red_only<0] = 0
    red_only[red_only>255] = 255
    red_only = np.uint8(red_only)
    #cv2.imshow("frame",red_only)
    
    a = np.count_nonzero(red_only)
    if a >10000: 
        column_sums = np.matrix(np.sum(red_only,0))
        column_numbers = np.matrix(np.arange(640))
        column_mult = np.multiply(column_sums,column_numbers)
        total_1 = np.sum(column_mult)
        total_total_1 = np.sum(np.sum(red_only))
        result_1 = np.count_nonzero(column_sums)
        
        
        if result_1<30:
           X_cordinate = 0.0
        else:
           X_cordinate = total_1/total_total_1
                
        print("Location Of Object is :" ,X_cordinate)
        
        
        if X_cordinate >200 and X_cordinate<400:
            print("Forward")
            Forward()
            sleep(0.06)
            Stop()
            sleep(0.04)
            
        if X_cordinate<200:
            print("Object detected at Left")
            Left()
            sleep(0.02)
            Stop()
            sleep(0.04)
            
        if X_cordinate>400:
            print("Object detected at Right")
            Right()
            sleep(0.02)
            Stop()
            sleep(0.04)
    else:
        print("No Object Detected")
        Stop() 
    
    if cv2.waitKey(5)==27:
        break

stop()
cap.release()
cv2.destroyAllWindows()
