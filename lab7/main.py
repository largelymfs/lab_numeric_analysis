#-*- coding:utf-8 -*-
import equation
def solve_jacobi(A, B, times):
	m = len(A)
	n = len(A[0])
	new = []
	old = []
	for i in range(n):
		old.append(1.0)
		new.append(0.0)

	for k in range(times):
		for i in range(n):
			tmp = 0.0
			for j in range(n):
				if j != i:
					tmp =tmp + float(A[i][j]) * float(old[j])
			tmp = float((B[i] - tmp ))/float(A[i][i])
			new[i] = tmp
		for i in range(n):
			old[i] = new[i]
	return old

def solve_GS(A, B, times):
	m = len(A)
	n = len(A[0])
	new = []
	old = []
	for i in range(n):
		old.append(1.0)
		new.append(0.0)

	for k in range(times):
		for i in range(n):
			tmp = 0.0
			for j in range(n):
				if j > i:
					tmp =tmp + float(A[i][j]) * float(old[j])
				elif j < i:
					tmp =tmp + float(A[i][j]) * float(new[j])		
			tmp = float((B[i] - tmp ))/float(A[i][i])
			new[i] = tmp
		for i in range(n):
			old[i] = new[i]
	return old

def solve_SOR(A, B, omega, times):
	m = len(A)
	n = len(A[0])
	new = []
	old = []
	for i in range(n):
		old.append(1.0)
		new.append(0.0)

	for k in range(times):
		for i in range(n):
			tmp = 0.0
			for j in range(n):
				if j > i:
					tmp =tmp + float(A[i][j]) * float(old[j])
				elif j < i:
					tmp =tmp + float(A[i][j]) * float(new[j])		
			
			tmp = omega * float((B[i] - tmp ))/float(A[i][i])

			new[i] = (1-omega) * old[i]+ tmp
		for i in range(n):
			old[i] = new[i]
	return old

def build(elpson, n, a):
	h = 1.0/float(n)
	elpson = float(elpson)
	a = float(a)
	A = []
	for i in range(n):
		A.append([])
		for j in range(n):
			A[i].append(0.0)

	for i in range(n):
		if i - 1 >= 0:
			A[i][i - 1] = elpson
		if i + 1 < n:
			A[i][i + 1] = elpson + h
		A[i][i] = -(2 * elpson + h)
	B = []
	for i in range(n):
		B.append(a * h * h)
	return A, B

if __name__=="__main__":
	A = [[20, 2, 3],[1, 8, 1],[2, -3, 15]]
	B = [24, 12, 30]
	A, B = build(0.1, 100, 0.5)

	#n = len(A)
	#for i in range(n):
	#	for j in range(n):
	#		print A[i][j],
	#	print
	print solve_jacobi(A, B, 100)[-5:-1]
	print solve_GS(A, B, 100)[-5:-1]
	print solve_SOR(A, B, 0.8, 100)[-5:-1]
	print equation.solve(A, B)[1][-5:-1]