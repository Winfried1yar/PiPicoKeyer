# PICO-Keyer zum Ansteuern der Fernsteuersoftware für IC705
#  DL1YAR November/Dezember 2022
# circuitpython-raspberry_pi_pico-de_DE-8.0.0-alpha.1.uf2
# Punktspeicher hinzugefügt Dezember 2022
# klassische ETM 6.1.2023
# Vband-Keyer 10.1.2023
# Revers-Paddle ohne Speicher 12.1.2 es  te st 023 auswahl am Jumper GPIO15
# Junkers-Mode am 13.1.23 = Junker meets Internett
#
#  cir_CwKeyer_HID-PKTsp_Multi.py
# test 5 



import board
import digitalio
import time
import usb_hid
import analogio

from analogio import AnalogIn
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)

# Anschlüsse 
PKT = digitalio.DigitalInOut(board.GP15)  # Paddle Spitze
PKT.switch_to_input(pull=digitalio.Pull.UP)

STR = digitalio.DigitalInOut(board.GP14)  # Paddle Ring
STR.switch_to_input(pull=digitalio.Pull.UP)

PAD_rev = digitalio.DigitalInOut(board.GP13)  # Punkt-Strich tauschen
PAD_rev.switch_to_input(pull=digitalio.Pull.UP)

ETM = digitalio.DigitalInOut(board.GP9)  # Klassische SquezzeTaste
ETM.switch_to_input(pull=digitalio.Pull.UP)

Vband = digitalio.DigitalInOut(board.GP8)    # Klassische SquezzeTaste
Vband.switch_to_input(pull=digitalio.Pull.UP) # im viruellen InternettQSO

Junkers = digitalio.DigitalInOut(board.GP7)    # Klassische Junkerstaste
Junkers.switch_to_input(pull=digitalio.Pull.UP) # im viruellen InternettQSO

OnBoardLed = digitalio.DigitalInOut(board.LED) # onboard zum testenCw zum OnBoardLed
OnBoardLed.direction = digitalio.Direction.OUTPUT # onboard zum testenCw zum OnBoardLed

Cw_Tx =digitalio.DigitalInOut(board.GP12)  #Transceiver  
Cw_Tx.direction = digitalio.Direction.OUTPUT #

M_Ton = digitalio.DigitalInOut(board.GP16) # Mithoertonausgang
M_Ton.direction = digitalio.Direction.OUTPUT

LED = digitalio.DigitalInOut(board.GP5)  # Status LED
LED.direction = digitalio.Direction.OUTPUT

speed_in = AnalogIn(board.A0)
 
n_cw = 0  #eventuell aendern
CW   = 1  #eventuell aendern
PKT_m = 1 #Punktmerker
STR_m = 1 #Strichmerker
Z_z   = 0 #Zeichenzaehler
Cod   = 0xff #Codemuster
Zp_a   = 0   #Pausenzaehler
speed = 22
SPACE = 0
M_Ton_m = 0 #Merker Mithoerton
M_Ton_d = 0 #Dummy Mithöerton
Ton = 0


def Woab(): #Wortabstand    
    global Zp_a,SPACE
    Pause()
    Zp_a +=1
    if (Zp_a >7):
        #print('  ')
        kbd.send(Keycode.SPACE)
        SPACE = 0
        Zp_a =0

