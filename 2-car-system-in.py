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
port = 9000 
buffsize = 4096


while True:
	

	info ={'brand':{'q':'Brand: ','value':''},
			'color':{'q':'Color: ','value':''},
			'plate':{'q':'Plate ','value':''},
			'card':{'q':'Card: ','value':''}}
	timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# data = input('Send to Server: ')
	for k,v in info.items():
		d = input(v['q'])
		info[k]['value'] = d

	text = 'in|' #in| is prefix from car-system-in
	print(info)

	for v in info.values():
		text += v['value'] + '|'

	text += timestamp

	print(text)

	writetocsv(text.split('|'))

	#### CONNCET
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(text.encode('utf-8'))
	data_server = server.recv(buffsize).decode('utf-8')
	print('Data from Server : ', data_server)
	server.close()
	print('---------------------')





































'''[2]-car-system-in.py
	-client-1.py
	function
	- เวลาเข้า
	- รถ ยี่ห้อ สี ทะเบียน
	- ส่งไปหา [1]
	- บันทึกลงใน csv ตัวเอง'''