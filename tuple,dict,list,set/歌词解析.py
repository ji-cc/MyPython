#歌词解析
musicLrc = """[00:01.32][00:01.33][00:01.34]白月光-张信哲
[00:31.45]白月光
[00:33.09]心里某个地方
[00:37.33]那么亮
[00:39.35]却那么冰凉
[00:43.72]每个人
[00:45.83]都有一段悲伤
[00:50.16]想隐藏
[00:52.10]却欲盖弥彰
[00:56.66]白月光
[00:58.61]照天涯的两端
[01:02.98]在心上
[01:04.91]却不在身旁
[01:09.60]擦不干
[01:11.35]你当时的泪光
[01:15.78]路太长
[01:17.69]追不回原谅
[01:23.05]你是我
[01:24.98]不能言说的伤
[01:29.31]想遗忘
[01:31.42]又忍不住回想
[01:35.81]像流亡
[01:37.89]一路跌跌撞撞
[01:41.79]你的捆绑
[01:45.11]无法释放
[01:51.05]白月光
[01:53.11]照天涯的两端
[01:57.54]越圆满
[01:59.36]越觉得孤单
[02:03.81]擦不干
[02:05.83]回忆里的泪光
[02:10.04]路太长
[02:12.01]怎么补偿
[02:43.33]你是我
[02:45.02]不能言说的伤
[02:49.33]想遗忘
[02:51.34]又忍不住回想
[02:55.78]像流亡
[02:57.77]一路跌跌撞撞
[03:01.79]你的捆绑
[03:04.94]无法释放
[03:11.42]白月光
[03:12.91]心里某个地方
[03:17.35]那么亮
[03:19.23]却那么冰凉
[03:23.60]每个人
[03:25.57]都有一段悲伤
[03:30.17]想隐藏
[03:32.28]却在生长
"""
lrcdict = {} #创建空字典
musiclist = musicLrc.splitlines()
#print(musiclist)
#以时间作为key,歌词作为value
#先一行一行处理，以]为切割符切割
#[00:01.32][00:01.33][00:01.34]白月光-张信哲
#[00:01.32  [00:01.33   [00:01.34   白月光-张信哲
for lrcline in musiclist:
    lrclinelist = lrcline.split("]")  #一句歌词可能对应几个时间
    # print(lrclinelist)
    for index in range(len(lrclinelist) - 1):  #取出时间  #range(4) = 0,1,2,3
        timestr = lrclinelist[index][1:]
        # print(timestr)
        #00:01.32
        timelist = timestr.split(":")
        time = float(timelist[0]) * 60 + float(timelist[1])  #换算：00:01.32=1.32秒
        # print(time)
        #存入字典
        lrcdict[time] ={ lrclinelist[-1] }   #lrclinelist[-1]表示lrclinelist里最后一个元素=歌词

print(lrcdict)
alltimelist = []  #创建空列表
for t in lrcdict:     #遍历时间
    alltimelist.append(t)   #歌词表里所有时间存入空列表中
alltimelist.sort()   #把时间排序
# print(alltimelist)
while 1:
    gettime = float(input("请输入一个时间："))
    #因为输入的时间在歌词表里不一定存在
    for n in range(len(alltimelist)):      #n为alltimelist列表的下标
        temptime = (alltimelist[n])
        if temptime > gettime:
            break     #循环过程中当输入的结果小于时间表里的某一个值时，循环结束
    #结果取第n-1个值  eg: 输入32时，取31.45秒对应的歌词
    if n == 0:
       pass  #表示空语句
    else:
        print(lrcdict[alltimelist[n - 1]])