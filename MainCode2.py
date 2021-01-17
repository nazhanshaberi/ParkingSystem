EMC311 Group 13

import RPi.GPIO as GPIO
import wiringpi as wiringpi  
import time

wiringpi.wiringPiSetupGpio()
GPIO.setmode(GPIO.BCM) 
wiringpi.pinMode(4,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(384)   
wiringpi.pwmSetRange(1000)  
wiringpi.pwmWrite(4,120)
GPIO.setup(14, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.OUT) 
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT) 
GPIO.setup(2, GPIO.IN)  
GPIO.setup(3, GPIO.IN)   
GPIO.setup(4, GPIO.OUT) 

def disp(int):
  if int==0:
    num0()
  elif int==1:
    num1()
  elif int==2:
    num2()
  elif int==3:
    num3()
  elif int==4:
    num4()
  elif int==5:
    num5()
 
  return;

def num0():                 
  GPIO.output(14, GPIO.HIGH)  
  GPIO.output(15, GPIO.HIGH)  
  GPIO.output(18, GPIO.HIGH) 
  GPIO.output(23, GPIO.HIGH) 
  GPIO.output(24, GPIO.HIGH) 
  GPIO.output(25, GPIO.HIGH) 
  GPIO.output(8, GPIO.LOW)   
def num1():
  GPIO.output(14, GPIO.LOW)  
  GPIO.output(15, GPIO.HIGH)  	
  GPIO.output(18, GPIO.HIGH)  
  GPIO.output(23, GPIO.LOW) 
  GPIO.output(24, GPIO.LOW)  
  GPIO.output(25, GPIO.LOW)  
  GPIO.output(8, GPIO.LOW)  
def num2():
  GPIO.output(14, GPIO.HIGH)  
  GPIO.output(15, GPIO.HIGH)  
  GPIO.output(18, GPIO.LOW)  
  GPIO.output(23, GPIO.HIGH)  
  GPIO.output(24, GPIO.HIGH)  
  GPIO.output(25, GPIO.LOW)  
  GPIO.output(8, GPIO.HIGH)  
def num3():
  GPIO.output(14, GPIO.HIGH) 
  GPIO.output(15, GPIO.HIGH) 
  GPIO.output(18, GPIO.HIGH)  
  GPIO.output(23, GPIO.HIGH)  
  GPIO.output(24, GPIO.LOW)
  GPIO.output(25, GPIO.LOW) 
  GPIO.output(8, GPIO.HIGH)  
def num4():
  GPIO.output(14, GPIO.LOW) 
  GPIO.output(15, GPIO.HIGH)  
  GPIO.output(18, GPIO.HIGH) 
  GPIO.output(23, GPIO.LOW)  
  GPIO.output(24, GPIO.LOW) 
  GPIO.output(25, GPIO.HIGH) 
  GPIO.output(8, GPIO.HIGH)  
def num5():
  GPIO.output(14, GPIO.HIGH)
  GPIO.output(15, GPIO.LOW)
  GPIO.output(18, GPIO.HIGH) 
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(24, GPIO.LOW)
  GPIO.output(25, GPIO.HIGH)  
  GPIO.output(8, GPIO.HIGH)  

print("Press CTRL+C to exit the simulation")  
try:
    num5()   
    num=5
    disp(num)
    while 1:
      if GPIO.input(2)&GPIO.input(3):      
        time.sleep(0.05)
      elif ~GPIO.input(2)& GPIO.input(3)&(num!=0):    
        wiringpi.pwmWrite(4,75)                
        num=num-1                          
        disp(num)     
        while GPIO.input(3):                
          time.sleep(0.05)                   
        wiringpi.pwmWrite(4,120)           
        time.sleep(2)                       
      elif ~GPIO.input(3)& GPIO.input(2)&(num!=5): 
        wiringpi.pwmWrite(4,75)
        num=num+1
        disp(num)
        while GPIO.input(2):
          time.sleep(0.05)                 
        wiringpi.pwmWrite(4,120)
        time.sleep(2)
        
except KeyboardInterrupt: 
    GPIO.cleanup() # cleanup all GPIO
