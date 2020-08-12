'''
list:
创建一个列表（不赋初值）:
a = []
a = list()
创建一个列表，并对其赋初值
a = [1,2,3]
列表更高级的创建方法——用表达式创建
a = [i for i in range(1, 11)]
#创建一个元素分别为1,2，...10的列表

a = [i for i in range(1, 11) if i % 2 == 0]
#创建一个1-10，且元素为偶数的列表
用list（）函数将其他（可迭代）数据转换为列表
list('ab c')   #列表为['a', 'b', ' ', 'c']
'''
'''
dict:
a = {key1:value1, key2:value2}  # 第一种

a = dict(key1=value1, key2=value2)  # 第二种，注意此种情况下键必须为字符串

a = {}
a[key1] = value1  
a[key2] = value2  # 第三种

a = dict([(key1, value1), (key2, value2)])  # 第四种
a = dict(zip([key1, key2], [value1, value2]))  # 第四种衍生，使用zip函数把键列表和值列表打包成键值对一一对应的元组（即第四种方法）

a = dict.fromkeys([key1, key2], value)  # 第五种，这种情况适用于多个键对应相同值的情况

a = {x: x**2 for x in [1, 2, 3]}  # 第六种，字典推导表达式

'''
'''
tuple:
t1 = (1, 2, 3)
t2 = tuple([1, 2])  #(1, 2, 3) (1, 2)
print(t1,t2)

'''
'''
set:
s = {'s', 'e', 't'}
s = set(['a, b, c, d, e'])

#注意，python中{}为空字典类型，并非空集合。空集合需要用set()函数创建
s = set()  #创建一个空集合

#集合也可以用表达式（推导）的方式创建
{x * 2 for x in 'abc'}  #{'aa', 'bb', 'cc} 
{x **2 for x in range(1,5)}   #{1, 4, 9, 16}
'''


