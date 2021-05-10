# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

char=input("檢測的字串(end結束)：")
check=input("檢測的單一字元：")
while (char != "end"):
    print("字元%s出現的次數為：%d" %(check,char.count(check)))
    char=input("檢測的字串(end結束)：")
    if char == "end":
        break
    data2=input("檢測的單一字元：")    
print("檢測結束")