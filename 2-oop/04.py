# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/4/24
# 属性案例
# 创建Student类，描述学生类
# 学生具有Student.name属性
# 但name的格式并不统一

# 此例子使用的是增加一个函数，然后自动调用的方式，但很蠢
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.setname(name)  # 内部直接调用自身

    def setname(self, name,):
        self.name = name.upper()  # 名字变成大写

    def intro(self):
        print("hi,my name is {0}".format(self.name))
s1 = Student("Liu Ying", 19)
s2 = Student("michi stangle", 24)
s1.intro()
s2.intro()


# property案例
# 定义一个Person类，具有name，age属性
# 对于任意输入的姓名，希望能用大写保存
# 年龄，希望内部统一用整数保存
# x = property(fget, fset, fdel, doc)

class Person():
    def fget(self):
        return self._name * 2
    def fset(self, name):
        self._name = name.upper()
    def fdel(self):
        self._name = "NoMame"
    name = property(fget, fset, fdel, "对name进行以下操作")

p1 = Person()
p1.name = "TshdsdwY"
print(p1.name)


# 作业
# 1. 在用户输入年龄时，可以输入整数，小数，浮点数
# 2. 内部数据清洗，直接舍去小数，保持整数
class Person():
    '''
这是一个人，一个高尚的，脱离了低级趣味的人。
    '''
    def fget(self):
        return self._age
    def fset(self, age):
        self._age = int(age)
    def fdel(self):
        self._age = "NoAge"
    age = property(fget, fset, fdel, "对name进行以下操作")
p1 = Person()
p1.age = 22.4
print(p1.age)

# 类的内置属性举例
print(Person.__dict__)
print(Person.__doc__)  # 打印这个类的说明文档

# 魔法函数距离举例：
class A():
    def __init__(self):
        print("这是我第一次被自动调用")
    def __call__(self):
        print("这是我第二次被自动调用")
    def __str__(self):
        return("这是我第三次被自动调用")
a = A()
a()  # 此处变量a直接作为函数使用
print(a)

# __getattr__
print("*" * 50)
class A():
    name = "cjx"
    age = "22"
    def __getattr__(self, item):
        print("没有该属性")
        print(item)
a = A()
print(a.name)
print(a.addr)

## 作业：为什么会打印第四句话，而第四局话是 None？？？

# __setattr__案例

