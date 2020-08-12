'''
set:类似dict,是一组key的集合，不存储value
    无序和无重复元素的集合
'''
#创建
#创建set需要一个list或者tuple或者dict作为输入集合
#重复元素在set中被自动过滤
s1 = set([1,2,3,4,5])
print(s1)
s2 = set({1:"good", 2:"nice"})
print(s2)

#添加
s = set([1,2,3,4,5])
s.add(6)
s.add(3)   #可以添加重复的，但不会有效果
# s.add([7,8,9])    #set的元素(key值)不能是列表，而list是可变的，所以报错
s.add((7,8,9))     #元组不可变
# s.add({1:"a"})     #set的元素(key值)不能是字典，而字典是可变的，所以报错
print(s)

#插入整个list,tuple, 字符串，打碎插入
s = set([1,2,3,4,5])
s.update([6,7,8])
s.update((9,10))
s.update("sunck")
print(s)

#删除
s = set([1,2,3,4,5])
s.remove(3)
print(s)

#遍历
s = set([1,2,3,4,5])
for i in s:
    print(i)
# print(s[7])#set没有索引

s = set([1,2,3,4,5])
for index, data in  enumerate(s):
    print(index, data)

#求交集
s1 = set([1,2,3])
s2 = set([2,3,4])
a1 = s1 & s2
print(a1)
print(type(a1))

# 求并集
s1 = set([1,2,3])
s2 = set([3,4])
a = s1 | s2
print(a)

















