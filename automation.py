
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#GPIO.setmode(GPIO.BCM)

#temperature and humidity sensor(dht11)
import sys
import Adafruit_DHT

while True:
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    humidity, temperature = Adafruit_DHT.read_retry(11, 5)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

#light intensity detector
GPIO.setup(4,GPIO.IN)
 
for i in range(0,5):
    print GPIO.input(4)

#motion detector sensor
GPIO.setup(10, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(10)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(3, 1)  #Turn ON LED
             time.sleep(0.1)
