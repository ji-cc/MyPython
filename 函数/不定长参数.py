'''
不定长参数：
    概念：能处理比定义时更多的参数
'''
#加了*的变量会存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元祖
def func(name, *arr):        #arr:会接收剩下的所有参数
    print(name)
    # print(type(arr))   #<class 'tuple'>
    for x in arr:
        print(x)
func("sunck", "good", "nice")

#求多个数的和
def mySum(*l):
    sum = 0
    for i in l:
        sum += i
    return sum
print(mySum(1,2,3,5,6))    #17

# **代表键值对的参数字典，和*所代表的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))    #<class 'dict'>
func2(x = 1, y = 2, z = 3)      # {'x': 1, 'y': 2, 'z': 3}

#可以接收任意参数
def func3(*args, **kwargs):
    pass   #代表一个空语句
