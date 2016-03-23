#!/usr/bin/python


class fruit:
	def __init__(self,color):
		self.__color = color
		self.__type = "chengshou"

	def prints(self):
		print self.__color,self.__type


class apple(fruit):
	def __init__(self,color,name):
		fruit.__init__(self,color)
		self.__name = name

	def prints(self):
		fruit.prints(self)
		print self.__name


if __name__=="__main__":
	a = apple("red","apple")
	a.prints()

