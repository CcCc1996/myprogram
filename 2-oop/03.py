# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/4/23

# 多继承的例子
# 子类可以直接拥有父类的属性和方法，私有的属性和方法除外
class Bird():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print("i can fly")
class Fish():
    def __init__(self, name):
        self.name = name
    def swim(self):
        print("i can swim")
class Person():
    def __init__(self, name):
        self.name = name
    def work(self):
        print("i can do work")
class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name

s = SuperMan("cjx")
s.fly()
s.swim()
s.work()

# 单继承的例子
class Flog(Fish):
    def __init__(self, name):
        self.name = name
f = Flog("anran")
f.swim()

# 构造函数的补充
print("*" * 50)
class A():
    def __init__(self, name):
        print("A")
        print(name)
class B(A):
    def __init__(self, name):
        A.__init__(self, name)  # 首先调用父类构造函数，或也可以使用super实现
        super(B, self).__init__(name)
        print ("这是A的构造函数")
b = B("A的名字")

# Mixin案例
