# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

a1=int(input("請輸入第一個要判斷的數字："))
a2=int(input("請輸入第二個要判斷的數字："))
a3 = a1 % 2
a4 = a2 % 2
if a3 == 0 or a4 == 0:
    print("N")
else:
    print("Y")