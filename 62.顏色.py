# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 02:13:09 2020

@author: 陳博劭
"""

dict1={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
print(dict1.keys())
data1=input("請輸入水果：")
if data1 not in dict1:       
    print("沒有%s這個水果" % (data1))
    data1=input("請輸入水果：")
else:
    print(data1+"是"+dict1[data1])