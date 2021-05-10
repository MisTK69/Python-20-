# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

list1=[]
list2=[]
n = int(input("輸入筆數n："))
for i in range (0,n):
    obj,num=input("").split(" ")
    list1.append(obj)
    list2.append(num)
for j in range(len(list1)):
    print(str(list1[j])+"牌得到"+str(list2[j])+"面")