#!/usr/bin/python
#coding=utf-8

#列表，基本上就是JavaScript中的数组

#列表可包含多种类型的数据

arr = ['test', 42, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']]

#使用in进行存在性检查
print 'test' in arr

#取数
print arr[1]

#分片操作
sub_arr = arr[2]
#从2取到8，每隔3个取一个
print sub_arr[2:8:3]

#list方法可以将字符串还原为列表
arr3 = list('love')
arr4 = list('hate')

#列表可以相加，即concat，也可以进行乘法运算，重复多遍
print arr3 + arr4 * 4

arr5 = list('hello')

#删除列表元素
del arr5[1]
print arr5

#统计元素出现次数
print arr5.count('l')

#查找第一次出现位置
print arr5.index('o')

#元组
#元组，可以理解为参数排列，使用逗号分隔一些数值，即创建元组，带不带 () 都可以
arr6 = 1, 'world', 3
#以类似于列表的方式取数
print arr6[1]

#tuple函数可以将列表转换为元组
print tuple([1,4,7])