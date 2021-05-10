# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

dict1 = {}
n = int(input("輸入筆數n："))
for i in range (1,n+1):
    obj,num=input("").split(" ")
    dict1[obj] = num
item1 = list(dict1.items())
for n1, n2 in item1:
    print(str(n1)+"牌得到"+str(n2)+"面")