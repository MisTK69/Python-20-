# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

a=list(input("甲方的數字："))
b=list(input("乙方的數字："))
e=""
for i in range(0,len(a)):
    if a[i]>b[i]:
        c="贏"
        e=e+c
    elif a[i]<b[i]:
        d="輸"
        e=e+d
    elif a[i]==b[i]:
        f="和"
        e=e+f
print("洗刷刷結果："+e)