import RPi.GPIO as GPIO
import time

#Sleep time (testing only)
icsleep=0.5

#Define Variables - Segments

DATAIN=16 #DS
LATCH=21  #STCP
CLOCK=20  #SHCP

#Define Variables - Digits

DATAIN_DIGIT=19
LATCH_DIGIT=13
CLOCK_DIGIT=6

#Define all LEDs

led1=0x80 #10000000
led2=0x40 #01000000
led3=0x20 #00100000
led4=0x10 #00010000
led5=0x08 #00001000
led6=0x04 #00000100
led7=0x02 #00000010
led8=0x01 #00000001

#Define Digits

digit1=0x80 #10000000
digit2=0x40 #01000000

#Number and Letter Dictionary

letter={"0":0xFC,
        "1":0x30,
        "2":0xDA,
        "3":0x7A,
        "4":0x36,
        "5":0x6E,
        "6":0xEE,
        "7":0x38,
        "8":0xFE,
        "9":0x3E,
        "a":0xBE,
        "b":0xE6,
        "c":0xCC,
        "d":0xF2,
        "e":0xCE,
        "f":0x8E,
        "g":0x7E,
        "h":0xB6,
        "i":0x30,
        "j":0xF0,
        "l":0xC4,
        "n":0xBC,
        "o":0xFC,
        "p":0x9E,
        "s":0x6E,
        "t":0x38,
        "u":0xF4,
        "x":0xB4,
        "y":0x76,
        "z":0xDE
}

#Setup and Cleanup functions

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setup(DATAIN,GPIO.OUT)
    GPIO.setup(CLOCK,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)
    GPIO.setup(DATAIN_DIGIT,GPIO.OUT)
    GPIO.setup(CLOCK_DIGIT,GPIO.OUT)
    GPIO.setup(LATCH_DIGIT,GPIO.OUT)

    GPIO.output(LATCH,False) #Latch is used to output the saved data
    GPIO.output(CLOCK,False) #Used to shift the value of DATAIN to the register
    GPIO.output(DATAIN,False) #Databit to be shifted into the register
    GPIO.output(DATAIN_DIGIT,False)
    GPIO.output(CLOCK_DIGIT,False)
    GPIO.output(LATCH_DIGIT,False)
    
def cleanup():
    #Set all leds to off
    writenumber(0)
    writeout()
    
# Stores a segment "Bit" to the shift register

def shift(input):
   if input == 1:
       input=True
   else:
       input=False

   GPIO.output(DATAIN,input)
   GPIO.output(CLOCK,GPIO.HIGH)
   GPIO.output(CLOCK,GPIO.LOW)
   GPIO.output(DATAIN,GPIO.LOW)
   
 # Stores a digit "Bit" to the shift register

def shift_digit(input):
   if input == 1:
       input=True
   else:
       input=False

   GPIO.output(DATAIN_DIGIT,input)
   GPIO.output(CLOCK_DIGIT,GPIO.HIGH)
   GPIO.output(CLOCK_DIGIT,GPIO.LOW)
   GPIO.output(DATAIN_DIGIT,GPIO.LOW)
   
#Writes the stored segment "Bit" to Displays
    
def writeout():
   #Display LEDs
   GPIO.output(LATCH,GPIO.HIGH)
   #Display for "icsleep" Ms
   time.sleep(icsleep)
   GPIO.output(LATCH,GPIO.LOW)
   
   #Writes the stored digit "Bit" to Displays
    
def writeout_digit():
   #Display LEDs
   GPIO.output(LATCH_DIGIT,GPIO.HIGH)
   #Display for "icsleep" Ms
   time.sleep(icsleep)
   GPIO.output(LATCH_DIGIT,GPIO.LOW)
   
#Writes a character to the shift register

def writenumber(number):
    for x in range(0,8):
        shift((number>>x)%2)
        
def writedigit(input):
    for x in range(0,8):
        shift((input>>x)%2)

# BEGIN PROGRAM HERE


print("Setup...")
setup()

try:
	
	while True:
		
		writenumber(letter["d"])
		writedigit(digit1)
		writeout()
		writeout_digit()
		time.sleep(1)
		
		writenumber(letter["h"])
		writedigit(digit2)
		writeout()
		writeout_digit()
		time.sleep(1)
		
except (KeyboardInterrupt, SystemExit):
    print("Exit...")
    writenumber(0)
    writeout()




