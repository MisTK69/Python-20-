# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

a=input("")
a1=a.replace("A","1")
a2=a1.replace("J","11")
a3=a2.replace("Q","12")
a4=a3.replace("K","13")
a5=a4.split(" ")
a6=int(a5[0])+int(a5[1])+int(a5[2])+int(a5[3])+int(a5[4])
print(str(a6))
