import socket 
from datetime import datetime
import csv
import threading  
serverip_location = '192.168.1.184'
port_location = 9500 
buffsize_location = 4096
serverip = '192.168.1.184'
port = 9000 
buffsize = 4096
############THREADING SERVER###########
plate_dict = {}
# plate_dict = {'1กง9999':['31213215135']}
def locationServer():
	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		server.bind((serverip_location,port_location))
		server.listen(1)
		print('Waiting Client...')

		client, addr = server.accept()
		print('connected from:',addr)

		data = client.recv(buffsize_location).decode('utf-8')
		print('Data from client: ',data)

	    # DATA FROM 4 : data ='check|1กง9999'
		source = data.split('|')[0] # มาจากโปรแกรมฝั่งไหน in/location/out
		plate = data.split('|')[1]

		if source =='check':
			check = plate_dict[plate] 
			text = 'location|'
			for c in check:
				text += c + '|'

			client.send(text.encode('utf-8'))
			client.close()
		else:
			client.close() 

	###########RUN THREAD############
	task = threading.Thread(target=locationServer)
	task.start()

	###########CSV##################
	def writetocsv(data):
		with open('2-car-system-in.csv','a',newline='',encoding='utf-8') as file:
			fw = csv.writer(file)
			fw.writerow(data) # no s is sigle line.append
		print('csv saved')

	#######ADRESS##########
	
	############################ Splitrow#################33

def splitrow(datalist, columns=7):
	    result = []
	    buflist = []
	    for i,t in enumerate(datalist,start=1):
	        if i % columns == 0:
	            buflist.append(t)
	            # print(buflist)
	            result.append(buflist)
	            buflist = []
	        else:
	            buflist.append(t)
	    return result



while True:
	q = input('[1] - get multiple car information\n[2] - get single car information\n[3] - Save car Zone \n[q] - exit\n>>>')
	if q == '1':
		text = 'location|allcar'
	elif q == '2':
		getcar = ('Enter plate code: ')
		text = 'location|{}'.format(getcar)
	elif q == '3':
		plate = input('Enter plate code: ')
		getzone = input('Enter Zone Number : ')
		if len(plate_dict[plate]) == 7:
			# ยังไม่เคยกรอกข้อมูล ข้อมูลจะมี 7 รายการ
			plate_dict[plate].append(getzone)
		else:
			# ถ้าเคยกรอกไปแล้วต้องการเปลี่ยนให้ใช้แบบนี้
			plate_dict[plate][7] = getzone	
	elif q=='q':
		break
	if q!='3':
		#### CONNCET
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		server.connect((serverip,port))
		server.send(text.encode('utf-8'))
		data_server = server.recv(buffsize).decode('utf-8')
		print('Data from Server : ', data_server)
		datalist = data_server.split('|')[1:-1] # [1:-1] remove prefix and fubflic
		for row in splitrow(datalist,7):
			print(row)
			if row[4] not in plate_dict:
				plate_dict[row[4]] = row  # บันทึกข้อมูลของรถเก็บไว้เป็น dict
		server.close()

'''[3]-car-system-location.py
	-client-1.py
	fucution 
	> ดึงข้อมูลรถจาก [1]
	-surver.py
	 > การบันทึกข้อมูลตำแหน่งโซนของรถได้
	 > ส่งข้อมูลไปยัง [4]'''