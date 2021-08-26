
from abc import ABC, abstractmethod


class BaseFigure(ABC):

	@abstractmethod
	def get_square(self):
		pass

	@abstractmethod
	def get_perimeter(self):
		pass

	def print_hello(self):
		print("hello!")

class Square_class(BaseFigure):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def get_square(self):
		square = self.a*self.b
		return print(square)

	def get_perimeter(self):
		perimetr = 2*self.a + 2*self.b
		return print(perimetr)

class Triangle_class(BaseFigure):
	def __init__(self, a, b, s):
		self.a = a
		self.b = b
		self.s = s

	def get_square(self):
		square = 0.5*(self.a*self.s)
		return print(square)


	def get_perimeter(self):
		perimetr = self.s +self.a + self.b
		return print(perimetr)



rectangle_1 = Square_class(15, 20)	
rectangle_2 = Triangle_class(15, 20, 10)

rectangle_1.get_square()
rectangle_1.get_perimeter()
rectangle_1.print_hello()

rectangle_2.get_square()
rectangle_2.get_perimeter()
rectangle_2.print_hello()