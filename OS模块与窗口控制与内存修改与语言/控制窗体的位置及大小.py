import win32con
import win32gui
import time
QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")

#参数1：控制的窗体
#参数2：大致方位，HWND_TOPMOST上方
#参数3：位置x
#参数4：位置y
#参数5：长度
#参数6：宽度
win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 10,10,6,3,win32con.SWP_SHOWWINDOW)