import RPi.GPIO as GPIO
import time

#Sleep time (testing only)
icsleep=0.5

#Define Variables - Numbers

DATAIN=16 #DS
LATCH=21  #STCP
CLOCK=20  #SHCP

#Define Variables - Digits

DATAIN_DIGIT=22
LATCH_DIGIT=17
CLOCK_DIGIT=4

#Define Variables - Letters

DATAIN_LETTER=18
LATCH_LETTER=23
CLOCK_LETTER=24

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

digits={"digit1":0x80,
		"digit2":0x40,
		"digit3":0x20,
		"digit4":0x10,
		"digit5":0x08,
		"digit6":0x04,
		"digit7":0x02,
		"digit8":0x01,
}
#Number and Letter Dictionary

numbers={"0":0xFC,
         "1":0x30,
         "2":0xDA,
         "3":0x7A,
         "4":0x36,
         "5":0x6E,
         "6":0xEE,
         "7":0x38,
         "8":0xFE,
         "9":0x3E,
         ".":0x01,
}

letters={
	"M":0x282A,
	"P":0x381A,
	"H":0x3838,
	"f":0x3802,
	"t":0x3A00,
	".":0x40,
	"N":0x68A8,
	"E":0x3A12,
	"W":0x2CA8,
	"S":0x4230,
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
    GPIO.setup(DATAIN_LETTER,GPIO.OUT)
    GPIO.setup(CLOCK_LETTER,GPIO.OUT)
    GPIO.setup(LATCH_LETTER,GPIO.OUT)

    GPIO.output(LATCH,False) #Latch is used to output the saved data
    GPIO.output(CLOCK,False) #Used to shift the value of DATAIN to the register
    GPIO.output(DATAIN,False) #Databit to be shifted into the register
    GPIO.output(DATAIN_DIGIT,False) #Data pin for the second shift register
    GPIO.output(CLOCK_DIGIT,False) #clock pin for the second shift register
    GPIO.output(LATCH_DIGIT,False) #latch pin for the second shift register
    GPIO.output(DATAIN_LETTER,False)
    GPIO.output(CLOCK_LETTER,False)
    GPIO.output(LATCH_LETTER,False)
    
    
def cleanup():
    #Set all leds to off
    writenumber(0)
    writeout()
    writedigit(0)
    writeout_digit()
    
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
   
#Stores a letter "Bit" to the shift register

def shift_letter(input):
   if input == 1:
       input=True
   else:
       input=False

   GPIO.output(DATAIN_LETTER,input)
   GPIO.output(CLOCK_LETTER,GPIO.HIGH)
   GPIO.output(CLOCK_LETTER,GPIO.LOW)
   GPIO.output(DATAIN_LETTER,GPIO.LOW)
   
#Writes the stored segment "Bit" to Displays
    
def writeout():
   #Display LEDs
   GPIO.output(LATCH,GPIO.HIGH)
   GPIO.output(LATCH,GPIO.LOW)
   
   #Writes the stored digit "Bit" to Displays
    
def writeout_digit():
   #Display LEDs
   GPIO.output(LATCH_DIGIT,GPIO.HIGH)
   GPIO.output(LATCH_DIGIT,GPIO.LOW)
   
def writeout_letter():
   #Display LEDs
   GPIO.output(LATCH_LETTER,GPIO.HIGH)
   GPIO.output(LATCH_LETTER,GPIO.LOW)
   
#Writes a character to the shift register

def writenumber(number):
    for x in range(0,8):
        shift((number>>x)%2)
        
def writedigit(number):
    for x in range(0,8):
        shift_digit((number>>x)%2)
        
def writeletter(number):
    for x in range(0,16):
        shift_letter((number>>x)%2)
        
def writexorrange(range):
    #close the chain to have no interrupts while displaying
    character=range[0]&range[-1]
    for x in range:
        character^=x
        writenumber(character)
        writeout()
    for x in range:
        character^=x
        writenumber(character)
        writeout()
    for x in reversed(range):
        character^=x
        writenumber(character)
        writeout()
    for x in reversed(range):
        character^=x
        writenumber(character)
        writeout()

# BEGIN PROGRAM HERE


print("Setup...")
setup()

try:
	
	while True:
		
		writenumber(numbers["1"])
		writedigit(digits["digit1"])
		writeout()
		writeout_digit()
		time.sleep(.001)
		
		writenumber(numbers["2"])
		writedigit(digits["digit2"])
		writeout()
		writeout_digit()
		time.sleep(.001)
		
		writenumber(numbers["3"])
		writedigit(digits["digit3"])
		writeout()
		writeout_digit()
		time.sleep(.001)
		
		writenumber(numbers["4"])
		writedigit(digits["digit4"])
		writeout()
		writeout_digit()
		time.sleep(.001)
		
		writeletter(letters["f"])
		writedigit(digits["digit5"])
		writeout_letter()
		writeout_digit()
		time.sleep(.001)
		
		writeletter(letters["t"])
		writedigit(digits["digit6"])
		writeout_letter()
		writeout_digit()
		time.sleep(.001)
		
		writeletter(letters["."])
		writedigit(digits["digit7"])
		writeout_letter()
		writeout_digit()
		time.sleep(.001)
		
except (KeyboardInterrupt, SystemExit):
    print("Exit...")
    writenumber(0)
    writeout()
    writedigit(0)
    writeout_digit()
    writeletter(0)
    writeout_letter()




