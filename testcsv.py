import csv 

def writetocsv(data):
	with open('2-car-system-in.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data) # no s is sigle line.append
	print('csv saved')

