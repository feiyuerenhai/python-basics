#!/usr/bin/python
#coding=utf-8

#使用def定义函数
def sum(x,y,z):
	#函数的第一句可以是一个字符串，作为函数的说明文档，使用__doc__访问
	'this is a function that sums up three parameters'
	return x+y+z

print sum(1,2,3)
print sum.__doc__

def greet(name, greeting):
	return greeting % name

#python中的函数可以使用标记来防止传参顺序紊乱
print greet(greeting='hi, %s, gooding morning', name='jack')

#使用*号做参数收集
def fn(x, y, z, *restFlat, **restPair):
	return {
		'xyz': [x,y,z],
		'restFlat': restFlat,
		'restPair': restPair
	}

print fn(1, 2, 3, 4, 5, 6, 7, 8, 9, name='tony', age=20)

def f1():
	x = 1
	y = 2
	#调用vars方法，可以返回该方法调用所在地的变量字典
	return vars()

print f1()

#此时，vars()与locals()结果相同
#还有一个方法globals()，用于获取全局变量字典