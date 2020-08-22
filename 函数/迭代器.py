'''
    可迭代对象(Iterable)：可直接作用于for循环的对象统称为可迭代对象
    可用isinstance()去判断一个对象是否是可迭代对象
可以直接作用于for的数据类型一般分两种：
    集合数据类型：如：list, tuple, dict, set, string
    是generator, 包括生成器和带yield的generator function
'''
#from collections import Iterable    #版本更新
#判断是否为可迭代对象
from collections.abc import Iterable    #导入一个包
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(2, Iterable))

'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后跑出一个StopIteration错误，表示无法继续返回下一个值
    可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)
可以用isinstance()函数判断一个对象是否是Iterator对象
    
'''
from collections.abc import Iterator    #导入一个包
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))
#next()
l = (x for x in [25,456,2525,45681])
print(next(l))
print(next(l))
print(next(l))
print(next(l))


#转成迭代器(Iterator对象)
a1 = iter([1,2,3,4,5])
a2 = [1,2,3]
#print(next(a2))    #TypeError: 'list' object is not an iterator
print(next(a1))
print(next(a1))

print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(''), Iterator))



