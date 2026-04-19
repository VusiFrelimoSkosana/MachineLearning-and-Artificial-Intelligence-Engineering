from cvxopt import matrix
from cvxopt import solvers# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:04:00 2022

@author: Professor
"""

import numpy



Q= matrix(numpy.array([[5,3,5],[3,5,3],[5,3,5]]), tc='d')
P= matrix(numpy.array([-1,-1,-1]), tc='d')
G= matrix(numpy.array([[-1,0,0],[0,-1,0],[0,0,-1]]), tc='d')
h= matrix(numpy.array([0,0,0]), tc='d')
A= matrix([1,1,-1], (1,3), 'd')
b= matrix(numpy.array([0]), tc='d')


print(A)
#Setting solver parameters (change default to decrease tolerance)


#solvers.options['show_progress']=False
#solvers.options['abstol']=1e-10
#solvers.options['reltol']=1e-10
#solvers.options['feastol']=1e-10

sol =solvers.qp(Q,P,G,h, A,  b)
alphas=numpy.array(sol['x'])

print(sol['x'])


for i in alphas:
    val=i[0]
    answer= float(val)
    
    print(answer)