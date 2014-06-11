#-*- coding:utf-8 -*-
#lab 3
from equation import solve
from matplotlib import pyplot as plt

def OLS(n, x, y):
	A = []
	m = len(x)
	if m!=len(y):
		return None
	for i in range(n + 1):
		A.append([])
		for j in range(n + 1):
			if i <= j:
				tmp = 0.0
				for p in range(m):
					#for q in range(m):
					tmp += (float(x[p]) ** i) * (float(x[p]) ** j)
				A[i].append(tmp)
			else:
				A[i].append(A[j][i])
	B = []
	for i in range(n+1):
		tmp = 0.0
		for p in range(m):
			#for q in range(m):
			tmp += (float(x[p]) ** i) * y[p]
		B.append(tmp)
	flag, answer = solve(A, B)
	return answer

if __name__=="__main__":
	x = [20, 25, 30, 35, 40, 45, 50, 55, 60]
	y = [805, 985, 1170, 1365, 1570, 1790, 2030, 2300, 2610]
	a = OLS(3, x, y)
	f = []
	for i in range(len(x)):
		tmp = 1.0
		tmp_f = 0.0
		for j in range(len(a)):
			tmp_f += tmp * a[j]
			tmp *= x[i]
		f.append(tmp_f)
	print "Answer : ","\t",
	for i in range(len(a)):
		print i,"\t",
	print
	print "\t",
	for i in range(len(a)):
		print a[i],"\t",
	print
	print "Estimation\t\t Actual Value\t\t ERROR"
	sum = 0.0
	for i in range(len(y)):
		print f[i],"\t\t",y[i],"\t\t",abs(f[i]-y[i])
		sum += abs(f[i]-y[i])**2
	print "TOTAL ERROR : ",sum

	plt.plot(x, y,'r.',label="x-y")
	plt.plot(x, f, 'g',label="x-f")
	plt.legend()
	plt.show()