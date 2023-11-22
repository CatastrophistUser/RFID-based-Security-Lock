# Import necessary libraries
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import Adafruit_CharLCD as LCD

# Define GPIO pins connected to the keypad
L1 = 13
L2 = 19
L3 = 26
L4 = 7
C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Define GPIO pin connected to the buzzer
buzzer = 17

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize RFID reader
reader = SimpleMFRC522()

# Initialize password
password = '1234'
password_int = ''

# Function to read a line of input from the keypad
def readLine(line, characters):
    global inputs
    GPIO.output(line, GPIO.HIGH)
    if (line == L4):
        if(GPIO.input(C1) == 1):
            inputs = ''
            lcd.clear()
        if(GPIO.input(C3) == 1):
            inputs = ''
            lcd.clear()
        if(GPIO.input(C2) == 1):
            inputs = inputs + characters[1]
            lcd.message(characters[1])
        if(GPIO.input(C4) == 1):
            lcd.message('Please scan key')
            keycard()
    else:
        if(GPIO.input(C1) == 1):
            inputs = inputs + characters[0]
            lcd.message(characters[0])
        if(GPIO.input(C2) == 1):
            inputs = inputs + characters[1]
            lcd.message(characters[1])
        if(GPIO.input(C3) == 1):
            inputs = inputs + characters[2]
            lcd.message(characters[2])
        if(GPIO.input(C4) == 1):
            if(line == L3):
                inputs = ''
                lcd.clear()
            if(line == L2):
                lcd.clear()
                chepass()
            if(line == L1):
                lcd.clear()
                repassword()
    GPIO.output(line, GPIO.LOW)

# Main loop
try:
    while True:
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.3)
        
except KeyboardInterrupt:
    print("\nApplication stopped!")