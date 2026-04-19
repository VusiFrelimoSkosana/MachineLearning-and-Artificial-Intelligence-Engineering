# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 07:43:45 2022

@author: Professor
"""

import numpy as np
from numpy import linalg as LA
from cvxopt import matrix


#solving matrix equation with numpy


#example_1
matrix1= np.array([[1,2], [3,5]])
vector= np.array([1,2])

answer= np.linalg.solve(matrix1, vector)
print(answer)

#example_2
matrix2= np.array([[6,4,9], [4,6,9],[9,9,17]])
vector2= np.array([-1,-1,1])

answer= np.linalg.solve(matrix2, vector2)
print(answer)

#example_3
matrix3= np.array([[6,4,9,4], [4,6,9,2],[9,9,17,5],[4,2,5,3]])
vector3= np.array([-1,-1,1,-1])

answer= np.linalg.solve(matrix3, vector3)
print(answer)


#example_4
#solving eigen value and eigen vectors

A=np.array([[0,1,1,1],[1,-2.5,-3,-5],[1,-3,-2.5,-3],[1,-5,-3,-2.5]])

#A=np.array([[5,2],[2,5]])
w,v =LA.eig(A)

print(v)