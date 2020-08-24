'''
值传递：传递不可变类型
    string, tuple, number是不可变的

'''
def fun1(num):
    print(id(num))    #140720777098080
    num = 10
    print(id(num))    #140720777097760

tem = 20
print(id(tem))    #140720777098080
fun1(tem)  #num = tem
print(tem)   #20

'''
引用传递：传递可变类型
    list, dict, set是可变的
'''
def func2(lis):
    lis[0] = 100
li = [1,2,3,4,5]
func2(li)
print(li)    #[100, 2, 3, 4, 5]
