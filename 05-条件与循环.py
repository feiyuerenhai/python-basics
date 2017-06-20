#!/usr/bin/python
#coding=utf-8

#python的语句块，使用缩进来标识，但是推荐不要用tab，而使用空格
if (1>0):print '1>0'

if(2>1):
#如果删除这个缩进，则程序不能执行
	print '2>1'

if(3>2):
#实际上，只要有缩进就行，不管缩进是几个
							print '3>2'

if(4>5):
				print 'impossible'
elif(4>6):
								print 'impossible neither'
elif(4>7):
#如果是空的代码块，必须使用pass标明什么都不做
	pass
else:
	print 'neither of the above is possible'

#总之，缩进并不关联逻辑关系，只表示以下为上面冒号 : 的代码块

#同样有类型转换
print [1,2,3]==[1,2,3]
print [1,2,3] is [1,2,3]

#for循环遍历列表
for item in list('hello'):
	print '>'+item

#for循环遍历字典
d = {'name': 'fish', 'gender': 'male'}
for key in d:
	print key+' -> ' + d.get(key)

#断言类似于if语句，但是，一旦出错会直接导致程序崩溃

assert 1>2, 'sorry, 1>2 is wrong'

print '所以，程序不会执行到这里'