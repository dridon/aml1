import numpy as np 
import scipy as sp 
import unicodecsv as csv 
import math 
from sklearn import linear_model
import regression as rg


#Returns weight vector for ridge regression
#pass X that doesn't have 1s appended
def ridgeReg(x, y):
        ridgeReg = linear_model.Ridge ()
	ridgeReg.fit (x, y) 
	wRidge = w

	for i in xrange(0,15):
	    if i == 14:
		wRidge[i] = ridgeReg.intercept_
	    else:
		wRidge[i] = ridgeReg.coef_[(0,i)]
        return wRidge

#Returns weight vector for lasso regularization
#pass X that doesn't have 1s appended
def lassoReg(x, y):	lassoReg = linear_model.Lasso ()
	lassoReg.fit (xNC, y) 
	wLasso = w

	for i in xrange(0,15):
	    if i == 14:
		wLasso[i] = lassoReg.intercept_
	    else:
		wLasso[i] = lassoReg.coef_[i]
        return wLasso
