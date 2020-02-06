# -*- coding: utf-8 -*-

#  list1 和list2 两个list ， 想要得到list1是不是包含 list2  （是不是其子集 )

a = [1, 2]
b = [1, 2, 3]
c = [0, 1]

set(b) > set(a)  # True
set(b) > set(c)  # False
