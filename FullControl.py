import RPI.GPIO as gpio
import urllib
import time
from ultrazvocniSenzor import razdalja
import random

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
CasPremika = 0.03

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
def Naprej(MoveTime):
	gpio.output(MotorLevoNaprej, gpio.HIGH)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.HIGH)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return
	
def Nazaj(MoveTime):
	gpio.output(MotorLevoNaprej, gpio.LOW)
	gpio.output(MotorLevoNazaj, gpio.HIGH)
	gpio.output(MotorDesnoNaprej, gpio.LOW)
	gpio.output(MotorDesnoNazaj, gpio.HIGH)
	time.sleep(MoveTime)
	return
	
def ZavojL(MoveTime):
	gpio.output(MotorLevoNaprej, gpio.LOW)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.HIGH)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return
	
def ZavojD(MoveTime):
	gpio.output(MotorLevoNaprej, gpio.HIGH)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.LOW)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return

def ObratL(MoveTime):
	gpio.output(MotorLevoNaprej, gpio.LOW)
	gpio.output(MotorLevoNazaj, gpio.HIGH)
	gpio.output(MotorDesnoNaprej, gpio.HIGH)
	gpio.output(MotorDesnoNazaj, gpio.LOW)
	time.sleep(MoveTime)
	return
	
def ObratD(MoveTime):
	gpio.output(MotorLevoNaprej, gpio.HIGH)
	gpio.output(MotorLevoNazaj, gpio.LOW)
	gpio.output(MotorDesnoNaprej, gpio.LOW)
	gpio.output(MotorDesnoNazaj, gpio.HIGH)
	time.sleep(MoveTime)
	return
	#Funkcija ki porise vrednosti na GPIO pinih ter vrne vrednost "false" za konec programa
def End():
	gpio.cleanup()
	return False

SetUp()

def preveriSpredaj():
	Razd = razdalja()
	if(Razd<=15):
		Zad=preveriZadaj();
		if (zadaj == "NiOvire"):
			Nazaj(CasPremika)
		if (zadaj == "OviraZadaj"):
			ObratL(CasPremika)
			preveriSpredaj()
			ObratD(CasPremika)
		if (zadaj == "OviraDesno"):
			ZavojL(CasPremika)
		if (zadaj == "OviraLevo"):
			ZavojD(CasPremika)
			
def preveriZadaj():
	LokacijaOvire = "NiOvire"
	if GPIO.input(GumbDesno) == GPIO.HIGH && GPIO.input(GumbLevo) == GPIO.HIGH:
		LokacijaOvire = "OviraZadaj"
	elif GPIO.input(GumbDesno) == GPIO.HIGH:
		LokacijaOvire = "OviraDesno"
	elif GPIO.input(GumbLevo) == GPIO.HIGH:
		LokacijaOvire = "OviraLevo"
	return LokacijaOvire
	
program = True
while program:
	i=0
	f = open("controll.txt", 'r+')
	line = f.readline()
	line = line.strip()
	if(line == "End"):
		program = End()
	if i == 20:
		progra = End()
		
	Rand=random.radnrange(0,6)
	for y in range(30)
		if Rand == 0:
			preveriSpredaj()
			Naprej(CasPremika)
		elif Rand == 1:
			zadaj=preveriZadaj()
			if (zadaj == "NiOvire"):
				Nazaj(CasPremika)
		elif Rand == 2:
			preveriSpredaj()
			ZavojL(CasPremika)
		elif Rand == 3:
			preveriSpredaj()
			ZavojD(CasPremika)
		elif Rand == 4:
			ObratL(CasPremika)
		elif Rand == 5:
			ObratD(CasPremika)
	i=i+1