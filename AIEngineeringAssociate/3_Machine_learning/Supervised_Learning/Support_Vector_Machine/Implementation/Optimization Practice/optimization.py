# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:48:53 2022

@author: Professor
"""

from cvxopt import matrix
from cvxopt import solvers

P=matrix([[1.0,0.0],[0.0,0.0]])
q=matrix([3.0,4.0])
G=matrix([[-1.0,0.0,-1.0,2.0,3.0],[0.0,-1.0,-3.0,5.0,4.0]])
h=matrix([0.0,0.0,-15.0,100.0,80.0])
#A=matrix([0,0])
#b=matrix([0])

#Setting solver parameters (change default to decrease tolerance)
solvers.options['show_progress']=False
solvers.options['abstol']=1e-10
solvers.options['reltol']=1e-10
solvers.options['feastol']=1e-10

sol= solvers.qp(P,q,G,h)

print(sol['x'])


