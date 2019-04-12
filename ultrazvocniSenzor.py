import RPI.GPIO as gpio
import time

	#Pina ki sluzita za upravljanje senzorja razdalje
SenzorIzhod = 12
SenzorVhod = 16
	#Funkcija za izracun razdalje
def razdalja ():
	try:
		#Nastavitev pinov ter plosce
		gpio.setmode(gpio.BOARD)
		gpio.setup(SenzorIzhod, gpio.OUT)
		gpio.setup(SenzorVhod, gpio.IN)
		#Postavitev Prozilnega pina na izklopljeno stanje
		gpio.output(SenzorIzhod,gpio.LOW)
		
		#Zapis casov ob posiljanj signala ter sprejemanju signala
		while gpio.input(SenzorVhod) == gpio.LOW:
			nosignal = time.time()

		while gpio.input(SenzorVhod) == gpio.HIGH:
			signal = time.time()

		#izracun casa ki ga potrebuje signal
		cas = signal - nosignal
		#Izracun razdalje iz casa ter konstantne hitrosti
		razdal = cas/0.000058 #Razdalja v CM
		#Pociscenje definiranih pinov
		gpio.cleanup()
		#Vrnitev razdalje
		return razdal
	except:
		gpio.cleanup()
		return 100
	
print razdalja()