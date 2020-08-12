'''
tuple:是一种有序集合
特点：
    与列表相似
    一旦初始化就不能修改
    使用小括号
创建tuple
    格式： 元组名 = (元组元素1,元组元素2, 元组元素3, ……, 元组元素n)
'''




#创建空元组
tuple = ()
print(tuple)
#创建带有元素的元组
#元组中的元素类型可以不同
#定义只有一个元素的元组
tuple = (1, )
print(tuple)
print(type(tuple))


#元组元素的访问
#格式：元组名[小标]
#下标从0开始
tuple = (1, 2, 3, 4)
print(tuple[0])
print(tuple[1])
print(tuple[2])
# print(tuple[4])  #下标超过范围（越界）
print(tuple[-1])   #获取最后一个元素
print(tuple[-2])
print(tuple[-3])
print(tuple[-4])

#修改元组
tuple = (1, 2, 3, 4,[5,6,7])
#tuple[0] = 100    #报错，元组不能变
# tuple[-1] = [7,8,9]   #报错
tuple[-1][0] = 500
print(tuple)

#删除元组
tuple = (1,2,3)
del tuple
print(tuple)

#元组的操作
t1 = (1,2,3)
t2 = (4,5,6)
print(t1 + t2)
print(t1,t2)

#元组重复
t1 = (1,2,3)
print(t1 * 3)

#判断元素是否在元组中
t1 = (1,2,3)
print(4 in t1)

#元组的截取
#格式：元组名[开始下标：结束下标]    截取到结束下标之前
t1 = (1,2,3,4,5,6,4,7,8,9)
print(t1[3:6])
print(t1[3:])
print(t1[:6])

#二维元组:元素为一维元组的元组
t1 = ((1,2,3),(4,5,6),(7,8,9))
print(t1[1][1])

#元组的方法
#len()   返回元组中元素的个数
t1 = (1,2,3,4,5,6,7,8,9)
print(len(t1))

#max()  min()   返回元组中的最大值、最小值
print(max(5,9,7,3,1))
print(min(5,9,7,3,1))

#将列表转为元组
list = [1,2,3]
t1 = tuple(list)
print(t1)

#元组的遍历
for i in (1,2,3):
    print(i)


