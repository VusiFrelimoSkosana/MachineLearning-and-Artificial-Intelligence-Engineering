# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:45:19 2023

@author: Professor
"""
import numpy as np


#Define the logistic function
def logistic(z):
    sig= 1/(1+np.exp(-z))
    return sig

#Gradient of a cost function
def cost_gradient(weight,x,y):
    m=len(x)
    sigmoid=logistic(weight[0] +  weight[1]*x)
    
    X=np.vstack((np.ones(len(x)),x))   #for  values
    grad=(1/m) *np.dot(X,(sigmoid-y))
    return grad