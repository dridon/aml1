import numpy as np 
import scipy as sp 
import math 

def grad_descent(x,y,init_weight,alpha,iterations):
  for i in range(1,iterations):
    loss = y-(x*init_weight)
    cost = (-2.0 / y.shape[0]) *x.T * loss
    init_weight = init_weight - (alpha * cost)
  return init_weight
