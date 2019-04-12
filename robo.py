import RPI.GPIO as gpio
import urllib
import time
from ultrazvocniSenzor import razdalja

# Nastavitev sistema pinov
gpio.setmode(gpio.BOARD)

#Definicija uporabljenih pinov (na razpolago imamo pine: 7, 11, 12, 13, 15, 16, 18, 22)
	#Pini ki poganjajo motorje Robota
MotorLevoNaprej = 7
MotorLevoNazaj = 11
MotorDesnoNaprej =13
MotorDesnoNazaj =15
	#Pini ki berejo podatke iz gumbov namescenih na robota (leva i desna stran zadaj)
GumbDesno = 22
GumbLevo = 18
	#Dwfinicija casa cakanja med ukazi
MoveTime = 1

#Nastavitev pinov za opravljanje definirane naloge ter postavitev izhodnih pinov na gpio.LOW polozaj
def SetUp():
	gpio.setup(MotorLevoNaprej, gpio.OUT)
	gpio.setup(MotorLevoNazaj, gpio.OUT)
	gpio.setup(MotorDesnoNaprej, gpio.OUT)
	gpio.setup(MotorDesnoNazaj, gpio.OUT)
	
	gpio.setup(GumbDesno, gpio.IN)
	gpio.setup(GumbLevo, gpio.IN)
	
	gpio.output(MotorLevoNaprej, gpio.LOW)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.LOW)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
#Funkcije premikanja robota
def Naprej():
	gpio.output(MotorLevoNaprej, gpio.HIGH)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.HIGH)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return
	
def Nazaj():
	gpio.output(MotorLevoNaprej, gpio.LOW)
	gpio.output(MotorLevoNazaj, gpio.HIGH)
	gpio.output(MotorDesnoNaprej, gpio.LOW)
	gpio.output(MotorDesnoNazaj, gpio.HIGH)
	time.sleep(MoveTime)
	return
	
def ZavojL():
	gpio.output(MotorLevoNaprej, gpio.LOW)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.HIGH)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return
	
def ZavojD():
	gpio.output(MotorLevoNaprej, gpio.HIGH)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.LOW)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return

def ObratL():
	gpio.output(MotorLevoNaprej, gpio.LOW)
	gpio.output(MotorLevoNazaj, gpio.HIGH)
	gpio.output(MotorDesnoNaprej, gpio.HIGH)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return
	
def ObratD():
	gpio.output(MotorLevoNaprej, gpio.HIGH)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.LOW)
	gpio.output(MotorDesnoNazaj, gpio.HIGH)
	time.sleep(MoveTime)
	return
	
def End():
	gpio.cleanup()
	return False
	
#Gumb desno aktiven
#	if GPIO.input(GumbDesno) == GPIO.HIGH:
#
#Gumb levo Aktiven
#	if GPIO.input(GumbLevo) == GPIO.HIGH:

SetUp()

program = True
while program:
	f = open("controll.txt", 'r+')

	line = f.readline()
	line = line.strip()
	
	time.sleep(MoveTime)
	
	if(line == "end"):
		program = End()
	
	if(line == "forward"):
	Razd = razdalja()
		if (Razd()>15):
			Naprej()
	
	if(line == "back"):
		Nazaj()
		
	if(line == "left"):
		ZavojL()
	
	if(line == "right"):
		ZavojD()
	
	if(line == "pivotR"):
		ObratD()
	
	if(line == "pivotL"):
		ObratL()
	
	
	f.close