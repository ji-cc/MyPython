
#字符串运算
'''
字符串的链接'''
'''
str6 = " sunck is a"
str7 = "good man"
str8 = str6 + str7
print(str8)
#输出重复字符串
str9 = "good"
str10 = str9 *3
print(str10)
#访问字符串中的某一个字母
#通过索引下标查找字符，索引从0开始
#格式：字符串名[下标]
str9 = "good"
print(str9[0])
# str9[0] = "a"   #字符串不可变

#截取字符串
str13 = "sunck is a good man!"
#从给定下标除截取到给定下标之前
str15 = str13[6:15]
#从头截取到给定下标之前
str16 = str13[:5]
#从给定下标处开始截取到结尾
str17 = str13[16:]
print("str15 =", str15)
print("str16 =", str16)
print("str17 =", str17)

str13 = "sunck is a good man!"
print("good" in str13)
print("good12" in str13)
print("good12" not in str13)

#格式化输出
num = 10
str19 = "sunck"
f = 10.1267
print("num =",num, "str19 =", str19)
#  %d    %s    %f   占位符
#                               精确到小数点后三位会四舍五入
print("num = %d, str19 = %s, f = %.3f" %(num, str19, f))
print("num = %d, str19 = %s, f = %f" %(num, str19, f))
'''
#转义字符    \  ：将一些字符转换成有特殊含义的字符
'''
# \n    换行
print("num = %d\nstr19 = %s\nf = %.3f" %(num, str19, f))
#   \'    \"
print("tom is a \'good\' man")
print("tom is a \"good\" man")
#如果字符串内有很多换行
print("good\nnice\nhand")
print('''
#good
#nice
#hand
''')
'''
#\t    制表符
'''
print("sunk\tgood")
#用r表示内部的字符串默认的字符串不转义
print("\\\t\\")
print(r"\\\t\\")



#eval()
#功能：将字符串str当成有效的表达式来求值并返回就算结果
num1 = eval("123")
print(num1)
print(type(num1))
print(eval("12+3"))


#len(str)
#返回字符串的长度
print(len("sunck is a good man"))

#lower(str)
#转化字符串中大写字母为小写字母
str20 = "SunCk iS a Good man"
str21 = str20.lower()
print(str21)

#upper()  z转化字符串中的小写字母为大写字母
str20 = "SunCk iS a Good man"
print(str20.upper())

#swapcase()  转化字符串中大写字母为小写字母，小写字母为大写字母
str20 = "SunCk iS a Good man"
print(str20.swapcase())

#capitalize()   首字母为大写，其他小写
str20 = "SunCk iS a Good man"
print(str20.capitalize())

#title()    每个单词的首字母大写
str20 = "SunCk iS a Good man"
print(str20.title())

#center(width,fillchar)  返回一个指定宽度的居中字符串，fillchar为填充的字符串
#center(width[,fillchar])   默认空格填充
str20 = "SunCk iS a Good man"
print(str20.center(40,"*"))

#ljust(width,fillchar)
#ljust(width[ ,fillchar])
#返回一个指定宽度的左对齐字符串，默认空格填充
str20 = "SunCk iS a Good man"
print(str20.ljust(40,"%"))


#rjust(width,fillchar)
#rjust(width[ ,fillchar])
#返回一个指定宽度的右对齐字符串，默认空格填充
str20 = "SunCk iS a Good man"
print(str20.rjust(40,"%"))



#zfill(width)
#返回一个一个长度为width的字符串，原字符串右对齐，前面补0
str20 = "SunCk iS a Good man"
print(str20.zfill(40))


#count(str[ ,start][ ,end])
#返回字符串中str出现的次数，可以指定一个范围默认从头到尾
str20 = "SunCk is is is a Good man"
print(str20.count("is",0,len(str20)))

#find(str[ ,start][ ,end])
#从左向右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，得到的是第一次出现的开始下标,没有返回-1
str20 = "SunCk is is is is a Good man"
print(str20.find("is"))
print(str20.find("aaa"))
print(str20.find("is",8,len(str20)))

#rfind(str[ ,start][ ,end])
#从右向左检测str字符串是否包含在字符串中
str20 = "SunCk is is is is a Good man"
print(str20.rfind("man"))
print(str20.rfind("aaa"))
print(str20.rfind("is",8,len(str20)))'''


#index(str,start = 0,end = len(str))
#跟find一样，但如果str不存在，会报一个异常
str20 = "SunCk is is is is a Good man"
print(str20.index("is"))

