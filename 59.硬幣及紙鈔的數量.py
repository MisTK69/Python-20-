# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

money=int(input(""))
a1 = money % 100
a2 = a1 % 50
a3 = a2 % 10
a4 = a3 % 5
a=0
b=0
if money//100!=0:
    a = money//100
    b += a        
if a1//50!=0:
    a = a1 // 50
    b+=a
if a2//10!=0:
    a = a2 // 10
    b+=a   
if a3//5!=0:
    a = a3 // 5
    b+=a
if a4//1!=0:
    a = a4 // 1
    b+=a 
print(b)
