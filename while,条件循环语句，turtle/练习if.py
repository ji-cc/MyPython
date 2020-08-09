'''
1.从控制台输入一个三位数，判断是否为水仙花数。eg:153=1~3+5~3+3~3
2.从控制台输入一个五位数，判断是否为回文数。eg:11111    12321    12221
3.输入两个数，输出较大值
4.输入三个数，输出较大值
'''
'''
#1
num = int(input("输入一个三位数："))
#153
ge = num % 10
shi = num // 10 % 10
bai = num // 100
if num == ge**3 +  shi ** 3 + pow(bai, 3):
    print("yes")
else:
    print("no")'''
'''
#2   代码优化
num = int(input("请输入一个五位数："))
ge = num % 10
wan = num // 10000
if ge != wan:
    print("no")
if 

#4
num1 = int(input())
num2 = int(input())
num3 = int(input())
max = num1
if num2 > num1:
    max = num2
if num3 > max:
    max = num3
print("max =", max)'''


'''
打印出所有三位数中的水仙花数
五位数中有多少个回文数
从控制台输入一个数，判断是否为质数
从控制台输入一个数，分解质因数
输入一个字符串，计算字符串里所有数字之和
'''


'''
#1
num = 100
while num <=999:
    a = num % 10
    b = num // 10 % 10
    c = num //100
    if num == a**3 + b**3 + c**3:
        print(num)
    num += 1

print("****************************")

#3
num = int(input("输入一个数："))
if num == 2:
    print("是质数")
a = 2
while a < num:
    if num % a == 0:
        print("不是质数")    #此处应跳出循环
    a += 1
if a == num:
    print("是质数")

print("****************************")

str = input()
index = 0
sum =0
while index < len(str):
    if str[index] >= "0" and str[index] <= "9":
        sum += int(str[index])
    index += 1
print("sum = %d" %(sum))'''

#字符串比较大小
#从第一个字母开始比较，谁的ASCII值大谁就大
print("njjkj" > "hihuh")   #回车运行
'''
#4
#90 = 2x3x3x5
num = int(input("输入一个数："))
i = 2
while num != 1:
    if num % i == 0:
        print(i)
        num /= i
    else:
        i += 1
'''


str = input()
str1 = str.strip()
index = 0
count = 0
while index < len(str1):
    while str1[index] != " ":
        index += 1
        if index == len(str1):
            break
            #结束这个循环
    count += 1
    print(count)
    if index == len(str1):
        break

    while str1[index] == " ":
        index += 1



