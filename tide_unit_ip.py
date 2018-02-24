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

#Define Variables - LEDs [Wave Rating]
DATAIN_LED=6
LATCH_LED=13
CLOCK_LED=19

#Define Variables - Title
DATAIN_TITLE=26
LATCH_TITLE=12
CLOCK_TITLE=25

#Define all LEDs

led1=0x80 #10000000
led2=0x40 #01000000
led3=0x20 #00100000
led4=0x10 #00010000
led5=0x08 #00001000
led6=0x04 #00000100
led7=0x02 #00000010
led8=0x01 #00000001

#Digit Dictionary

digits={"digit1":0x8000,
		"digit2":0x4000,
		"digit3":0x2000,
		"digit4":0x1000,
		"digit5":0x0800,
		"digit6":0x0400,
		"digit7":0x0200,
		"digit8":0x0100,
		"digit9":0x80,
		"digit10":0x40,
		"digit11":0x20,
		"digit12":0x10,
		"digit13":0x08,
		"digit14":0x04,
		"digit15":0x02,
		"digit16":0x01,
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
	"S":0x4232,
}

rating={
	"1":0x80,
	"2":0xC0,
	"3":0xE0,
	"4":0xF0,
	"5":0xF8,
}

title={
	"G":0x7C8282925E,
}

#Setup and Cleanup functions

def setup():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DATAIN,GPIO.OUT)
    GPIO.setup(CLOCK,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)
    GPIO.setup(DATAIN_DIGIT,GPIO.OUT)
    GPIO.setup(CLOCK_DIGIT,GPIO.OUT)
    GPIO.setup(LATCH_DIGIT,GPIO.OUT)
    GPIO.setup(DATAIN_LETTER,GPIO.OUT)
    GPIO.setup(CLOCK_LETTER,GPIO.OUT)
    GPIO.setup(LATCH_LETTER,GPIO.OUT)
    GPIO.setup(DATAIN_LED,GPIO.OUT)
    GPIO.setup(CLOCK_LED,GPIO.OUT)
    GPIO.setup(LATCH_LED,GPIO.OUT)
    GPIO.setup(DATAIN_TITLE,GPIO.OUT)
    GPIO.setup(LATCH_TITLE,GPIO.OUT)
    GPIO.setup(CLOCK_TITLE,GPIO.OUT)

    GPIO.output(LATCH,False) #Latch is used to output the saved data
    GPIO.output(CLOCK,False) #Used to shift the value of DATAIN to the register
    GPIO.output(DATAIN,False) #Databit to be shifted into the register
    GPIO.output(DATAIN_DIGIT,False) #Data pin for the second shift register
    GPIO.output(CLOCK_DIGIT,False) #clock pin for the second shift register
    GPIO.output(LATCH_DIGIT,False) #latch pin for the second shift register
    GPIO.output(DATAIN_LETTER,False)
    GPIO.output(CLOCK_LETTER,False)
    GPIO.output(LATCH_LETTER,False)
    GPIO.output(DATAIN_LED,False)
    GPIO.output(CLOCK_LED,False)
    GPIO.output(LATCH_LED,False)
    GPIO.output(DATAIN_TITLE,False)
    GPIO.output(LATCH_TITLE,False)
    GPIO.output(CLOCK_TITLE,False)
    
    clear()
    
def clear():
	writenumber(0)
	writeout()
	writeletter(0)
	writeout_letter()
	writedigit(0)
	writeout_digit()
	writeled(0)
	writeout_led()
	writetitle1(0)
	writeout_title
    

# Stores a Title "Bit" to the shift register

def shift(input):
   if input == 1:
       input=True
   else:
       input=False

   GPIO.output(DATAIN,input)
   GPIO.output(CLOCK,GPIO.HIGH)
   GPIO.output(CLOCK,GPIO.LOW)
   GPIO.output(DATAIN,GPIO.LOW)

def shift_title(input):
   if input == 1:
       input=True
   else:
       input=False

   GPIO.output(DATAIN_TITLE,input)
   GPIO.output(CLOCK_TITLE,GPIO.HIGH)
   GPIO.output(CLOCK_TITLE,GPIO.LOW)
   GPIO.output(DATAIN_TITLE,GPIO.LOW)
   
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
  
