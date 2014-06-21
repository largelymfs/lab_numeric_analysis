def mult(A, B):
	m = len(A)
	n = len(A[0])
	if n != len(B):
		return None
	p = len(B[0])
	res = []
	for i in range(m):
		res.append([])
		for j in range(p):
			res[i].append(0)

	for i in range(m):
		for j in range(p):
			for k in range(n):
				res[i][j] += (A[i][k] * B[k][j])
	return res

if __name__=="__main__":
	A = [[1, 0],[0, 1]]
	B = [[2, 3],[4, 5]]
	print mult(A, B)