'''
os：包含了普遍的操作系统的功能
'''

import os
# 获取操作系统类型
print(os.name)    # nt      # 说明是windows系统
                  # posix   #说明是Linux、Unix或者Mac OS X

#打印操作系统详细的信息
# print(os.uname())   #需要在Linux系统上执行

#获取操作系统中所有的环境变量
print(os.environ)
'''
结果：environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\asus-pc\\AppData\\Roaming', 'CLASSPATH': 'G:\\l
'''

#获取操作系统中的指定环境变量
print(os.environ.get("AppData"))        # C:\Users\asus-pc\AppData\Roaming

# 获取当前目录    ./a/
print(os.curdir)    # .

#获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())   # C:\Users\asus-pc\Desktop\python\OS模块与窗口控制与内存修改与语言

#以列表的形式返回指定目录下的所有的文件
print(os.listdir(r"C:\Users\asus-pc\Desktop\python\while,条件循环语句，turtle"))  #path前要加r,以防止转义
'''
结果：['turtle绘图.py', 'while语句.py', '__pycache__', '条件控制语句.py', '练习2.py', '练习if.py']
'''

# 在当前目录下创建新目录
# os.mkdir("sunck")   #在当前目录下创建了名为sunck的新目录
#删除目录
# os.rmdir("sunck")    #在当前目录删除了名为sunck的目录

#获取文件属性
# print(os.stat("sunck"))
'''结果：
os.stat_result(st_mode=16895, st_ino=12384898975319242, st_dev=4108229110, st_nlink=1, st_uid=0, st_gid=0, st_size=0,
'''

#重命名
# os.rename("sunck", "kai")   #名为sunck的目录重命名为kai

# 删除普通文件
# os.remove("file1.txt")

#运行shell命令
# os.system("notepad")    #打开记事本
# os.system("mspaint")     #打开画板
# os.system("write")     #打开写字板
# os.system("msconfig")   #打开系统设置
# os.system("shutdown -s -t 1")   #定时关机
# os.system("shutdown -a")   #自动关机被取消
# os.system("taskkill /f /im notepad.exe")   #关闭记事本
                            #想关哪个就在在任务管理器里找名字
#有些方法存在于os模块里，还有些存在于os.path
#查看当前的绝对路径
print(os.path.abspath("./kai"))        # C:\Users\asus-pc\Desktop\python\OS模块与窗口控制与内存修改与语言\kai

#拼接路径
p1 = r"C:\Users\asus-pc\Desktop\python\OS模块与窗口控制与内存修改与语言"
p2 = "kai"
# 注意：参数2开始不能有斜杠
print(os.path.join(p1, p2))    # C:\Users\asus-pc\Desktop\python\OS模块与窗口控制与内存修改与语言\kai
p3 = "/root/sunck/home"
p4 = "kai"
print(os.path.join(p3, p4))    # /root/sunck/home\kai

#拆分路径
path2 = r"C:\Users\asus-pc\Desktop\python\OS模块与窗口控制与内存修改与语言.txt"
print(os.path.split(path2))    # ('C:\\Users\\asus-pc\\Desktop\\python', 'OS模块与窗口控制与内存修改与语言.txt')

# 获取扩展名
path2 = r"C:\Users\asus-pc\Desktop\python\OS模块与窗口控制与内存修改与语言.txt"
print(os.path.splitext(path2))    # ('C:\\Users\\asus-pc\\Desktop\\python\\OS模块与窗口控制与内存修改与语言', '.txt')

#判断是否是目录
print(os.path.isdir(path2))      # False

#判断文件是否存在
path2 = r"C:\Users\asus-pc\Desktop\python\OS模块与窗口控制与内存修改与语言\os模块.py"
print(os.path.isfile(path2))    # True

#判断目录是否存在
path2 = r"C:\Users\asus-pc\Desktop\python"
print(os.path.exists(path2))     # True

#获得文件大小（字节）
path2 = r"C:\Users\asus-pc\Desktop\python"
print(os.path.getsize(path2))    # 8192

#获得文件的目录
path2 = r"C:\Users\asus-pc\Desktop\python"
print(os.path.dirname(path2))      # C:\Users\asus-pc\Desktop
#获得文件名
print(os.path.basename(path2))     # python









