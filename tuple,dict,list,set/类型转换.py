'''
类型转换
'''
#list-->set
s1 = [1,2,3,4,5,3,4]
s2 = set(s1)
print(s2,type(s2))

#tuple-->set
s1 = (1,2,3,4,5,3,2)
s2 = set(s1)
print(s2,type(s2))

#set-->list
s1 = {1,2,3}
s2 = list(s1)
print(s1,type(s1))
print(s2,type(s2))

#set-->tuple
s1 = {1,2,3,4}
s2 = tuple(s1)
print(s2,type(s2))










