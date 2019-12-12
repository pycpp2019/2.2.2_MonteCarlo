# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:52:52 2019

@author: asus
"""

import numpy as np

def pi_error(N):
    data = np.random.rand(N,2)
    shift = np.array([[0.5, 0.5]]*N)
    data = data - shift
    data_of_len = np.array([(i[0]*i[0]+i[1]*i[1])**0.5 for i in data])
    data_of_len.sort()
    i = 0
    while data_of_len[i] < 0.5:
        i += 1
    return (np.abs(i/N*4 - np.pi)) 

import matplotlib.pyplot as plt

xs = [2**k for k in range(10, 25)]
ys = [pi_error(x) for x in xs]
plt.plot(xs, ys)
plt.xscale("log")
plt.show()