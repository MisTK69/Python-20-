# -*- coding: utf-8 -*-
"""
@author: 陳劭
"""

n = input("輸入一整數序列為:").split(" ")
list1=[]
for i in range(len(n)):
    c=n.count((n[i]))
    list1.append(c)
b=max(list1)
if b>(len(n)/2):    
    a = list1.index(b)
    print("過半元素為:"+n[a])
else:
    print("過半元素為:NO")
