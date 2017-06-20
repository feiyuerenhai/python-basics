#!/usr/bin/python
#coding=utf-8

#基本用法
class Person:
	#自身属性
	species = 'human'
	#方法的第一个入参总是对象本身
	def getSpecies(self):
		return self.species
	def setName(selfObj, name):
		selfObj.name = name
	def getName(selfObj):
		return selfObj.name
	#还可以使用lambda表达式
	getName2=lambda self:self.name


jack = Person()

print jack.getSpecies()
jack.setName('jack')
print jack.getName()
print jack.getName2()

#构造器
class Computer:
	def __init__(self, name):
		self.name = name;
	def getName(self):
		return self.name

comp = Computer('ordinary computer')
print comp.getName()

#继承
class AppleComputer(Computer):
	def __init__(self, name, price):
		# python3才刚刚加入的super方法
		# super(AppleComputer, self).__init__(name)
		Computer.__init__(self, name)
		self.price = price
	def getPrice(self):
		return '$ %i' % self.price

appComp = AppleComputer('app computer', 146)
print appComp.getName()
print appComp.getPrice()