#rindex(str,start = 0,end = len(str))
#跟rfind一样，但如果str不存在，会报一个异常
str20 = "SunCk is is is is a Good man"
print(str20.rindex("is"))

#lstrip()   会截掉字符串左侧指定字符，默认为空格
str20 = "    SunCk is is is is a Good man"
print(str20.lstrip())
str20 = "*****SunCk is is is is a Good man"
print(str20.lstrip("*"))

#rstrip()   会截掉字符串右侧指定字符，默认为空格
str20 = "SunCk is is is is a Good man   "
print(str20.rstrip())
str20 = "SunCk is is is is a Good man*****"
print(str20.rstrip("*"))

#strip()  截取两边指定字符串
str20 = "******SunCk is is is is a Good man*****"
print(str20.strip("*"))

#split(str=""，num) 以str为分隔符截取字符串,指定num,则截取num个字符串,结果是个二维列表
str = "sunck**is*****a****good"
list = str.split("*")
print(list)
print(len(list))
count = 0
for i in list:
    if len(i) > 0:   #说明是一个单词
        print(i)
        count += 1
print(count)

#splitlines(keepends)   安装（'\r', '\r\n', '\n'）分隔，返回
#keepends可以不写,默认为False,当keepends == True时会保留换行符
str = '''sunck is a good man
sunck is a nice man
sunck is handsome man
'''
print(str.splitlines())

#join(seq)  以指定的字符串分隔符，将seq中的所有元素组合成一个字符串
list = ['sunck', 'is', 'a',  'good']
str = "***".join(list)
print(str)

#max() min()  按照ASCII值比较
str = "sunck is a nice man"
print(max(str))
print("*"+min(str)+"*")

#replace(oldstr,newstr,count)
#用newstr替换oldstr，默认是全部替换，若指定了count,则只替换前count个
str = "sunck is a nice nice nice man"
str1 = str.replace("nice","good",1)
print(str)
print(str1)

#创建一个字符串映射表
t1 = str.maketrans("ac", "65")
#a--6   c--5
str1 = "sunck is a good good good man"
str2 = str1.translate(t1)
print(str1)
print(str2)




#startswith(str, start = 0, end = len(str))
#endswith(str, start=0, eng=len(str))
#在给定范围内，判断是否以给定字符串开头/结尾，若没有指定范围，则默认整个字符串
str = "sunck is a good man"
print(str.startswith("sunck",5, 16 ))
print(str.endswith("man"))


#编码 encode(encoding="utf-8", errors="strict")
#解码  decode() 注：要与编码时的编码格式一致
str = "sunck is a good man凯"
data1 = str.encode("utf-8")
data2 = data1.decode("utf-8")
print(data1,data2)
data3 = str.encode("utf-8","ignore")   #ignore错误不处理
data4 = data3.decode("gbk", "ignore")
print(data3, data4)

#isalpha() 如果字符串中至少有一个字符且所有字符都是字母返回True,否则返回False
#isalnum() 如果字符串中至少有一个字符且所有字符都是字母或数字返回True,否则返回False
#isupper() 如果字符串中至少有一个英文字符且所有英文字符都为大写英文字母返回True,否则返回False
#islower() 如果字符串中至少有一个英文字符且所有英文字符都为小写英文字母返回True,否则返回False
str1 = "s13n"
str2 = "sjak"
str3 = "122"
print(str1.isalpha(), str2.isalpha(), str3.isalpha())
print(str1.isalnum(), str2.isalnum(), str3.isalnum())
print("ABH3".isupper(), "ABHa".isupper(), "ABH**".isupper())
print("zvsd3".islower(), "ABHa".islower(), "dfdx**".islower())

#istitle()
#如果字符串是标题化的返回True,否则返回False
print("sunck is".istitle(), "Sunck is".istitle(), "Sunck Is".istitle())

#isdigit()
#如果字符串值只包含数字字符的返回True,否则返回False
print("123".isdigit(), "h23".isdigit())

#isnumeric()
#如果字符串值只包含数字字符则返回True,否则返回False
print("1323".isnumeric(), "247a".isnumeric())

#isdecimal()
#如果字符串值只包含十进制字符则返回True,否则返回False
print("1323".isdecimal(), "247a".isdecimal())

#isspace()
#如果字符串中只包含空格则返回True,否则返回False
print("  ".isspace(), "\t".isspace(), "\n".isspace())





