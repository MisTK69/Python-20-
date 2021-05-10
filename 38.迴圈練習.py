# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

n=int(input(""))
for i in range(-int(n/2),int(n/2)+1):
  print(" "*abs(i),"*"*abs(n-abs(i)*2)) 