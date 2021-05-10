# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

sA=input("sA：")
sB=input("sB：")
sa=set(sA)
sb=set(sB)
if sa&sb==sa:
    print("YES")
else:
    print("NO")