from tqdm import tqdm
import math
import turtle

'''
outside func. state:
pd = True
xdeg = 0
xpos = xpos
'''
class Tchar:

	turtle = None

	def __init__(self):
		self.turtle = turtle.Turtle()

	def next(self, xwidth = 100, xdist = 10):
		self.turtle.pu()
		self.turtle.fd(xwidth + xdist)
		self.turtle.pd()

	def square(self, xheight = 100, xwidth = 80, xdeg = 0):
		for i in range(2):
			self.turtle.fd(xwidth)
			self.turtle.rt(90)
			self.turtle.fd(xheight)
			self.turtle.rt(90)

	def half_oval(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		state_heading = self.turtle.heading()
		delta_h = (xheight * 0.5) / sum([i for i in range(1, accuracy + 1)])
		delta_w = (xwidth / 200 * 191) / sum([i for i in range(1, accuracy + 1)])
		sub_h = 0
		sub_w = delta_w * accuracy
		next_deg = 0
		prev_deg = 0
		for i in range(1, accuracy + 1):
			dist = math.sqrt(sub_h ** 2 + sub_w ** 2)
			self.turtle.rt(next_deg - prev_deg)
			self.turtle.fd(dist)
			prev_deg = next_deg
			sub_h = delta_h * i
			sub_w = delta_w * (accuracy - i + 1)
			next_deg = math.atan(sub_h / sub_w) * 180 / math.pi
		for i in range(1, accuracy + 1):
			dist = math.sqrt(sub_h ** 2 + sub_w ** 2)
			self.turtle.rt(next_deg - prev_deg)
			self.turtle.fd(dist)
			prev_deg = next_deg
			sub_h = delta_h * (accuracy - i + 1)
			sub_w = delta_w * i
			next_deg = 180 - math.atan(sub_h / sub_w) * 180 / math.pi
		for i in range(1, 3):
			dist = math.sqrt(sub_h ** 2 + sub_w ** 2)
			self.turtle.rt(next_deg - prev_deg)
			self.turtle.fd(dist)
			prev_deg = next_deg
			sub_h = delta_h * i
			sub_w = delta_w * (accuracy - i + 1)
		self.turtle.lt(state_heading + 180 - self.turtle.heading())
#		print(self.turtle.heading())

	def A(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan((xwidth * 0.5) / xheight) * 180 / math.pi
		long_side = math.sqrt(xheight ** 2 + (xwidth / 2) ** 2)
		short_rot = 180 - (math.atan((xwidth * 0.8) / (xheight * 0.4)) * 180 / math.pi) + rotate
		short_cross = math.sqrt((xwidth * 0.8) ** 2 + (xheight * 0.4) ** 2)
		self.turtle.pu()
		self.turtle.lt(90)
		self.turtle.bk(xheight)
		self.turtle.rt(rotate)
		self.turtle.pd()
		self.turtle.fd(long_side)
		self.turtle.rt(180 - rotate * 2)
		self.turtle.fd(long_side)
		self.turtle.pu()
		self.turtle.rt(short_rot)
		self.turtle.fd(short_cross)
		self.turtle.rt(270 - short_rot + rotate)
		self.turtle.pd()
		self.turtle.fd(xwidth * 0.6)
		self.turtle.pu()
		self.turtle.rt(270 - short_rot + rotate)
		self.turtle.fd(short_cross)
		self.turtle.rt(short_rot - rotate)
		self.turtle.fd(xheight)
		self.turtle.rt(90)
		self.turtle.pd()

	def B(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.half_oval(xheight * 0.4, xwidth * 0.8, accuracy, xdeg)
		self.turtle.rt(180)
		self.half_oval(xheight * 0.6, xwidth, accuracy, xdeg)
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.rt(90)

	def C(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.square(xheight, xwidth)

	def D(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.half_oval(xheight, xwidth, accuracy, xdeg)
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.rt(90)

	def E(self, xheight = 100, xwidth = 80, xdeg = 0):
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth)
		self.turtle.rt(90)
		self.turtle.pd()
		self.turtle.fd(xheight)
		self.turtle.lt(90)
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth)
		self.turtle.rt(90)
		self.turtle.bk(xheight * 0.6)
		self.turtle.lt(90)
		self.turtle.pd()
		self.turtle.fd(xwidth * 0.8)
		self.turtle.pu()
		self.turtle.bk(xwidth * 0.8)
		self.turtle.rt(90)
		self.turtle.bk(xheight * 0.4)
		self.turtle.lt(90)
		self.turtle.pd()

	def F(self, xheight = 100, xwidth = 80, xdeg = 0):
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth)
		self.turtle.rt(90)
		self.turtle.pd()
		self.turtle.fd(xheight)
		self.turtle.pu()
		self.turtle.bk(xheight * 0.6)
		self.turtle.lt(90)
		self.turtle.pd()
		self.turtle.fd(xwidth * 0.8)
		self.turtle.pu()
		self.turtle.bk(xwidth * 0.8)
		self.turtle.rt(90)
		self.turtle.bk(xheight * 0.4)
		self.turtle.lt(90)
		self.turtle.pd()

	def G(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.square(xheight, xwidth)

	def H(self, xheight = 100, xwidth = 80, xdeg = 0):
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.pu()
		self.turtle.bk(xheight * 0.5)
		self.turtle.lt(90)
		self.turtle.pd()
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.lt(90)
		self.turtle.fd(xheight * 0.5)
		self.turtle.pd()
		self.turtle.bk(xheight)
		self.turtle.pu()
		self.turtle.fd(xheight)
		self.turtle.rt(90)
		self.turtle.bk(xwidth)
		self.turtle.pd()

	def I(self, xheight = 100, xwidth = 80, xdeg = 0):
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth * 0.5)
		self.turtle.rt(90)
		self.turtle.pd()
		self.turtle.fd(xheight)
		self.turtle.pu()
		self.turtle.lt(90)
		self.turtle.bk(xwidth * 0.5)
		self.turtle.pd()
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth)
		self.turtle.lt(90)
		self.turtle.fd(xheight)
		self.turtle.rt(90)
		self.turtle.pd()

	def J(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth * 0.5)
		self.turtle.rt(90)
		self.turtle.pd()
		self.turtle.fd(xheight * 0.9)
		self.half_oval(xwidth * 0.5, xheight * 0.1, accuracy, xdeg)
		self.turtle.pu()
		self.turtle.fd(xheight * 0.9)
		self.turtle.rt(90)
		self.turtle.pd()

	def K(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan(xheight * 0.5 / xwidth) * 180 / math.pi
		side = math.sqrt((xheight * 0.5) ** 2 + xwidth ** 2)
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.pu()
		self.turtle.bk(xheight * 0.5)
		self.turtle.lt(90 + rotate)
		self.turtle.pd()
		self.turtle.fd(side)
		self.turtle.pu()
		self.turtle.bk(side)
		self.turtle.rt(rotate * 2)
		self.turtle.pd()
		self.turtle.fd(side)
		self.turtle.pu()
		self.turtle.bk(side)
		self.turtle.lt(90 + rotate)
		self.turtle.fd(xheight * 0.5)
		self.turtle.rt(90)
		self.turtle.pd()

	def L(self, xheight = 100, xwidth = 80, xdeg = 0):
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.lt(90)
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth)
		self.turtle.rt(90)
		self.turtle.bk(xheight)
		self.turtle.lt(90)
		self.turtle.pd()

	def M(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan((xwidth * 0.5) / (xheight * 0.6)) * 180 / math.pi
		side = math.sqrt((xwidth * 0.5) ** 2 + (xheight * 0.6) ** 2)
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.pu()
		self.turtle.bk(xheight)
		self.turtle.lt(rotate)
		self.turtle.pd()
		self.turtle.fd(side)
		self.turtle.lt(180 - rotate * 2)
		self.turtle.fd(side)
		self.turtle.lt(rotate)
		self.turtle.bk(xheight)
		self.turtle.pu()
		self.turtle.fd(xheight)
		self.turtle.lt(90)
		self.turtle.fd(xwidth)
		self.turtle.lt(180)
		self.turtle.pd()

	def N(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan(xwidth / xheight) * 180 / math.pi
		side = math.sqrt(xwidth ** 2 + xheight ** 2)
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.pu()
		self.turtle.bk(xheight)
		self.turtle.lt(rotate)
		self.turtle.pd()
		self.turtle.fd(side)
		self.turtle.rt(rotate)
		self.turtle.bk(xheight)
		self.turtle.pu()
		self.turtle.lt(90)
		self.turtle.bk(xwidth)
		self.turtle.pd()

	def O(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		'''
		note after complete:
		do not use accumulator for sub_h and sub_w, since the float value accuracy
		in python is awful, and will cause negative width, further causes reverse degree
		'''
		delta_h = (xheight * 0.5) / sum([i for i in range(1, accuracy + 1)])
		delta_w = (xwidth * 0.5) / sum([i for i in range(1, accuracy + 1)])
		sub_h = 0
		sub_w = delta_w * accuracy
		next_deg = 0
		prev_deg = 0
		self.turtle.pu()
		self.turtle.fd(xwidth * 0.5 - sub_w)
		self.turtle.pd()
		for i in range(1, accuracy + 1):
			dist = math.sqrt(sub_h ** 2 + sub_w ** 2)
			self.turtle.rt(next_deg - prev_deg)
			self.turtle.fd(dist)
			prev_deg = next_deg
			sub_h = delta_h * i
			sub_w = delta_w * (accuracy - i + 1)
			next_deg = math.atan(sub_h / sub_w) * 180 / math.pi
		for i in range(1, accuracy + 1):
			dist = math.sqrt(sub_h ** 2 + sub_w ** 2)
			self.turtle.rt(next_deg - prev_deg)
			self.turtle.fd(dist)
			prev_deg = next_deg
			sub_h = delta_h * (accuracy - i + 1)
			sub_w = delta_w * i
			next_deg = 180 - math.atan(sub_h / sub_w) * 180 / math.pi
		for i in range(1, accuracy + 1):
			dist = math.sqrt(sub_h ** 2 + sub_w ** 2)
			self.turtle.rt(next_deg - prev_deg)
			self.turtle.fd(dist)
			prev_deg = next_deg
			sub_h = delta_h * i
			sub_w = delta_w * (accuracy - i + 1)
			next_deg = 180 + math.atan(sub_h / sub_w) * 180 / math.pi
		for i in range(1, accuracy + 1):
			dist = math.sqrt(sub_h ** 2 + sub_w ** 2)
			self.turtle.rt(next_deg - prev_deg)
			self.turtle.fd(dist)
			prev_deg = next_deg
			sub_h = delta_h * (accuracy - i + 1)
			sub_w = delta_w * i
			next_deg = 360 - math.atan(sub_h / sub_w) * 180 / math.pi
		self.turtle.lt(- self.turtle.heading())
		self.turtle.pu()
		self.turtle.bk(xwidth * 0.5)
		self.turtle.pd()

	def P(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.half_oval(xheight * 0.4, xwidth, accuracy, xdeg)
		self.turtle.pu()
		self.turtle.lt(90)
		self.turtle.fd(xheight * 0.6)
		self.turtle.pd()
		self.turtle.bk(xheight)
		self.turtle.lt(90)

	def Q(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		rotate = math.atan(xheight / xwidth) * 180 / math.pi
		side = math.sqrt(xheight ** 2 + xwidth ** 2)		
		self.O(xheight, xwidth, accuracy, xdeg)
		self.turtle.pu()
		self.turtle.rt(rotate)
		self.turtle.fd(side * 0.7)
		self.turtle.pd()
		self.turtle.fd(side * 0.3)
		self.turtle.pu()
		self.turtle.bk(side)
		self.turtle.lt(rotate)
		self.turtle.pd()

	def R(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		rotate = math.atan((xheight * 0.6) / xwidth) * 180 / math.pi
		side = math.sqrt(xwidth ** 2 + (xheight * 0.6) ** 2)
		self.half_oval(xheight * 0.4, xwidth, accuracy, xdeg)
		self.turtle.rt(rotate)
		self.turtle.bk(side)
		self.turtle.pu()
		self.turtle.fd(side)
		self.turtle.rt(90 - rotate)
		self.turtle.bk(xheight * 0.6)
		self.turtle.pd()
		self.turtle.fd(xheight)
		self.turtle.rt(90)

	def S(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.square(xheight, xwidth)

	def T(self, xheight = 100, xwidth = 80, xdeg = 0):
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth / 2)
		self.turtle.rt(90)
		self.turtle.pd()
		self.turtle.fd(xheight)
		self.turtle.pu()
		self.turtle.bk(xheight)
		self.turtle.lt(90)
		self.turtle.bk(xwidth / 2)
		self.turtle.pd()

	def U(self, xheight = 100, xwidth = 80, accuracy = 40, xdeg = 0):
		self.turtle.rt(90)
		self.turtle.fd(xheight * 0.8)
		self.half_oval(- xwidth, xheight * 0.2, accuracy, xdeg)
		self.turtle.fd(xheight * 0.8)
		self.turtle.pu()
		self.turtle.rt(90)
		self.turtle.bk(xwidth)
		self.turtle.pd()

	def V(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan(xheight / (xwidth * 0.5)) * 180 / math.pi
		side = math.sqrt(xheight ** 2 + (xwidth * 0.5) ** 2)
		self.turtle.rt(rotate)
		self.turtle.fd(side)
		self.turtle.lt(rotate * 2)
		self.turtle.fd(side)
		self.turtle.pu()
		self.turtle.rt(rotate)
		self.turtle.bk(xwidth)
		self.turtle.pd()

	def W(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan((xwidth * 0.5) / (xheight * 0.6)) * 180 / math.pi
		side = math.sqrt((xwidth * 0.5) ** 2 + (xheight * 0.6) ** 2)
		self.turtle.rt(90)
		self.turtle.fd(xheight)
		self.turtle.rt(rotate)
		self.turtle.bk(side)
		self.turtle.lt(rotate * 2)
		self.turtle.fd(side)
		self.turtle.rt(rotate)
		self.turtle.bk(xheight)
		self.turtle.pu()
		self.turtle.lt(90)
		self.turtle.bk(xwidth)
		self.turtle.pd()

	def X(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan(xheight / xwidth) * 180 / math.pi
		side = math.sqrt(xwidth ** 2 + xheight ** 2)
		self.turtle.rt(rotate)
		self.turtle.fd(side)
		self.turtle.pu()
		self.turtle.lt(rotate)
		self.turtle.bk(xwidth)
		self.turtle.lt(rotate)
		self.turtle.pd()
		self.turtle.fd(side)
		self.turtle.pu()
		self.turtle.rt(rotate)
		self.turtle.bk(xwidth)
		self.turtle.pd()

	def Y(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan((xheight * 0.4) / (xwidth * 0.5)) * 180 / math.pi
		side = math.sqrt((xheight * 0.4) ** 2 + (xwidth * 0.5) ** 2)
		self.turtle.rt(rotate)
		self.turtle.fd(side)
		self.turtle.rt(90 - rotate)
		self.turtle.fd(xheight * 0.6)
		self.turtle.pu()
		self.turtle.bk(xheight * 0.6)
		self.turtle.lt(90 + rotate)
		self.turtle.pd()
		self.turtle.fd(side)
		self.turtle.pu()
		self.turtle.rt(rotate)
		self.turtle.bk(xwidth)
		self.turtle.pd()

	def Z(self, xheight = 100, xwidth = 80, xdeg = 0):
		rotate = math.atan(xheight / xwidth) * 180 / math.pi
		side = math.sqrt(xheight ** 2 + xwidth ** 2)
		self.turtle.fd(xwidth)
		self.turtle.lt(rotate)
		self.turtle.bk(side)
		self.turtle.rt(rotate)
		self.turtle.fd(xwidth)
		self.turtle.pu()
		self.turtle.bk(xwidth)
		self.turtle.lt(90)
		self.turtle.fd(xheight)
		self.turtle.rt(90)
		self.turtle.pd()

def retype(xstr, xheight = 100, xwidth = 80, accuracy = 40, xgap = 10):
	new = Tchar()
	new.turtle.ht()
	new.turtle.speed(0)
	for each in xstr:
		if each.upper() == 'A':
			new.A(xheight, xwidth)
		elif each.upper() == 'B':
			new.B(xheight, xwidth, accuracy)
		elif each.upper() == 'C':
			new.C(xheight, xwidth, accuracy)
		elif each.upper() == 'D':
			new.D(xheight, xwidth, accuracy)
		elif each.upper() == 'E':
			new.E(xheight, xwidth)
		elif each.upper() == 'F':
			new.F(xheight, xwidth)
		elif each.upper() == 'G':
			new.G(xheight, xwidth, accuracy)
		elif each.upper() == 'H':
			new.H(xheight, xwidth)
		elif each.upper() == 'I':
			new.I(xheight, xwidth)
		elif each.upper() == 'J':
			new.J(xheight, xwidth, accuracy)
		elif each.upper() == 'K':
			new.K(xheight, xwidth)
		elif each.upper() == 'L':
			new.L(xheight, xwidth)
		elif each.upper() == 'M':
			new.M(xheight, xwidth)
		elif each.upper() == 'N':
			new.N(xheight, xwidth)
		elif each.upper() == 'O':
			new.O(xheight, xwidth, accuracy)
		elif each.upper() == 'P':
			new.P(xheight, xwidth, accuracy)
		elif each.upper() == 'Q':
			new.Q(xheight, xwidth, accuracy)
		elif each.upper() == 'R':
			new.R(xheight, xwidth, accuracy)
		elif each.upper() == 'S':
			new.S(xheight, xwidth, accuracy)
		elif each.upper() == 'T':
			new.T(xheight, xwidth)
		elif each.upper() == 'U':
			new.U(xheight, xwidth, accuracy)
		elif each.upper() == 'V':
			new.V(xheight, xwidth)
		elif each.upper() == 'W':
			new.W(xheight, xwidth)
		elif each.upper() == 'X':
			new.X(xheight, xwidth)
		elif each.upper() == 'Y':
			new.Y(xheight, xwidth)
		elif each.upper() == 'Z':
			new.Z(xheight, xwidth)

		print(new.turtle.heading())
		new.next(xwidth, xgap)
	new.turtle.st()

def main():
	win = turtle.Screen()
	win.screensize(10000, 1000)
	retype("barry will be the idiot", 100, 50, 40, 10)
	'''
	test = Tchar()
	test.turtle.speed(0.7)
	test.square()
	test.J()
	test.next()
	'''
	win.exitonclick()

if __name__ == '__main__':
	main()