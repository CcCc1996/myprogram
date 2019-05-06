# 1. 模块
- 一个模块就是一个包含python代码的文件，后缀名称是.py就可以，模块就是个python文件
- 为什么要使用模块
    - 程序太大，编写维护非常不便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
- 如何使用模块
    - 模块直接导入使用
        - 假如模块名称直接以数字开头，需借助importlib包进行名称替换
             import importlib
             pp01 = importlib.import_module("01")  此时01被pp01进行了替换
    - 语法
            
            import module_name
            module_name.function_name
            module_name.class_name
    - import 模块名 as 别名
        - 导入的同时给模块起一个别名，其余用法跟第一中相同
        - 案例见02.py
      
    - from module_name import func_name,class_name
        - 想使用模块中哪个就只导入哪个，案例02.py
        - from module_name import *   （导入模块内的所有内容）
        
-   " if __name__ == '__main__' "的使用
    - 可以有效解决模块代码被导入时被动执行的问题
    - 建议所有程序都已此代码作为程序入口

## 1.1 模块的搜索路径和存储
- 什么是模块的搜索路径，
    - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径

        import sys
        sys.path 属性可以获取路径列表
        # 案例03.py
- 添加搜索路径

        sys.path.append(dir)
- 模块的加载顺序
    - 1.搜索内存中已经加载好的模块
    - 2.python的内置模块
    - 3.搜索sys.path路径
    
# 2. 包
- 包是一种组织管理代码的方式，包里存放的就是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

        |---包
        |---|--- __init__.py  包的标志文件
        |---|--- 模块1
        |---|--- 模块2
        |---|--- 子包(子文件夹)
        |---|---|--- __init__.py  包的标志文件
        |---|---|--- 子包模块1
        |---|---|--- 子包模块2
        
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式是：
        
                package_name.func_name()
                package_name.class_name.func_name()
        - 案例pkg01，04.py
        
    - import package_name as 别名，改名操作和模块相同
    - 注意此种导入方法是默认对__init__.py内容的导入
    
    - import package.module 
        - 导入包中某一个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.func()
                package.module.class.var
        - 案例05.py
        
- from package import module导入
    - 此种导入方法不执行__init__的内容
- from package import *
    - 导入当前包__init__文件中所有的函数和类，其余包不导入
    - 案例06.py
- from package。module import *
    - 导入包中指定的模块中的所有内容
    
- 在开发环境中经常会使用其他模块，可在当前包中直接导入其他模块中的内容
    - import 完整的包或模块的路径

- `__all__` 的用法
    - 在使用from package import * 的时候，* 可以导入的内容
    - `__init__.py`  中如果文件为空，或者没有`__all__` ，那么只可以把`__init__.py` 中的内容导入
    - `__init__`  如果设置了`__all__` 的值，那么则按照`__all__` 指定的子包或者模块进行，
    如此则不会载入`__init__` 中的内容  
    - `__all__=['module1', 'module2', 'package1', .......]` 
    
# 3. 命名空间
- 由于区分不同位置不同功能但名称相同的函数或变量的一个特定前缀
- 作用是防止命名冲突 

# 4. 常用模块
- calendar  跟日历相关的模块
- time  
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用理论上都应该先导入，srting是特例