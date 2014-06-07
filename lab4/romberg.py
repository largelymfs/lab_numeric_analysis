#-*- coding: utf-8-*-
import math

def f_1(x):
	return 1.0/float(x)
def f_2(x):
	return 1.0/(1.0+float(x)*float(x))

def cal(a, b, n, f):
	h = float(b - a) / float(n)
	s = f(a) + f(b)
	now = a + h
	while abs(b-now) > 0.0001:
		s += 2 * f(now)
		now += h
	s = s * h / 2.0
	return s

def romberg(a, b, n, e, f):
	t = []
	line = 0
	now_n = n
	while True:
		tmp_s = []
		tmp_s.append(cal(a, b, now_n, f))
		#romberg
		base = 1
		for i in range(line):
			base *= 4
			tmp_s.append((base * tmp_s[i] - t[line-1][i])/float(base-1))
		
		t.append(tmp_s)
		if line!=0:
			if abs(t[line][line] - t[line - 1][line - 1]) < e:
				break
		line += 1
		now_n *= 2
		
	return t[line][line]

if __name__=="__main__":
	f1 = romberg(1, 2, 10, 0.5 * 1e-8, f_1)
	f2 = 4.0 * romberg(0, 1, 10, 0.5 * 1e-8, f_2)
	y1 = math.log(2)
	y2 = math.pi
	t1 = abs(y1 - f1)
	t2 = abs(y2 - f2)
	print "=============ROMBERG============="
	print "For Problem 1, we have : ", f1, ",answer is : ", y1, ",delta is ", t1
	print "For Problem 1, we have : ", f2, ",answer is : ", y2, ",delta is ", t2
	
			