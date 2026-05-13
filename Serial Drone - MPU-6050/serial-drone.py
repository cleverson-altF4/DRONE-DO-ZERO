import serial
from time import sleep

arduino = serial.Serial('/dev/ttyUSB0', 9600)


while True:
    dado = arduino.readline().decode("utf-8").strip()
    print(dado)
    sleep(1)