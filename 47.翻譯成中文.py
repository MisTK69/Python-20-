# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

dict1 = {}
n = int(input("輸入筆數n："))
for i in range (1,n+1):
    eng=input("請輸入英文：")
    chi=input("請輸入中文：")
    dict1[eng] = chi
s=input("請輸入查詢單字：")
if s in dict1:
    print(s+"中文意思"+dict1[s])
else:
    print("字典未有此單字")