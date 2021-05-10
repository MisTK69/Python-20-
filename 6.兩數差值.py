# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:02:49 2020

@author: 陳博劭
"""

s1=""
n=input("輸入值為:").split(",")
n.sort()
m=list(n)
m.reverse()
minn=int(s1.join(n))
maxx=int(s1.join(m))
print("最大值數列與最小值數列差值為:"+str(maxx-minn))
