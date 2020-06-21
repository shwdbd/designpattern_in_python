#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   factory.py
@Time    :   2020/06/21 11:27:56
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   工厂模式范例

类 AnlimalFactory是工厂类，有一个getAnlimal()函数根据不同的参数返回不同的动物实例

Anlimal是抽象的类，有action函数，子类必须继承。

'''


class AnlimalFactory:
    """工厂类
    """

    @staticmethod
    def getAnlimal(anlimal_type):
        """工厂函数，根据传入参数新建不同的动物实例

        Args:
            anlimal_type ([type]): [description]
        """
        if anlimal_type == "cat":
            return Cat()
        elif anlimal_type == "tiger":
            return Tiger()
        else:
            return Anlimal()


class Anlimal:
    """动物的抽象类
    """

    def action(self):
        return "未知的动作"


class Cat(Anlimal):
    """猫
    """

    def action(self):
        return "抓老鼠"


class Tiger(Anlimal):
    """老虎
    """

    def action(self):
        return "吃人"


if __name__ == "__main__":
    # 猫
    cat = AnlimalFactory.getAnlimal("cat")
    print(cat)
    print(cat.action())

    # 老虎
    tiger = AnlimalFactory.getAnlimal("tiger")
    print(tiger)
    print(tiger.action())

    # 默认的动物
    unkown_anlimal = AnlimalFactory.getAnlimal("xxx")
    print(unkown_anlimal)
    print(unkown_anlimal.action())
