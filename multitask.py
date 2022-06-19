import threading  
import time  

def Driving():
	# 10 second
	for i in range(10):
		print('กำลังขับรถอยู่......',i)
		time.sleep(1)



def Metting():
	for i in range(10):
		print('กำลังประชุม....',i)
		time.sleep(0.5)

t1 = time.time()
#########NORMAL######
#Driving()
#Metting()

#####Paraller######
task1 = threading.Thread(target=Driving)
task2 = threading.Thread(target=Metting)

print(time.time())
task1.start()
print(time.time())
task2.start()


task1.join()
task2.join()


t2 = time.time()
print('Time: ',t2-t1)
