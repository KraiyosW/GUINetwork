import socket 
from datetime import datetime
import csv
def writetocsv(data):
	with open('2-car-system-in.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data) # no s is sigle line.append
	print('csv saved')
#######ADRESS##########
serverip = '192.168.1.184'
port = 9500 
buffsize = 4096


while True:

	text = 'check|'

	q = input('Enter Plate No. : ')
	text += q 
	#### CONNCET
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(text.encode('utf-8'))
	data_server = server.recv(buffsize).decode('utf-8')
	print('Data from Server : ', data_server)
	data_list = data_server.split('|')
	print('Your car zone: ',data_list[-2])
	server.close()
	print('--------------------------')



'''[4]-car-system-check.py
	- client-3.py
	fucution 
	 - ดึงข้อมูลรถจาก [3]
	 - ดึงข้อมูลตำแหน่งโซนจาก [3]
############'''