#!/usr/bin/python
#coding=utf-8

#exec与eval是实现元编程的绝佳方法

#exec默认是在当前作用域内执行
a='hello'
exec('print a')

#但也可以改变其执行作用域，使用exec in语句
scope={'a': 'world'}
exec('print a') in scope

#eval与exec的区别在于，eval会返回执行结果
d = eval("1+1")
print d

#同样地，eval也能指定作用域
print eval('x+y', {'x':2, 'y':3})