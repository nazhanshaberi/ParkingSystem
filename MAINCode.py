import RPi.GPIO as GPIO
import wiringpi as wiringpi  
import time

wiringpi.wiringPiSetupGpio()
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
wiringpi.pinMode(4,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(384)   #clock at 50kHz (20us tick)
wiringpi.pwmSetRange(1000)  #range at 1000 ticks (20ms)
wiringpi.pwmWrite(13,120)
GPIO.setup(14, GPIO.OUT) # LED a pin set as output
GPIO.setup(15, GPIO.OUT) # LED b pin set as output
GPIO.setup(18, GPIO.OUT) # LED c pin set as output
GPIO.setup(23, GPIO.OUT) # LED d pin set as output
GPIO.setup(24, GPIO.OUT) # LED e pin set as output
GPIO.setup(25, GPIO.OUT)# LED f pin set as output
GPIO.setup(8, GPIO.OUT) # LED g pin set as output
GPIO.setup(2, GPIO.IN)  # set GPIO 2 as an input for proximity sensor 1. 
GPIO.setup(3, GPIO.IN)  # set GPIO 3 as an input for proximity sensor 2. 
GPIO.setup(4, GPIO.OUT) # set GPIO 4 as an output for servo. 


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

def num0():                  # def=define its define at num0() what it would do
  GPIO.output(14, GPIO.HIGH) # a pin 
  GPIO.output(15, GPIO.HIGH) # b pin 
  GPIO.output(18, GPIO.HIGH) # c pin 
  GPIO.output(23, GPIO.HIGH) # d pin 
  GPIO.output(24, GPIO.HIGH) # e pin 
  GPIO.output(25, GPIO.HIGH) # f pin 
  GPIO.output(8, GPIO.LOW)   # g pin
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
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.LOW) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num4():
  GPIO.output(14, GPIO.LOW) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.LOW) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num5():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.LOW) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin

print("Press CTRL+C to exit the simulation")  # since we are using except KeyboardInterupt, CTRL + C mean "Clear"
try:
    num5()   
    num=5
    disp(num)
    while 1:
      if GPIO.input(2)&GPIO.input(3):       # sensor 1 & sensor 2 are not detected
        time.sleep(0.05)
      elif ~GPIO.input(2)& GPIO.input(3)&(num!=0):    #sensor 1 detect Car enter 
        wiringpi.pwmWrite(4,75)             # 4 ouput for servo; 75 = counterclockwise (90degree) Gate open     
        num=num-1                           # number -1   
        disp(num)     
        while GPIO.input(3):                # sensor 2 detect car 
          time.sleep(0.05)                   
        wiringpi.pwmWrite(4,120)            # 4 ouput for servo; 120 =(90degree) clockwise  Gate close
        time.sleep(2)                       
      elif ~GPIO.input(3)& GPIO.input(2)&(num!=5): # situasi bila kereta nak keluar. sama macam kat atas
        wiringpi.pwmWrite(4,75)
        num=num+1
        disp(num)
        while GPIO.input(2):
          time.sleep(0.05)                 
        wiringpi.pwmWrite(4,120)
        time.sleep(2)
        
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
