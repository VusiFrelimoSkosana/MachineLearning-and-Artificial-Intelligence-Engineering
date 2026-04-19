# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:22:00 2023

@author: Professor
"""
import numpy as np
import matplotlib.pyplot as plt

x= np.array([1,2,3,4,5,6,7])
y_1=np.array([0,0,0,1,1,1,1])
z=np.array([2,4,6,8,10,12,14])
y_2=np.array([0,0,0,0,1,1,1])
"""
def multi_logistic(x_val,z_val):
    sig= np.exp(-x_val)/(np.exp(-x_val)+np.exp(-z_val))
    return sig
"""


def logistic(z):
    sig= 1/(1+np.exp(-z))
    return sig
X=np.vstack(((np.ones(len(x))),x))


def cost_gradient(x,y,weight):
    m=len(x)
    sig=logistic(weight[0]+weight[1]*x)
    X=np.vstack(((np.ones(len(x))),x))
    for i in y:
     w=((1/m)*np.dot(X,sig))*i
    return w
#initializing multipl weight in a dictionary

weight= np.zeros(2)

dic_keys=[]

j=1
for i in range(0,len(x)):
    key= 'w_'+str(j)
    dic_keys.append(key)
    j+=1
    

weights_dic={}  #multiple weights in a dictionary

for key in dic_keys:
    weights_dic[key]= weight

print(weights_dic)

iteration=9   #iteration
alpha=0.1    #learning rate

#computing the Gradient descent with multiple weights


for weight in weights_dic:
   
    for i in range(1,iteration):
        weights_dic[weight] -= alpha*cost_gradient(x,y_1,weights_dic[weight])
    print(weights_dic[weight])


'''
NB: THIS WAS A SIDE NOTE ABOUT THAT MULTIPLE WEIGHTS WERE USED WITH ONE CLASS INSTEAD
OF MANY CORRESPONDING CLASS WHICH WAS WRONG, HOWEVER THIS WAS JUST A PRACTICE EXAMPLE

'''


