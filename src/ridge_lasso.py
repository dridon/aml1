import numpy as np 
import scipy as sp 
import unicodecsv as csv 
import math 
from sklearn import linear_model
import regression as rg


#Returns weight vector for ridge regression
#pass X that doesn't have 1s appended
def ridge_reg(x, y):
  ridge = linear_model.Ridge()
  ridge.fit(x, y)
  w = np.zeros(x.shape[1] + 1)
  w[0:-1] = ridge.coef_[0] 
  w[-1] = ridge.intercept_
  return np.matrix(w).T

#Returns weight vector for lasso regularization
#pass X that doesn't have 1s appended
def lasso_reg(x, y):	
  lasso = linear_model.Lasso()
  lasso.fit(x, y) 
  w = np.zeros(x.shape[1] + 1)
  w[0:-1] = lasso.coef_ 
  w[-1] = lasso.intercept_
  return np.matrix(w).T
