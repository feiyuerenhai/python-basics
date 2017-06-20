#!/usr/bin/python
#coding=utf-8

#格式化操作符号 %
tmpl = 'My friend %s is %i years old and scores %.2f in the test'
#操作符的入参
val = 'jack', 12, 3.75
#输出
print tmpl % val

#查找第一次出现的位置
print 'you jump i jump'.find('jump')

#大小写转换
print 'test'.upper()

#替换
print 'test'.replace('es', '--')

#拆分得到数组
print '1+3+test+love'.split('+')