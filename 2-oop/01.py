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
class PythonStudent():
    name = None  # 用None给不确定的值赋值
    age = 18
    course = "python"
    def DoHomeWork(self):  # 此处self是系统默认给定的
        print("我在做作业")
        return None   # 函数末尾加return

# 实例化一个叫anran的学生，是一个具体的人
anran = PythonStudent()
print(anran.age)
print(anran.name)
anran.DoHomeWork()  # 成员函数的调用没有传递进入参数
