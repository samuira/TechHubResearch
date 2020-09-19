t# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:32:21 2020

@author: ssil
"""
import math
ab = 3
bc = 4
ac = math.sqrt(math.pow(ab,2)+math.pow(bc,2))
ad = ac/2
print(ab,bc,ac,ad)
bac = math.degrees(math.atan(bc/ab))

abd = (ab*ab)/(2*ab*ad)
print(math.degrees(math.acos(abd)))
