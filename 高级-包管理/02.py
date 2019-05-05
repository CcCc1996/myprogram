# -*- coding: utf-8 -*-
# Author: IMS2017-MJR
# Creation Date: 2019/5/5
import p01  # 导入这个模块，就相当于将模块中的代码粘贴到了这里并执行一遍，所以其中print等代码会直接执行，最好不要有。
stu = p01.Student("cjx", 22)
stu.say()
p01.sayHello()

print("#" * 50)

import p01 as p
stu = p.Student("anran", 22)
stu.say()
p.sayHello()

print("#" * 50)

from p01 import Student, sayHello
stu = Student("cwy", 0)  # 此时p01.的前缀都不需要，否则会报错
stu.say()
sayHello()