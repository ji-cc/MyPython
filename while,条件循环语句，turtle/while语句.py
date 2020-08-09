'''
while 语句

while 表达式：
    语句

逻辑：当程序执行到while语句时，首先计算“表达式”的值，如果“表达式”的值为假，则跳出while语句；如果“表达式”的值为真，则执行“语句
”，执行完“语句”，再去计算“表达式”，一直循环，直至“表达式”的值为假才停止

'''
'''
num = 1
while num <= 5:
    print(num)
    num += 1

# 计算1+2+3+……+100
sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print("sum = %d" %(sum) )'''

str = "sunck is a handsome man"
index = 0
while index < len(str):
    print("str[%d] = %s" % (index, str[index]))
    index += 1

str36 = "a"    #转换生成SSCII值
print(ord(str36))

import time
while 1:
    time.sleep(3)  #每3秒执行一次循环
    print("***")




