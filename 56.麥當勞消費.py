# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

dict1 = {"1A":"127","1B":"140","2A":"117","2B":"130",
         "3A":"137","3B":"150","4A":"99","4B":"112",
         "5A":"115","5B":"128"}
m=input("請選擇主餐及升級的套餐：")
if m in dict1:
    a = int(dict1[m])
d=input("是否升級成大杯飲料：")
if d == "是":
    b = a + 7
else:
    b = a
f=input("是否換成大薯：")
if f == "是":
    c = b + 13
else:
    c = b
print("總共為"+str(c)+"元")
