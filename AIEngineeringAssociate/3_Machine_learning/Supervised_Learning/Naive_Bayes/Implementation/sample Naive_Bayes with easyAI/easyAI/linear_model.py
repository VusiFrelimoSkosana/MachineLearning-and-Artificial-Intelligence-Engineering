# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:58:25 2022

@author: Professor
"""

#slope
def gradient(x,y):
    x_sum= sum(x)
    y_sum= sum(y)
    
    x_2_count=[]
    for i in x:
       square= i**2
       x_2_count.append(square)
    x_2_sum= sum(x_2_count)
    
    
    xy_count=[]
    k=0
    for i in x:
       xy= x[k]*y[k]
       xy_count.append(xy)
       k=k+1
    xy_sum=sum(xy_count)
       
    grad=(len(x)*xy_sum - x_sum*y_sum)/(len(x)*x_2_sum-(x_sum)**2)
    

    return grad

#prediction
def predict(pred,x,y):
    x_sum= sum(x)
    y_sum= sum(y)
    
    
    x_2_count=[]
    for i in x:
       square= i**2
       x_2_count.append(square)
    x_2_sum= sum(x_2_count)
    
    
    xy_count=[]
    k=0
    for i in x:
       xy= x[k]*y[k]
       xy_count.append(xy)
       k=k+1
    xy_sum=sum(xy_count)
        
    gradient=(len(x)*xy_sum - x_sum*y_sum)/(len(x)*x_2_sum-(x_sum)**2)
    
    b= (y_sum - gradient* x_sum)/len(x)
    
    y= gradient* pred + b
    return y

def intercept(x,y):
    x_sum= sum(x)
    y_sum= sum(y)
    
    x_2_count=[]
    for i in x:
       square= i**2
       x_2_count.append(square)
    x_2_sum= sum(x_2_count)
    
    
    xy_count=[]
    k=0
    for i in x:
       xy= x[k]*y[k]
       xy_count.append(xy)
       k=k+1
    xy_sum= sum(xy_count)
       
    grad= (len(x)*xy_sum - x_sum*y_sum)/(len(x)*x_2_sum-(x_sum)**2)
    
    b= (y_sum - grad* x_sum)/len(x)

    return b

def ss_mean(y):

    mean= sum(y)/len(y)
    data_mean=[]
    for data in y:
        data_mean_count= (data- mean)**2
        data_mean.append(data_mean_count)
    total_ss_mean=sum(data_mean)
    return total_ss_mean

def ss_fit(x,y):
    x_sum= sum(x)
    y_sum= sum(y)
    
    x_2_count=[]
    for i in x:
       square= i**2
       x_2_count.append(square)
    x_2_sum= sum(x_2_count)
    
    
    xy_count=[]
    k=0
    for i in x:
       xy= x[k]*y[k]
       xy_count.append(xy)
       k=k+1
    xy_sum= sum(xy_count)
       
    grad= (len(x)*xy_sum - x_sum*y_sum)/(len(x)*x_2_sum-(x_sum)**2)
    
    b= (y_sum - grad* x_sum)/len(x)
    
    data_fit=[]
    k=0
    for data in y:
        fit= grad*x[k] + b
        fit_count= (data-fit)**2
        data_fit.append(fit_count)
        k=k+1
    total_ss_fit=sum(data_fit)
    return total_ss_fit

def variance_mean(x,y):
    var= ss_mean(y)/len(y)  #calling the outer function (ss_mean(x,y))
    return var

def variance_fit(x,y):
    var= ss_fit(x,y)/len(y)  #calling the outer function (ss_fit(x,y))
    return var

def r2_score(x,y):
    r2= (variance_mean(x,y)- variance_fit(x,y))/ variance_mean(x,y)
    return r2