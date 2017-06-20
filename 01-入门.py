#!/usr/bin/python
#coding=utf-8

#注释：python2之前不支持非ASCII，必须使用codeing=utf-8标明

#声明变量，变量和值之间有多少空格都可以
#一行语句的结尾有没有分号都可以
greeting      =                'hello world!\n世界你好！';

#在shell中有三种引用，python中不再推荐使用反引号``

#多行文本
saying = '''
使用python
美好的一天
开始了'''

#打印变量
print greeting+saying

#python支持类似于ES6的解构赋值
x,y,z=1,2,list('love')
print z[2]

#利用解构赋值还可以交换变量值
x,y=y,x
print x