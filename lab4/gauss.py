#-*- coding:utf-8 -*-
import math
#for 1/x^2
def f_1(x):
	return 1.0/float(x)

def f_2(x):
	return 1.0/(float(x)*float(x)+1.0)

def gauss(a, b, e, f):
	n = int((b - a) / e) + 1
	h = float(b - a)/float(n)
	base = h/(2 * math.sqrt(3.0))
	now = a
	s = 0.0
	for i in range(n):
		s += (f(now + 0.5 * h + base) + f(now + 0.5 * h - base))
		now += h
	s = s * h /2.0
	return s
if __name__=="__main__":
	h = 0.0308007
	f1 = gauss(1, 2, h, f_1)
	y1 = math.log(2)
	f2 = 4.0 * gauss(0, 1, h, f_2)
	y2 = math.pi
	print "=============GAUSS============="
	print "For Problem 1, we have : ", f1, ",answer is : ", y1
	print  "delta is ", abs(y1 - f1)
	print "For Problem 1, we have : ", f2, ",answer is : ", y2 
	print "delta is ", abs(y2 - f2)
	