'''
dict(字典)
概述：
    使用键-值（key-value）存储，具有极快的查找速度
注：字典是无序的
key的特性：
    字典的key必须唯一
    key必须是不可变对象
    字符串、整数等都是不可变的，可以作为key
    list是可变的，不可作为key
eg:保存多位学生的姓名和成绩
    使用字典，学生姓名作为key,学生成绩作为值
'''
#元素的访问
#获取：字典名[key]
dict1 = {"Tom":60,"lilei":70}
print(dict1["Tom"])
ret = dict1.get("sunck")
if ret == None:
    print("没有")
else:
    print("有")

#添加
dict1 = {"Tom":60,"lilei":70}
dict1["hanmei"] = 90
#因为一个key对应一个value,所以多次对一个key赋值其实是修改值
dict1["lilei"] = 80
print(dict1)

#删除
dict1 = {"Tom":60,"lilei":70}
dict1.pop("Tom")
print(dict1)

#遍历
dict1 = {"Tom":60,"lilei":70, "haimeimei":90}
for key in dict1:
    print(key, dict1[key])

#print(dict1.values())  #结果：dict_values([60, 70, 90])
for value in dict1.values():
    print(value)

#print(dict1.items())   #结果dict_items([('Tom', 60), ('lilei', 70), ('haimeimei', 90)])
for k, v in dict1.items():
    print(k, v)

for i,v in enumerate(dict1):
    print(i, v)

'''
dict:
    查找和插入数据极快，不会随着key-value的增加而变慢
    需要占用大量的内存，内存浪费多
list:
    查找和插入的速度会随着数据量的增多而减慢
    占用空间小，浪费内存少
'''
'''
#输入一个时间字符串，输出这个时间的下一秒
timestr = input()
#12:23:24
timelist = timestr.split(":")
h = int(timelist[0])
m = int(timelist[1])
s = int(timelist[2])
s += 1
if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
print("%.2d:%.2d:%.2d" %(h, m, s))
#结果
#06:59:59
#07:00:00

'''









