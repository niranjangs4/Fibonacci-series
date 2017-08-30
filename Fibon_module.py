import matplotlib.pyplot as plt

def fibo():
	c=s[-1]+s[-2]
	s.append(c)
if __name__ == '__main__':
	while True:
		s=[1,1,]
		k=int(input('Enter how many fibina number :'))
		for i in range(k):
			fibo()
		print(s)
		plt.plot(s)
		plt.show()
		a= input("Do you want to continue (y/n):")
		if a=='n':
			break
