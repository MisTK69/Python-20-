# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

text=input("請輸入一小串小寫英文:")
def a(text):
    new=[]  
    v=["a","e","i","o","u"]
    for i in text:          
        if i not in v:  
            new.append(i)  
        else:
            new.extend(".")
    return "".join(new)
print (a(text))
