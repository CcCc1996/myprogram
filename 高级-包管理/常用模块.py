# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/5/6

# 日历模块
# calendar  获取一年的日历字符串
# w = 每个日期之间的间隔字符数
# l = 每周所间隔的行数
# c = 每个月之间间隔的字符数
import calendar
cal = calendar.calendar(2019, l=0, c=3)
print(cal)
# isleap：判断是否是闰年
print(calendar.isleap(2000))
# leapdays：判断两年份直接闰年个数
print(calendar.leapdays(1998, 2019))

m3 = calendar.month(2019, 5)  # 获取某个月份的日历
print(m3)

mr = calendar.monthrange(2019, 5)  # 获取该月份是从周几开始，和该月总天数
print(mr)

list = calendar.monthcalendar(2019, 5)
for i in list:
    print(i)

calendar.prmonth(2019, 5)
print(calendar.weekday(2019, 5, 6))


# time模块
# 时间戳，使用比较多，是从1970年1月1日0时0分0秒至今的秒数，根据不同语言，可以是整数或者浮点数
# 32位操作系统能够支持到2038年

# UTC时间，中国时间是UTC+8 东八区

# 时间元组，一个包含时间内容的普通元组

import time
# 时间模块的属性，timezone：当前时区和UTC时间相差得描述，在没有夏令时的情况下的间隔
print(time.timezone)
# 得到时间戳
print(time.time())
# localtime,得到当前时间的时间结构
t = time.localtime()
print(t)
print(t.tm_hour)
# 字符串化之后的当前时间格式
tt = time.asctime()
print(tt)
tt = time.ctime()
print(tt)

# sleep:使程序进入睡眠，N秒后继续
t0 = time.perf_counter() # 得到时间戳
time.sleep(1)
t1 = time.perf_counter()
print(t1 - t0)

# strftime：将时间元组进行自定义的字符串格式化
t = time.localtime()
ft = time.strftime("%Y %m %d  %H:%M")
print(ft)

from datetime import datetime, timedelta
t1 = datetime.now()
td = timedelta(hours=1)  # 一个小时的时间间隔
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))



# timeit——时间测量工具
# 案例，两种列表生成方法的比较
import timeit
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
# 利用timeit调用代码，执行10000次，查看运行时间。
# stmt=表示要测量的代码内容，以字符串形式出现
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=10000)
t2 = timeit.timeit(stmt=c, number=10000)
print(t1)
print(t2)