def Bu_a(): #Buchstabenerkennung
    global Z_z,Cod,Pkt_m,Zp_a
    Pause()
    Zp_a = Zp_a +1
    #print('*Code ', Cod,' Zeich ',Z_z,' Zp ', Zp_a,)
    if Zp_a == 3:
        Cod =(Cod &0xFF)        #Begrenzung auf 8Bit
        #print('Bin ', bin(Cod)) #Begrenzung auf 8Bit
        #print('Code ', Cod,' Zeich ',Z_z,' Zp ', Zp_a,)
        if (Cod == 2 ) and (Z_z == 2 ):
            #print('A')
            kbd.send(Keycode.A)
        elif (Cod == 1) and (Z_z == 4 ):
            #print('B')
            kbd.send(Keycode.B)
        elif (Cod == 5) and (Z_z == 4 ):
            #print('C')
            kbd.send(Keycode.C)
        elif (Cod == 1) and (Z_z == 3 ):
            #print('D')
            kbd.send(Keycode.D)
        elif (Cod == 0) and (Z_z == 1 ):
            #print('E')
            kbd.send(Keycode.E)
        elif (Cod == 4) and (Z_z == 4 ):
            #print('F')
            kbd.send(Keycode.F)
        elif (Cod == 3) and (Z_z == 3 ):
            #print('G')
            kbd.send(Keycode.G)
        elif (Cod == 0) and (Z_z == 4 ):
            #print('H')
            kbd.send(Keycode.H)
        elif (Cod == 0) and (Z_z == 2 ):
            #print('I')
            kbd.send(Keycode.I)
        elif (Cod == 14) and (Z_z == 4 ):
            #print('J')
            kbd.send(Keycode.J)
        elif (Cod == 5) and (Z_z == 3 ):
            #print('K')
            kbd.send(Keycode.K)
        elif (Cod == 2) and (Z_z == 4 ):
            #print('L')
            kbd.send(Keycode.L)
        elif (Cod == 3) and (Z_z == 2 ):
            #print('M')
            kbd.send(Keycode.M)
        elif (Cod == 1) and (Z_z == 2 ):
            #print('N')
            kbd.send(Keycode.N)
        elif (Cod == 7) and (Z_z == 3 ):
            #print('O')
            kbd.send(Keycode.O)
        elif (Cod == 6) and (Z_z == 4 ):
            #print('P')
            kbd.send(Keycode.P)
        elif (Cod == 11) and (Z_z == 4 ):
            #print('Q')
            kbd.send(Keycode.Q)
        elif (Cod == 2) and (Z_z == 3 ):
            #print('R')
            kbd.send(Keycode.R)
        elif (Cod == 0) and (Z_z == 3 ):
            #print('S')
            kbd.send(Keycode.S)
        elif (Cod == 1) and (Z_z == 1 ):
            #print('T')
            kbd.send(Keycode.T)
        elif (Cod == 4) and (Z_z == 3 ):
            #print('U')
            kbd.send(Keycode.U)
        elif (Cod == 8) and (Z_z == 4 ):
            #print('V')
            kbd.send(Keycode.V)
        elif (Cod == 6) and (Z_z == 3 ):
            #print('W')
            kbd.send(Keycode.W)
        elif (Cod == 9) and (Z_z == 4 ):
            #print('X')
            kbd.send(Keycode.X)
        elif (Cod == 13) and (Z_z == 4 ):
            #print('Y')
            kbd.send(Keycode.Z)
        elif (Cod == 3) and (Z_z == 4 ):
            #print('Z')
            kbd.send(Keycode.Y)
        elif (Cod == 30) and (Z_z == 5 ):
            #print('1')
            kbd.send(Keycode.ONE)
        elif (Cod == 28) and (Z_z == 5 ):
            #print('2')
            kbd.send(Keycode.TWO)
        elif (Cod == 24) and (Z_z == 5 ):
            #print('3')
            kbd.send(Keycode.THREE)
        elif (Cod == 16) and (Z_z == 5 ):
            #print('4')
            kbd.send(Keycode.FOUR)
        elif (Cod == 0) and (Z_z == 5 ):
            #print('5')
            kbd.send(Keycode.FIVE)
        elif (Cod == 1) and (Z_z == 5 ):
            #print('6')
            kbd.send(Keycode.SIX)   
        elif (Cod == 3) and (Z_z == 5 ):#
            #print('7')
            kbd.send(Keycode.SEVEN)
        elif (Cod == 7) and (Z_z == 5 ):#
            #print('8')
            kbd.send(Keycode.EIGHT)
        elif (Cod == 15) and (Z_z == 5 ):#
            #print('9')
            kbd.send(Keycode.NINE)
        elif (Cod == 31) and (Z_z == 5 ):
            #print('0')
            kbd.send(Keycode.ZERO)   
        elif (Cod == 9) and (Z_z == 5 ):
            #print('/')
            kbd.send(Keycode.SHIFT,Keycode.SEVEN)
        elif (Cod == 42) and (Z_z == 6 ):
            #print('.')
                 kbd.send(Keycode.PERIOD)     
        elif (Cod == 51) and (Z_z == 6 ):
            #print(',')
            kbd.send(Keycode.COMMA)
        elif (Cod == 12) and (Z_z == 6 ):
            #print('?')
            kbd.send(Keycode.SHIFT,Keycode.MINUS)# ?
        elif (Cod == 14) and (Z_z == 5 ):
            #print(';')
            kbd.send(Keycode.SHIFT,Keycode.COMMA)# ;
        elif (Cod == 29) and (Z_z == 5 ):
            #print('!')
            kbd.send(Keycode.SHIFT,Keycode.ONE) # !
        elif (Cod == 20) and (Z_z == 6 ):
            #print('(')
            kbd.send(Keycode.SHIFT,Keycode.NINE) #(
        elif (Cod == 45) and (Z_z == 6 ):
            #print(')')
            kbd.send(Keycode.SHIFT,Keycode.ZERO) #)
        elif (Cod == 7) and (Z_z == 6 ):
            #print(':')
            kbd.send(Keycode.SHIFT,Keycode.PERIOD)# :
        elif (Cod == 17) and (Z_z == 5 ):
            #print('=')
            kbd.send(Keycode.SHIFT,Keycode.ZERO)
        elif (Cod == 1) and (Z_z == 5 ):
            #print('+')
            kbd.send(Keycode.PLUS)
        elif (Cod == 33) and (Z_z == 6 ):
            #print('-')
            ##kbd.send(Keycode.SHIFT,Keycode.FORWARD_SLASH)# -
            kbd.send(Keycode.FORWARD_SLASH)# 
        elif (Cod == 18) and (Z_z == 6 ):
            #print('"')
            kbd.send(Keycode.SHIFT,Keycode.TWO)# "
        elif (Cod == 18) and (Z_z == 5 ):
            #print('ret')    #pspps
            kbd.send(Keycode.RETURN )#Enter
        Z_z = 0
        Cod   = 0 #Codemuster
        Pause()
        Zp_a = Zp_a +1
    return    
       
