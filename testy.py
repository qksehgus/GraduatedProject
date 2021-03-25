import RPi.GPIO as GPIO
import time
import os
import pyautogui

print("HC-SR04 Start")

GPIO.setmode(GPIO.BCM)

def turnOn():
        path=os.getcwd()
        os.system('cd{}'.format(os.getcwd()))
        output=os.popen('nmp start').read()
        print(output)
def turnOff():
        pyautogui.hotkey('ctrl','q')

GPIO_TRIGGER=17
GPIO_ECHO=18
GPIO_LIGHT=27




GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(GPIO_LIGHT,GPIO.OUT)

try:
    while True:
        GPIO.output(GPIO_TRIGGER,False)
        time.sleep(0.5)

        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        elapsed=stop-start
        
        distance=elapsed*17000
        distance=round(distance,2)
        
        if distance<=10:
                GPIO.output(GPIO_LIGHT,1)
                trunOn()
        else:
                
                GPIO.output(GPIO_LIGHT,0)
                trunOff()
        
        print("Distance =",distance,"cm")

except KeyboardInterrupt:
    print("end")
    GPIO.cleanup()
