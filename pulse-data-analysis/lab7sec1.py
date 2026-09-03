# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:09:19 2025

@author: eia23npf
"""
nums = 'pulse_data.txt'
def pulse_data(nums):
    data=[]
    f = open(nums,'r')
    for line in f.readlines():
        words = float(line.split()[0])
        print (words)
        data.append(words)
    return data
        
from pylab import *
data = pulse_data(nums)
data.sort()
Xs = []
for i in range(len(data)):
    Xs.append(i)

#plot(Xs,data,'rx-')
hist(data, 50)
show()
xlabel('ascending integers')
ylabel('list of data values')
title('initial data exploration')