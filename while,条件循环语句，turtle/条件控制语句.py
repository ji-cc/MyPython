'''
if 语句
if-else语句

if-elif-else语句
格式：
if 表达式：
    语句1
elif 表达式2：
    语句2
elif 表达式3：
    语句3
……
elif 表示式n:
    表达式n
else:        #else可有可无
    语句
'''
# elif       else if
#每个el都是对他上面所有表达式的否定



#死循环：表达式永远为真的循环
'''
while 2:
    print("sunck is a good man")'''

#使用else语句
'''
while 表达式：
    语句1
else:
    语句2
逻辑：在表达式为假时执行语句2

'''
a = 1
while a <= 3:
    print("****")
    a += 1
else:
    print("*********")


#for语句
'''
格式：
for 变量名 in 集合：
    语句
逻辑：按顺序取集合中的每一个元素赋值给“变量”，再去执行语句。如此循环往复，直到取完“集合”中的元素截止

for i in [1,2,3,4,5]:
    print(i)
'''
'''
range(start,end,step)函数    列表生成器：生成数列
'''
a = range(10)
print(a)
for x in range(10):
    print(x)
for x in range(2,12,2):
    print(x)

#同时遍历下标和元素
for index, m in enumerate([1,2,3,4,5]):    #index, m = 下标， 元素
    print(index, m)
#求1到100的和
sum = 0
for n in range(1, 101):
    sum += n
print(sum)


'''
break语句：
作用;跳出for和while循环
注：只能跳出距离他最近的那一层循环
'''
for i in range(10):
    print(i)
    if i==5:
        break

num = 1
while num <= 10:
    print(num)
    if num == 3:
        break
    num += 1
#注：循环语句可以有else语句，break导致循环截止，不会执行else下面的语句
else:
    print("sunck")



'''
continue语句：跳过当前循环中的剩余语句，然后继续下一次循环
'''
for i in range(5):
    print(i)
    if i == 3:
        continue
    print("**")
































