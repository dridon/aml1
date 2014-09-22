import numpy as np 
import scipy as sp 
import unicodecsv as csv 
import math 

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

def regression_weights(x, y):
  return (x.T*x).I*x.T*y

def predict(x, w):
  return w*x

def lse_error(x, y, w): 
  e1 = y - x*w 
  return e1.T*e

def mse_error(x, y, w):
  return lse_error(x, y, w)/y.size

dataf = open('data/features/feature_data.csv', 'rt')
datac = csv.reader(dataf)
next(datac)
m = csv2matrix(datac) 
x = m.T[:-1].T
y =  m.T[-1:].T
w = regression_weights(x,y)