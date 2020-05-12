import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

Motor_1 = 2
Motor_2 = 3
Motor_3 = 17
Motor_4 = 27

ENA = 4
ENB = 14

def Test():
  GPIO.output(Motor_3,GPIO.HIGH)
  GPIO.output(Motor_4,GPIO.LOW)

def Forward():
    GPIO.output(Motor_1,GPIO.HIGH)
    GPIO.output(Motor_2,GPIO.LOW)
    GPIO.output(Motor_3,GPIO.HIGH)
    GPIO.output(Motor_4,GPIO.LOW)
    GPIO.output(ENA,-120)
    GPIO.output(ENB,-150)
    

def Right():
    GPIO.output(Motor_1,GPIO.HIGH)
    GPIO.output(Motor_2,GPIO.LOW)
    GPIO.output(Motor_3,GPIO.LOW)
    GPIO.output(Motor_4,GPIO.LOW)
    

def Left():
    GPIO.output(Motor_1,GPIO.LOW)
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

    
while True:
    try:
      Forward()
    
    except KeyboardInterrupt:
        break
        
Stop()        

