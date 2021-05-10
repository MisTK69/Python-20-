# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

a=int(input("輸入一正整數："))
b=a%2
c=a%11
d=a%5
e=a%7
if b==0 and c==0:
    if d!=0 and e!=0:
        print(str(a)+"為新公倍數?:Yes")
    else:
        print(str(a)+"為新公倍數?:No")
else:
    print(str(a)+"為新公倍數?:No")