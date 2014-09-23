import numpy as np 
import scipy as sp 
import unicodecsv as csv 
import math 
import sys
from sklearn import linear_model

def csv2matrix(csv):
  a = [] 
  for row in csv: 
    l = [] 
    for c in row: 
      l.append(float(c))
    a.append(l)
  return np.matrix(a)

def data2matrx(data): 
  a = [] 
  for d in data: 
    a.append(list(d))
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
  return w*x

def lse_error(x, y, w): 
  e1 = y - x*w 
  return e1.T*e1

def mse_error(x, y, w):
  return lse_error(x, y, w)/y.size

dataf = open('data/features/feature_data.csv', 'rt')
datac = csv.reader(dataf)
next(datac)
m = csv2matrix(datac) 
x = m.T[:-1].T
x = append_ones(x)
y =  m.T[-1:].T
w = regression_weights(x,y)
lse = lse_error(x, y, w) 
mse = mse_error(x, y, w)


#Ridge Regression Manual
'''xNC = m.T[:-1].T #i.e. x without the constant field
lmb = 1
wRidge = ( (xNC.T)*(xNC) + (lmb * np.identity(xNC.shape[1])) )*xNC.T*y 
#print wRidge
#print ""
#print w
'''

#Ridge Regression (SciKit) - utilizes cross-validation to choose a lambda value
xNC = m.T[:-1].T #i.e. x without the constant field
clf = linear_model.Ridge (alpha = .5)
clf.fit (xNC, y) 
wRidge = w

for i in xrange(0,15):
    if i == 14:
        wRidge[i] = clf.intercept_
    else:
        wRidge[i] = clf.coef_[(0,i)]
#print wRidge

ridgeLSE = lse_error(x, y, wRidge) 
ridgeMSE = mse_error(x, y, wRidge) 

print "Normal Reg:"
print lse
print mse
print "Ridge Reg:"
print ridgeLSE
print ridgeMSE
