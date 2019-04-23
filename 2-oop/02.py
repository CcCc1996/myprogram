# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/4/22
# 继承的语法
# 在python中，任何类都有一个共同的父类叫object
class Person():
    name = "NoName"
    age = 18
    __score = 0   # 考试成绩是私有，只能自己知道
    _petname = "sec"   # 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("sleep..........")

# 父类写在括号内
print("*" *  50)
class Teacher(Person):
    teacher_id = "9527"
    name = "dana"
    def make_text(self):
        print("不准抄作业")
t = Teacher()
print(Teacher.name)
print(t._petname)    # 子类可以访问父类除私有成员外的所有内容，因此受保护的成员可以被访问
# print(t.__score)   # 公开访问私有成员，报错!!!
t.sleep()
print(t.teacher_id)
t.make_text()
print(t.name)    # 子类和父类成员同名时，优先使用子类，此处是dana，不是NoName

# 子类扩充父类功能案例
print("*" *  50)
class Person():
    def work(self):
        print("make some money")
class Teacher(Person):
    def make_text(self):
        print("不准抄作业")
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        # Person.work(self)
        # 扩充父类的另一种方法
        super().work()
        self.make_text()
t = Teacher()
t.work()

# 构造函数的概念
class Dog():
    # __init__就是构造函数
    # 每次实例化时，第一个被自动的调用
    # 因为每次工作是进行初始化，因此得名
    def __init__(self):
        print("I am init in dog")
print("*" *  50)
kaka = Dog()   # 无任何操作，自动被调用

# 继承中的构造函数——1
print("*" *  50)
class Animal():
    def __init__(self):
        print("都是动物")
class BuruAnimal(Animal):
    def __init__(self):
        print("哺乳动物")
class Dog(BuruAnimal):
    def __init__(self):
        print("I am init in dog")
kaka = Dog()  # 狗写了构造函数，直接调用自身的构造函数
class Cat(BuruAnimal):
    pass
meixi = Cat() # 猫没写构造函数，则继续向上查找，遵循就近原则

print("*" *  50)
class A():
    pass
class B(A):
    pass
print(B.__mro__)   # __mro__用于查询父子关系的函数