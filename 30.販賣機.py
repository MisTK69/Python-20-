# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""


dolar=int(input("小明身上有幾元："))
obj=int(input("販賣機有幾種飲料："))
list1=[]
a=0
for i in range(1,obj+1):
    p=int(input("請輸入第%d種飲料價格：" %(i)))
    list1.append(p)
    if list1[i-1] <= dolar:
        a += 1
print(a)