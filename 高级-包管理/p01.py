# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/5/5
# 包含一个学生类    一个sayhello函数   一个打印语句
class Student():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age
    def say(self):
        print("My name is {0},my age is {1}".format(self.name, self.age))

def sayHello():
    print("Hi, 很高兴见到大家")

# 此判断语句建议一直作为程序的入口
if __name__ == "__main__":    # 作为主程序使用时后面的程序触发，但作为模块被导入时，后面的程序不自动触发
    print("希望大家今后多多关照!")