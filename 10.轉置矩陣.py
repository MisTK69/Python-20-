# -*- coding: utf-8 -*-
"""
@author: 陳柏劭
"""

import numpy as np
n,m=input("輸入N及M為:").split(" ")
array1=[]
for i in range(int(n)):
   array1.append([int(m) for m in input("輸入矩陣數值第"+str(i+1) +"列為:").split()])
a=np.transpose(array1).tolist()

for j in range(int(m)):
  print("輸出矩陣數值第"+str(j+1)+"列為",end="")
  for k in range(int(n)):
    print(str(a[j][k])+" ",end="")
  print()
