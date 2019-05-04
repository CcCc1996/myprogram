# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/5/4
class A():
    def __init__(self):
        self.name = "cjx"
        self.age = 22
    def fget(self):
        print("我被调用了")
        return self.name
    def fset(self, name):
        print("我被写入了")
        self.name = "图灵学院：" + name
    def fdel(self):
        pass
    # property 必须严格遵循 读取、写入、删除、DOC的顺序
    name2 = property(fget, fset, fdel, "这是一个property的例子")
a = A()
a.name2 = "anran"
print(a.name2)

# 抽象类的实现
import abc
# 声明一个抽象类，并且指定当前类的元类，此处为固定格式
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象方法
    @abc.abstractmethod
    def smoke(self):
        pass
    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass


# 类的组装
from types import MethodType
class A():
    pass
def say(self):
        print("say.......")
a = A()
a.say = MethodType(say, A)
a.say()

