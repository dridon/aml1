import numpy as np 
import scipy as sp 
import math 

def iter2matrix(it):
  a = [] 
  for row in it: 
    l = [] 
    for c in row: 
      l.append(float(c))
    a.append(l)
  return np.matrix(a)

def append_ones(m):
  p,q = m.shape
  a = np.zeros((p, q+1))
  a[:,:-1] = m 
  a[:,-1:] = np.ones((p, 1))
  return np.matrix(a)

def regression_weights(x, y):
  return (x.T*x).I*x.T*y

def predict(x, w):
  return x*w

def lse_error(x, y, w): 
  e1 = y - predict(x, w) 
  return e1.T*e1

def mse_error(x, y, w):
  return lse_error(x, y, w)/y.size

