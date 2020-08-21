#列表
#存储5个人的年龄，求他们的平均年龄
list2 = [18, 19, 20, 21, 22]
index = 0
sum = 0
while index < 5:
    sum += list2[index]
    index += 1
print("平均年龄：%d" %(sum / 5))
'''
创建列表
格式： 列表名 = [列表选项1, 列表选项2, ……,列表选项n]
'''
#创建空列表
list1 = []
print(list1)
#创建带有元素的列表
list2 = [18, 12, 15, 26, 22]
list3 = [1, 2, "sunck", "good", True]
print(list3)

#列表元素的访问
#取值   格式：列表名[下标]
list4 = [1, 2, 3, 4, 5]
print(list4[2])

#替换
list4[4] = 300
print(list(list4))

#列表操作：
#列表组合
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7 )

#列表重复
list5 = [1,2,3]
print(list5 * 3)
#判断元素是否在列表中
list5 = [1,2,3]
print(3 in list5)
print(6 in list5)

#列表的截取
list8 = [1,2,3,4,5,6,7,8,9]
print(list8[2:6])
print(list8[3:])
print(list8[:5])


#二维列表
list9 = [[1,2,3], [4,5,6], [7,8,9]]
print(list9[1])
print(list9[1][1])

#列表方法
#append 在列表末尾添加新的元素
list5 = [1,2,3]
list5.append(6)
list5.append([7,8,9])
print(list5)

#在末尾一次性追加另一个列表中的多个值
list5 = [1,2,3]
list5.extend([6,7,8])
print(list5)

#insert 在下标出添加一个元素，不覆盖原数据，原数据向后顺延
list5 = [1,2,3]
list5.insert(2,100)
print(list5)
list5.insert(2,[200,300])
print(list5)

#pop(x=list[-1])
#移除列表中指定下标元素，默认移除最后一个元素，并返回删除的数据
list5 = [1,2,3,4,5,6]
list5.pop()
print(list5)
print(list5.pop(1))
print(list5)

#remove  移除列表中的某个元素
list5 = [1,2,3,4,5,4]
list5.remove(4)
print(list5)

#clear  清楚列表中的元素
list5 = [1,2,3,4,5,4]
list5.clear()
print(list5)

#index 从列表中找出某个值第一个匹配的索引值
list5 = [1,2,3,4,5,3,4]
index1 = list5.index(3)
#圈定范围
index2 = list5.index(3,3,6)
#按住按住“Ctrl”键，并用鼠标点击想要查看的函数的函数名，就可以直接进入 __inti__.py 文件查看到该函数的定义。
print(index1, index2)

#列表中元素个数
list5 = [1,2,3,4,5,3,4]
print(len(list5))
#获取列表中的最大最小值
list5 = [1,2,3,4,5,3,4]
print(max(list5))
print(min(list5))
#查看元素在列表中出现的次数
list5 = [1,2,3,4,5,3,4]
print(list5.count(3))
#倒序
list5 = [1,2,3]
list5.reverse()
print(list5)

#排序   升序
list5 = [1,4,2,8,5]
list5.sort()
print(list5)


#拷贝
#浅拷贝
list1 = [1,2,3,4,5]
list2 = list1
list2[1] = 200
print(list1)
print(list2)
print(id(list1))
print(id(list2))
#深拷贝   内存拷贝
list1 = [1,2,3,4,5]
list2 = list1.copy()
list2[1] = 200
print(list1)
print(list2)
print(id(list1))
print(id(list2))

#将元组转成列表
list = list((1,2,3,4))
print(list)

#找出第二大的值
'''
listNum = []  #创建空列表
num = 0
while num < 10:    #从控制台输入列表
    val = int(input())
    listNum.append(val)
    num += 1
print(listNum)

#升序排序
listNum.sort()
lon = len(listNum)
count = listNum.count(listNum[lon - 1])   #统计列表里最大元素的个数
c = 0
while c < count:   #删除最大值
    listNum.pop()
    c += 1
print(listNum[len(listNum) - 1])    #输出第二大值
'''
'''
if listNum[0] >= listNum[1]:        #代码不完善
    max = listNum[0]
    sec = listNum[1]
else:
    max = listNum[1]
    sec = listNum[0]
index = 2
while index < len(listNum):
    if listNum[index] >= max:
        sec = max
        max = listNum[index]
    if listNum[index] >= sec:
        sec = listNum[index]
    index += 1
print(sec)
'''






















