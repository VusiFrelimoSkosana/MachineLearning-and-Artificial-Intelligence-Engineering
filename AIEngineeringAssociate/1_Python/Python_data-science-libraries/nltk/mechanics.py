# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:01:05 2022

@author: Professor
"""
#constants
g=9.8

"""fundamental equations"""

# hooks force
def displacement(initial_position, final_position):
    d_change= final_position - initial_position
    return d_change

def velocity(displacement, time):
    v= displacement/time
    return v

def velocity_change(initial_velocity, final_velocity):
    v_change =  final_velocity - initial_velocity
    return v_change
    
def accelaration(initial_velocity, final_velocity, time):
        a = (final_velocity - initial_velocity)/time
        return a

def hooks_force(k,displacement):
    f_s= k*displacement
    return f_s

#gravitational force
def gravitational_force(mass,g):
    f_g = mass*g
    return f_g

#calculating momentum
def momentum(mass, velocity_change):
    p = mass*velocity_change
    return p

"""non-fundamental equations"""
#calculating fore
def force(momentum,time):
    f = momentum/time
    return f


print(force(momentum(3,7),9))

"""
input_values =['what is the mass?', "what is the velocity"]
for value in input_values:
inp = int(input(value))
"""