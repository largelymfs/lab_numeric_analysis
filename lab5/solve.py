#-*- coding:utf-8 -*-

def f1(x):
	return (-1 + 3 * x - x * x + 2 * x * x * x);
def g1(x):
	return (3 - 2 * x +6 * x * x)
def f2(x):
	return (x * x * x - x - 1.0)
def g2(x):
	return (3 * x * x)


def middle(a, b, e, f):
	step = 0
	left = a
	right = b
	print "Step " , 0, "LEFT : ", left, "RIGHT : ", right, "DELTA : ", right-left

	while right - left > e:
		middle = (left + right) / 2.0
		f_left = f(left)
		f_middle = f(middle) 
		if f_middle * f_left < 0:
			right = middle
		else:
			left = middle
		step += 1
		print "Step " , step, "LEFT : ", left, "RIGHT : ", right, "DELTA : ", right-left
	print "THE ANSWER IS : ", left
	
def newton(a, e, f, g):
	now_x = float(a)
	C = 1.0
	step = 0
	while True:
		old_x = now_x
		gra = g(old_x)
		if abs(gra)<0.000001:
			gra = 0.000001
		now_x = old_x - (f(old_x)) / gra
		step += 1
		print "Step " , step, "OLD X : ", old_x, "NEW_X : ", now_x,
		if abs(now_x) < C:
			delta = abs(now_x - old_x)
		else:
			delta = abs(now_x - old_x) / abs(now_x)
		print "DELTA : ", delta
		if delta < e:
			break
	print "THE ANSWER IS : ", now_x 

def update1(x):
	return ((float(x)+1.0)/2.0)**(1.0/3.0)
def update2(x):
	return (2 * float(x) *float(x) * float(x) -1.0)

def stop_point(x, f, n):
	step = 0
	now = x
	for i in range(n):
		print "Step ", i + 1,
		old = now
		now = f(old)
		print "OLD :\t", old, "NEW :\t", now


if __name__=="__main__":
	print "======================PROBLEM 1======================"
	middle(0, 10, 1e-6, f1)
	newton(0, 1e-6, f1, g1)
	print "======================PROBLEM 2======================"
	stop_point(0.0, update1, 10)
	stop_point(0.0, update2, 10)
	print "====================================================="
	newton(0, 1e-6, f2, g2)
	newton(1.5, 1e-6, f2, g2)
	
	