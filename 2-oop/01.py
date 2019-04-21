# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/4/16
"""
用来定义一个学生类，用来形容学生
"""
# 定义一个空的类
class Student():
    pass  # 此次pass必须有，否则报错
# 定义一个对象
anran = Student()

# 定义一个描述听python的学生的类
class Student():
    name = None  # 用None给不确定的值赋值
    age = 18
    course = "python"
    def DoHomeWork(self):  # 此处self是系统默认给定的
        print("我在做作业")
        return None   # 函数末尾加return

# 实例化一个叫anran的学生，是一个具体的人
anran = Student()
print(anran.age)
print(anran.name)
anran.DoHomeWork()  # 成员函数的调用没有传递进入参数
##############################
print(Student.__dict__)
print(anran.__dict__)
##############################
print(id(Student.age))
print(id(Student.name))
print("*" * 50)
print(id(anran.age))
print(id(anran.name))  # 此处id相同，说明指向的是同一个变量,但如果给anran中的属性赋和类中属性不同的值，则id会发生变化
anran.age = 18
anran.name = "anran"
print("*" * 50)
print(id(anran.age))
print(id(anran.name))
print(anran.__dict__)

class Student():
    def say(self):
        self.name = "cjx"   # 将self替换成cjx，此处变成 cjx.name
        self.age = 23
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
    def sayagain(s):
        print("my name is {0}".format(s.name))  # s也用cjx代替
        print("my age is {0}".format(s.age))
cjx = Student()
cjx.say()
cjx.sayagain()
print("*" * 50)


class Teacher():
    name = "dana"
    age = 40
    def say(self):
        self.name = "yaona"
        self.age = 23
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
    def sayagain():  # 此处为绑定类方法
        print("hello,nice to see you")
t = Teacher()
t.say()
Teacher.sayagain()  # 调用绑定类方法必须使用类名.

print("*" * 50)

# 关于self的案例
class A():
    name = "liuying"
    age = "40"
    def __init__(self):
        self.name = "aaaa"
        self.age = "1000"
    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbb"
    age = "2000"
a = A()
a.say()  # 此时，系统会把a作为第一个参数传入函数
A.say(a) # 此时，self被a代替
A.say(A) # 同样可以把A作为参数传入
A.say(B) # 传入的是类B，但B具有同样的name和age属性，所以不会报错

#  以上代码，利用了鸭子模型

# 私有成员案例
print("*" * 50)
class Person():
    name = "liuying"
    __age = 18
p = Person()
print(p.name)
#  print(p.__age)  # 报错信息为：类中没有age属性

# name mangling技术
print(Person.__dict__)  # 使用dict命令查询age改名后名称
print(p._Person__age)  # 此时就能访问到改名后的age属性信息
p._Person__age = 22   # 还可以修改
print(p._Person__age)