def Pause():
    global speed,Zp_a,Ton,M_Ton_m
    speed = int((speed_in.value /180))
    #speed = int((speed_in.value /350))  
    while speed > 0:
        time.sleep(0.00072)
        if (M_Ton_m >0) :
            if Ton == 1:
                Ton = 0
            else :
                Ton = 1
        M_Ton.value = Ton
        speed -=1
    Zp_a +=1   
   
     
def Punkt():
    #OnBoardLed.value(CW)
    global Z_z,Cod,PKT_m,Zp_a,SPACE,M_Ton_m
    OnBoardLed.value = True
    if (ETM.value == False):
        Cw_Tx.value = LED.value =True
    if (Vband.value == False):
        kbd.press(Keycode.LEFT_CONTROL)     
    M_Ton_m = 1
    Cod = Cod & ~(1 << Z_z)  #Bit loeschen
    print('Punkt ')
    Z_z +=1
    Pause()
    #OnBoardLed.value(n_cw)
    OnBoardLed.value = False
    Cw_Tx.value = LED.value = False
    if (Vband.value == False):
        kbd.release_all()
    M_Ton_m = 0
    Pause()
    PKT_m = 1
    Zp_a = 1   #Pausenzaehler
    SPACE =1
        
def Strich():
    global Z_z,Cod,PKT_m,Zp_a,SPACE,M_Ton_m
    OnBoardLed.value = True
    if (ETM.value == False):
        Cw_Tx.value = LED.value = True
    if (Vband.value == False):
        kbd.press(Keycode.LEFT_CONTROL)
    M_Ton_m = 1
    Pause()
    if (PKT.value == False and PAD_rev.value == True ):
        PKT_m = 0     #Punktspeicher
    Pause()
    if (PKT.value == False and PAD_rev.value == True ):
        PKT_m = 0
    Pause()
    Cod = Cod |(1 << Z_z) # Bit setzen
    print('Strich ')
    Z_z +=1
    OnBoardLed.value = False
    Cw_Tx.value = LED.value = False
    if (Vband.value == False):
        kbd.release_all()
    M_Ton_m = 0
    Pause()
    Zp_a = 1   #Pausenzaehler
    SPACE = 1

def Key():
    #Junkers meets WWW
    global Ton
    OnBoardLed.value = False
    kbd.release_all()
    while True:
        if PKT.value == False :
            OnBoardLed.value  = True
            kbd.press(Keycode.LEFT_CONTROL)
            if Ton == 1:
                Ton = 0
                M_Ton.value = Ton
                time.sleep(0.001072)
            elif Ton == 0:
                Ton = 1
                M_Ton.value = Ton
                time.sleep(0.001072)
        else:
            OnBoardLed.value = False
            kbd.release_all()


OnBoardLed.value = True
time.sleep(1)
OnBoardLed.value = False
time.sleep(1)
OnBoardLed.value = True
time.sleep(0.51)
while True:
    if Junkers.value == False:
        Key()
    if STR.value == False :
        if PAD_rev.value == False:
           Punkt()
        if PAD_rev.value == True:
            Strich()    
    
    if (PKT.value == False or PKT_m == 0):
        if PAD_rev.value == False:
            Strich()
        if PAD_rev.value == True:    
            Punkt()
    if (ETM.value == True and Vband.value == True):# Bu-decoder
        if (PKT.value and STR.value and (Z_z > 0)):
            Bu_a()
        if (PKT.value and STR.value and (SPACE >0)):    
            Woab()

# s 4 : 4 : e t  i i  est b de dl1yarpsek te i t test 

 #5 h 
