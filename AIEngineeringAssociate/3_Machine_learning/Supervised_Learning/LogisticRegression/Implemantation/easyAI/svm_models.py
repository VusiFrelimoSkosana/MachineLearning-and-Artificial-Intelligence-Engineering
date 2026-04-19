# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:58:00 2023

@author: Professor
"""

import numpy as np

from cvxopt import matrix
from cvxopt import solvers




def alphas(x_pos, x_neg, x_array, y_array):
    #Creating a loop that combine both positive and negative samples into one list
    
    x_length=len(x_neg) + len(x_pos)   #total size of samples
    x=[]   #contain both negative and positive samples
    
    p=0
    for i in range(0 ,x_length):
        if i < len(x_neg):
            x.append(x_neg[i])
        elif i>= len(x_neg):
            x.append(x_pos[p])
            p=p+1
    
    x_array= np.array(x)   #convert an ordinary list into an array
    
    y_neg= np.ones(len(x_neg))*(-1)   #contain the  negative y samples
    y_pos= np.ones(len(x_pos))*(+1)   #contain the  positive y samples
    
    y_array= np.hstack((y_neg,y_pos)) #contain both negative and positive y samples
    
    
    #Now we construct a Q matrix
    
    x_prime= []
    
    j=0
    for x_vector in x_array:
        mult= x_vector*y_array[j]
        x_prime.append(mult)
        j=j+1
    
    x_prime_array = np.array(x_prime) #convert x_prime into an array
    x_prime_array_transpose= x_prime_array.transpose()
    Q= np.dot( x_prime_array, x_prime_array_transpose) #This is Q matrix
    
    # finding a p matrix
    
    p= np.ones(len(x_array))*(-1)
    
    #finding a G matrix
    N=len(x_array)
    G= np.zeros((N,N))  #G matrix
    
    for i in range(0,N):
        G[i,i]=-1
    
    #finding an h matrix
    h= np.zeros(len(x_array))
    
    #finding A matrix
    A = y_array*(-1)
    
    #finding b matrix
    
    b=np.array([0.])
    
    #Finding a solution, use cvxcov library to find values of alphas
    
    sol =solvers.qp(matrix(Q , tc='d'), matrix(p , tc='d'), matrix(G , tc='d'), matrix(h, tc='d'), matrix(A, (1,len(x_array)), 'd'), matrix(b , tc='d'))
    alphas=np.array(sol['x'])
    
    return alphas
    

    #finding the support vectors (points that lie on the plane or gutter)
def support_vectors(x_array, alphas):
    support_vectors=[]  #All support vectors
    p=0
    for j in x_array:
        rounded= round(alphas[p][0], 2)
        p+=1
        if rounded != 0:
            support_vectors.append(j)
            
    return support_vectors



def pos_neg_sv(support_vectors, x_pos):
    #separate support vectors into individual classes
    #i.e (separate lists for positive and negative samples)
    
    
    pos_neg={'positive_support_vectors': [] , 'negative_support_vectors': [] } #dictionery contains positive and negative support vectors
    
    
    for sv in support_vectors:
        for pos in np.  array(x_pos):
            if sv[0] == pos[0] and sv[1] == pos[1]:
                pos_neg['positive_support_vectors'].append(sv)
            else:
                pos_neg['negative_support_vectors'].append(sv)
                
    return pos_neg

def w(alphas,y_array, x_array):

    w_sum=np.zeros(2)
    
    for i in range(0,len(x_array)):
        w_sum= w_sum + alphas[i]*y_array[i]*x_array[i]
    return w_sum

def b(x_array, y_array, w):
    const_b= -1- np.dot(x_array[0], w)
    return const_b

def margin_gradient(w_vector):
    #Computing the gradient of the margins 
    #(left and right margins are parallel so they have the same gradient or slope)
    #Recall margins/separating planes are perpendicular to vector W
    
    gradient=[]
    
    if round(w_vector[0],2)== 0:
        slope= w_vector[0]/w_vector[1]
        gradient.append(slope)
    else:
        slope2= -1/((w_vector[1]/w_vector[0]))  #perpendicular vectors m1 * m2 =-1
        gradient.append(slope2)
    
    return gradient