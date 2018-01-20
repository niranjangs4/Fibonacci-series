# Developer By : NIRANJAN KUMAR G S 
# From : INDIA
# Email : niranjan4@outlook.in
# Updated date : 20/Dec/2017

import matplotlib.pyplot as plt

def fibo():
	c=s[-1]+s[-2]
	s.append(c)
if __name__ == '__main__':
	while True:
		s=[1,1,]
		k=int(input('Enter how many fibina number :'))	#python2
		#k=int(raw_input('Enter how many fibina number :'))	#python3
		for i in range(k):
			fibo()
		print(s[0:len(s)-2])
		plt.plot(s[0:len(s)-2])
		plt.show()
		a= input("Do you want to continue (y/n):") #python2
		#a= raw_input("Do you want to continue (y/n):") #python3
		if a.lower() =='n':
			break
