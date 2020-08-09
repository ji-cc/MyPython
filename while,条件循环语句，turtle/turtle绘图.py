'''
turtle:简单的绘图工具
提供一个小海龟，可以把它理解为一个机器人，只能听懂有限的命令
绘图窗口的原点在正中间，默认海龟的方向是右侧
方法：
    运动命令
        forward(d)  向前移动d长度
        backward(d)  向后移动d长度
        right(d)   向右转动多少度
        left(d)    向左转动多少度
        goto(x,y)   移动到坐标为(x,y)的位置
        speed(speed) 笔画绘制的速度[0,10]
    笔画控制命令
        up()  笔画抬起，在移动的时候不会绘图
        down()   笔画落下，移动绘图
        setheading(d)  改变海龟朝向
        pensize(d)   笔画的宽度
        pencolor(colorstr)   笔画颜色
        reset() 恢复所有设置，清空窗口，重置turtle状态
        clear() 清空窗口，不会重置turtle
        circle(r, steps=e)  绘制圆形 r为半径，steps=e为边（可以不写） eg:e=3时为三边形

        begin_fill()   开始填充
        filcolor(colorstr)   填充颜色
        end_fill()    结束填充

    其他命令
        done()     程序继续执行
        undo()   撤销上一次动作
        hideturtle()  隐藏海龟
        showturtle()   显示海龟
        screensize(x,y)  设置画图的屏幕大小
'''
#导入turtle库
import  turtle
turtle.speed(10)
turtle.backward(100)
turtle.right(45)
turtle.goto(-100,200)
turtle.up()
turtle.goto(20,100)
turtle.down()
turtle.pencolor("red")
turtle.pensize(10)
turtle.forward(50)
turtle.circle(50)
turtle.setheading(50)
turtle.pensize(1)

turtle.goto(-200,50)

turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(50,steps=5)
turtle.end_fill()

# turtle.clear()
# turtle.reset()
turtle.done()







