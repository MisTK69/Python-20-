# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

dict1 = {}
n = int(input("輸入n值："))
for i in range (1,n+1):
    a=input("請輸入姓名：")
    b=input("請輸入電子郵件：")
    dict1[a] = b
c=input("請輸入查詢電子郵件的姓名：")
if c in dict1:
    print(c+" 電子郵件帳號為 "+dict1[c])