def shift_led(input):
   if input == 1:
       input=True
   else:
       input=False

   GPIO.output(DATAIN_LED,input)
   GPIO.output(CLOCK_LED,GPIO.HIGH)
   GPIO.output(CLOCK_LED,GPIO.LOW)
   GPIO.output(DATAIN_LED,GPIO.LOW) 


#Writes the stored segment "Bit" to Displays
    
def writeout():
   #Display LEDs
   GPIO.output(LATCH,GPIO.HIGH)
   GPIO.output(LATCH,GPIO.LOW)
   
def writeout_title():
   #Display LEDs
   GPIO.output(LATCH_TITLE,GPIO.HIGH)
   GPIO.output(LATCH_TITLE,GPIO.LOW)
   
#Writes the stored digit "Bit" to Displays

def writeout_digit():
   #Display LEDs
   GPIO.output(LATCH_DIGIT,GPIO.HIGH)
   GPIO.output(LATCH_DIGIT,GPIO.LOW)
   
def writeout_letter():
   #Display LEDs
   GPIO.output(LATCH_LETTER,GPIO.HIGH)
   GPIO.output(LATCH_LETTER,GPIO.LOW)
   
def writeout_led():
   #Display LEDs
   GPIO.output(LATCH_LED,GPIO.HIGH)
   GPIO.output(LATCH_LED,GPIO.LOW)
   
#Writes a character to the shift register

def writenumber(number):
    for x in range(0,8):
        shift((number>>x)%2)
        
def writedigit(number):
    for x in range(0,16):
        shift_digit((number>>x)%2)
        
def writeletter(number):
    for x in range(0,16):
        shift_letter((number>>x)%2)
        
def writeled(number):
    for x in range(0,8):
        shift_led((number>>x)%2)
        
#Write column bytes to led array shift register        

def writetitle1(number):
    for x in range(1,8):
        shift_title((number>>x)%2)

def writetitle2(number):
    for x in range(9,16):
        shift_title((number>>x)%2)
        
def writetitle3(number):
    for x in range(17,24):
        shift_title((number>>x)%2)
        
def writetitle4(number):
    for x in range(25,32):
        shift_title((number>>x)%2)
        
def writetitle5(number):
    for x in range(33,40):
        shift_title((number>>x)%2)
        
def printtitle(number):
	
	writetitle1(number)
	writedigit(digits["digit8"])
	writeout_title()
	writeout_digit()
	clear()
	
	writetitle2(number)
	writedigit(digits["digit9"])
	writeout_title()
	writeout_digit()
	clear()
	
	writetitle3(number)
	writedigit(digits["digit10"])
	writeout_title()
	writeout_digit()
	clear()
	
	writetitle4(number)
	writedigit(digits["digit11"])
	writeout_title()
	writeout_digit()
	clear()
	
	writetitle5(number)
	writedigit(digits["digit12"])
	writeout_title()
	writeout_digit()
	clear()

        

# BEGIN PROGRAM HERE


print("Setup...")
setup()

try:
	
	while True:
		
		writenumber(numbers["1"])
		writedigit(digits["digit1"])
		writeout()
		writeout_digit()
		clear()
		
		writenumber(numbers["."])
		writedigit(digits["digit2"])
		writeout()
		writeout_digit()
		clear()
		
		writenumber(numbers["5"])
		writedigit(digits["digit3"])
		writeout()
		writeout_digit()
		clear()
		
		writenumber(numbers["7"])
		writedigit(digits["digit4"])
		writeout()
		writeout_digit()
		clear()
		
		writeletter(letters["f"])
		writedigit(digits["digit5"])
		writeout_letter()
		writeout_digit()
		clear()
		
		writeletter(letters["t"])
		writedigit(digits["digit6"])
		writeout_letter()
		writeout_digit()
		clear()
		
		writeletter(letters["."])
		writedigit(digits["digit7"])
		writeout_letter()
		writeout_digit()
		clear()
		
		writeled(rating["4"])
		writeout_led()
		clear()
		
		
		printtitle(title["G"])
		
except (KeyboardInterrupt, SystemExit):
    print("Exit...")
    writenumber(0)
    writeout()
    writedigit(0)
    writeout_digit()
    writeletter(0)
    writeout_letter()




