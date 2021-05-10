# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

km = float(input("請輸入路程公里數(km)："))
fee = 75
if km < 1.5:
    fee=75
else:       
    diff=km-1.5
    if diff%0.25==0:
        fee+=(diff//0.25)*5
    else:
        fee+=((diff//0.25)+1)*5
print("總共車資為:"+str(int(fee)))
