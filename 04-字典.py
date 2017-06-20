#!/usr/bin/python
#coding=utf-8

#字典就是对象
#但属性必须使用引号
obj = {'name': 'Alice', 'age': 12}
#不能使用obj.age取值
#可以使用obj['age']或obj.get('age')取值
#但是前者如果取不到值会报错
print obj['age']
#后者如果取不到值会返回None类型
print obj.get('gender')

#可以将类似于多维数组的 列表嵌套元组 转换为字典
obj2 = dict([('name', 'Fish'),('age', 20)])
print obj2['name']

obj2['name']='海涛'
print obj2['name']

#使用has_key方法检测是否包含键值
print obj2.has_key('gender')