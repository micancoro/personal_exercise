#2019-5-7
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
f = float(input('请输入华氏温度:'))
c = (f-32)/1.8
print '华氏温度：%.1f,摄氏温度：%.1f\n' %(f,c)

"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
r = float(input('请输入半径：'))
c = 2 * math.pi * r
s = math.pi * r * r
print '半径为：%.1f, 圆周长为： %.3f， 圆面积为： %.3f' %(r,c,s)

"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
year = int(input('请输入年份：'))
if year%4 == 0 and year%100 != 0:
	print True
elif year%400 == 0:
	print True
else:
	print False

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)

"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
l = float(input('请输入长度：'))
chose = int(input('请选择单位：\n 1：英寸\n 2：厘米\n'))
if chose == 1:
	print '%.3f 英寸 = %.3f 厘米\n' %(l, 2.54*l)
elif chose == 2:
	print '%.3f 厘米 = %.3f 英寸\n' %(l, l/2.54)
else:
	print 'Error, boy'

"""
掷骰子决定做什么事情

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
fate = random.randint(1,6)
print '开始掷骰子..\n点数为：%d\n你需要：\n' %fate
if fate == 1:
	print '学猫叫\n'
elif fate == 2:
	print '跳支舞\n'
elif fate == 3:
	print '唱首歌n'
elif fate == 4:
	print '讲笑话\n'
elif fate == 5:
	print '原地自爆\n'
else:
	print '挂机\n'

"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
result = float(input('请输入你的成绩：\n'))
if result >= 90:
	level = 'A'
elif result >= 80:
	level = 'B'
elif result >= 70:
	level = 'C'
elif result >= 60:
	level = 'D'
else:
	level = 'E'
print ('你的等级为: ' ,level)

"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
a = float(input('请输入第一条边长：\n'))
b = float(input('请输入第二条边长：\n'))
c = float(input('请输入第三条边长：\n'))
is_tra = (a+b > c or a+c > b or b+c >a and a-c < b or a-b < c or b-c <a)
if is_tra:
	p = a+b+c
	t = p / 2
	s = math.sqrt(t * (t-a) * (t-b) * (t-c))
	print '可以构成三角形，周长为: %.3f，面积为：%.3f\n' %(p, s)
else:
	print '不能构成三角形\n'

"""
输入月收入和五险一金计算个人所得税

Version: 0.1
Author: 骆昊
"""
"""
输入一个正整数判断它是不是素数
Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
c = int(input('请输入一个正整数:\n'))
for x in range(1, c+1):
	if c % x == 0 and x != c and x != 1:
		print '%d不是一个素数\n' %c
		break
	elif x == c:
		print '%d是一个素数\n' %c

"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
line = int(input('请输入行数：\n'))
print '第一种三角形：\n'
for x in range(line):
	for t in range(x):
		print '*'

#2019-5-8

寻找“水仙花数”。
#!/usr/bin/python
# -*- coding: utf-8 -*-
# 水仙花数：水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
print '三位水仙花数为：\n'
for x in range(100, 1000):
	bw = int(x/100)
	sw = int((x - 100 * bw) / 10)
	gw = x - 100 * bw - 10 * sw
	if (bw ** 3 + sw ** 3 + gw ** 3) == x:
		print '%d\n' %x

寻找“完美数”。
#!/usr/bin/python
# -*- coding: utf-8 -*-
#完美数：它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身
#约数：约数，又称因数。整数a除以整数b(b≠0) 除得的商正好是整数而没有余数，我们就说a能被b整除，或b能整除a。a称为b的倍数，b称为a的约数
print '一万以内的完美数为：\n'
for x in range(1, 10001):
	sum = 1
	for t in range(2, x):
		if x % t == 0:
			sum += t
	if sum == x:
		print '%d\n' %x

“百钱百鸡”问题。
#!/usr/bin/python
# -*- coding: utf-8 -*-
#百钱百鸡：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
max_gj = int(100 / 5)
max_mj = int(100 / 3)
max_xj = int(3 * 100)
for x in range(max_gj + 1):
	for y in range(max_mj + 1):
		for z in range(3 , max_xj + 1, 3):
			if z / 3 + 3 * y + 5 * x == 100 and x + y + z == 100:
				print '鸡翁%d只，鸡母%d只，鸡雏%d只\n' %(x, y, z)

生成“斐波拉切数列”。
#!/usr/bin/python
# -*- coding: utf-8 -*-
#斐波拉切数列：数列为：1,1,2这个数列从第3项开始，每一项都等于前两项之和。
print '斐波拉切数列为：\n'
list = [1,1]
for x in range(3, 11):
	list.append(list[x-2] + list[x-3])
print list

Craps赌博游戏。
#!/usr/bin/python
# -*- coding: utf-8 -*-
#规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输庄家胜。若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。
import random
first_1 = random.randint(1,6)
first_2 = random.randint(1,6)
first_sum = first_1 + first_2
endgame = True
print 'Craps赌博游戏开始...!!!\n按回车键开始掷骰子'
raw_input()
print '第一次掷骰子....\n第一个骰子点数为：%d,第二个骰子点数为：%d' %(first_1, first_2)
if first_sum == 7 or first_sum == 11:
	print '玩家胜利'
	endgame = False
if first_sum == 2 or first_sum == 3 or first_sum == 12:
	print '庄家胜利'
	endgame = False
while (endgame):
	print '未决胜负，按回车键继续掷骰子...\n'
	raw_input()
	first = random.randint(1,6)
	second = random.randint(1,6)
	sum = first + second
	print '第一个骰子点数为：%d,第二个骰子点数为：%d' %(first, second)
	if sum == first_sum:
		print '玩家胜利'
		break
	if sum == 7:
		print '庄家胜利'
		break
