#-*- coding:utf-8 -*-
import math
#for 1/x^2
def f_1(x):
	return 1.0/float(x)

def f_2(x):
	return 1.0/(float(x)*float(x)+1.0)

def cal(a, b, h, f):
	n = int((b - a) / h) + 1
	h = float((b-a))/float(n)
	#for the point a, b
	s = f(a)+f(b)
	now = a + h
	while abs(now - b)>0.0001:
		s += 2 * f(now) + 4 * f(now - 0.5 * h)
		now += h
	s += 4 * f(b - 0.5 * h)
	s = s * h / 6.0
	return s

if __name__=="__main__":
	h = 0.0278316
	f1 = cal(1, 2, h, f_1)
	f2 = 4.0 * cal(0, 1, h, f_2)
	y1 = math.log(2)
	y2 = math.pi
	print "=============SIMPSON============="
	print "For Problem 1, we have : ", f1, ",answer is : ", y1, ",delta is ", abs(y1 - f1)
	print "For Problem 1, we have : ", f2, ",answer is : ", y2, ",delta is ", abs(y2 - f2)
	