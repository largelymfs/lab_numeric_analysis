import copy

#A Tool using by experiment
#solve the equation AX=B
def solve(now_A, now_B):
	A = copy.deepcopy(now_A)
	B = copy.deepcopy(now_B)

	m = len(A)
	if m==0 or m!=len(B):
		return False, None
	n = len(A[0])
	if m!=n :
		return True, None
	
	for i in range(n):
		max_id = i
		for j in range(i, n):
			if abs(A[j][i]) > abs(A[max_id][i]):
				max_id = j

		for j in range(i, n):
			tmp = A[i][j]
			A[i][j] = A[max_id][j]
			A[max_id][j] = tmp

		tmp = B[i]
		B[i] = B[max_id]
		B[max_id] = tmp

		#change the A(i,i) to 1
		delta = float(A[i][i])
		if delta==0:
			return True, None
		for j in range(i, n):
			A[i][j] /= delta
		B[i] /= delta
		#change A(i+..,i) to 0
		for j in range(i+1, n):
			delta = A[j][i]
			for k in range(i, n):
				A[j][k] += float(-delta) * A[i][k]
			B[j] += float(-delta) * B[i]

	x = [0.0 for i in range(n)]
	for i in range(n):
		now_line = n - i - 1
		tmp = float(B[now_line])
		for j in range(now_line+1, n):
			tmp -= x[j] * A[now_line][j]
		x[now_line] = tmp
	return True, x

#check the result of the solution
def check(A, x, B):
	m = len(A)
	n = len(A[0])
	if len(x)!=n or len(B)!=m:
		return False
	for i in range(m):
		tmp = 0.0
		for j in range(n):
			tmp += x[j] * A[i][j]
		if abs(tmp-float(B[i]))>0.001:
			return False
	return True

##check program
if __name__=="__main__":
	A=[[2,3,5.0],[-4.0,5,6],[2,4,6]]
	B=[4, 5,87]
	#A = [[1, 0],[0,1]]
	#B = [1, 2]
	print solve(A, B)
	print check(A, solve(A, B)[1], B)