print '游戏结束'

练习1：实现计算求最大公约数和最小公倍数的函数。
#!/usr/bin/python
# -*- coding: utf-8 -*-
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)

练习2：实现判断一个数是不是回文数的函数
#!/usr/bin/python
# -*- coding: utf-8 -*-
def is_huiwen(num):
	tmp = num
	sum_all = 0
	while(tmp > 0):
		sum_all = sum_all * 10 + tmp % 10
		tmp = tmp / 10
	return sum_all == num
a = input('请输入一个正整数：\n')
print is_huiwen(a)

练习3：实现判断一个数是不是素数的函数。
#!/usr/bin/python
# -*- coding: utf-8 -*-
def is_sushu(num):
	if num == 2 or num == 3:
		return True
	for x in range(2, num):
		if num%x == 0:
			return False
	return True
#a = int(input('请输入一个大于1的自然数：\n'))
for x in range(2, 100):
	if is_sushu(x):
		print x

练习4：写一个程序判断输入的正整数是不是回文素数。
def is_huiwen_and_sushu(num):
	if is_sushu(num) and is_huiwen(num):
		return True
	else:
		return False
a = int(input('请输入一个正整数：\n'))

练习1：在屏幕上显示跑马灯文字
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os

def paomadeng():
	content = '这是一个屏幕保护程序'
	while(True):
		os.system('clear')
		print(content)
		content = content[1:] + content[0]
		time.sleep(0.05)
paomadeng()

#2019-5-8
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

def make_yzm_list(code_long, code_ku):
	code = []
	for x in range(code_long):
		code.append(random.choice(code_ku))
	return code

def make_yzm_str(code_long, code_ku):
	code = ''
	for x in range(code_long):
		code += random.choice(code_ku)
	return code

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z','y','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
b = int(input('请输入验证码长度：\n'))
#print make_yzm_list(b, a)
print make_yzm_str(b, a)

练习3：设计一个函数返回给定文件名的后缀名。
#!/usr/bin/python
# -*- coding: utf-8 -*-

def return_type(file_name):
	extend = ''
	for x in file_name[::-1]:
		if x != '.':
			extend += x
		else:
			break
	return extend[::-1]

a = raw_input('请输入文件名：\n')
print '文件后缀名为：' + return_type(a) 

练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
#!/usr/bin/python
# -*- coding: utf-8 -*-

def max_and_second(list):
	a = 0
	b = 0
	for x in list:
		if x > a:
			a = x
	for y in list:
		if y > b and y != a:
			b = y
	return a, b
a = [1,4,3,5,6,2]
print max_and_second(a)

练习5：计算指定的年月日是这一年的第几天
#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_runyear(year):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		return True
	else:
		return False

def sum_the_days(year,month, day):	
	sum_day = day
	for x in range(1, month+1):
		if x == [6, 8, 9, 11]:
			days = 30
		elif x == 2:
			if is_runyear(year):
				days = 29
			else:
				days = 28
		else:
			days = 31
		sum_day += days
	return sum_day

a = input('输入年份\n')
b = input('输入月份\n')
c = input('输入日份\n')
print '今年是%d的第%d天\n' %(a, sum_the_days(a, b, c))

练习6：打印杨辉三角。
#!/usr/bin/python
# -*- coding: utf-8 -*-

综合案例2：约瑟夫环问题
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
def lucky_guys():
	the_line = [1] * 30
	dead = 0
	count = 0
	line_shot = 0
	while (line_shot < 30):
		count += 1
		if count == 9:
			the_line[line_shot] = 0
			dead += 1
			count = 0
		line_shot += 1
		if line_shot == 30:
			line_shot = 0
		if dead == 15:
			return the_line

if __name__ == '__main__':
	print lucky_guys()

综合案例3：井字棋游戏

练习1：定义一个类描述数字时钟
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

class Clock(object):
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def run(self):
		self.seconds += 1
		if self.seconds > 59:
			self.minutes += 1
			self.seconds = 0
		if self.minutes > 59:
			self.hours += 1
			self.minutes = 0
		if self.hours > 23:
			self.hours = 0
		
	def watch(self):
		print '现在是%d点%d分%d秒\n' %(self.hours, self.minutes, self.seconds)

if __name__ == '__main__':
	time_now = Clock(23, 59, 58)
	while(True):
		time_now.run()
		time_now.watch()
		time.sleep(1)

#2019-5-13
练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

class Point(object):

	def __init__(self, x=0, y=0):
		print 'init Ok...'
		self.x = x
		self.y = y

	def move_left(self):
		self.x -= 1
		print 'now you location is (%d, %d)' %(self.x, self.y)

	def move_right(self):
		self.x += 1
		print 'now you location is (%d, %d)' %(self.x, self.y)

	def move_up(self):
		self.y += 1
		print 'now you location is (%d, %d)' %(self.x, self.y)

	def move_down(self):
		self.y -= 1
		print 'now you location is (%d, %d)' %(self.x, self.y)

	def distance(self, x, y):
		s = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
		print 'the distance between (%d, %d) is %d' %(x, y, s)

	def move_to(self, x, y):
		self.x = x
		self.y = y
		print 'now you location is (%d, %d)' %(self.x, self.y)

	def distance_to(self, that):
		s = math.sqrt(float((self.x - that.x) ** 2 + (self.y - that.y) ** 2))
		print 'the distance between (%d, %d) is %.1f' %(that.x, that.y, s)		

if __name__ == '__main__':
	point1 = Point()
	point1.move_left()
	point1.move_up()

	point2 = Point()
	point2.move_to(12,8)
	point2.distance_to(point1)

#2019-5-14
