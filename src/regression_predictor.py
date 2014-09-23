import unicodecsv as csv 
import numpy as np 
import scipy as sp 
import math 
import regression as rg

dataf = open('data/features/feature_data.csv', 'rt')
datac = csv.reader(dataf)
next(datac)
m = rg.iter2matrix(datac) 
x1 = m.T[:-1].T
x = rg.append_ones(x1)
y =  m.T[-1:].T
w = rg.regression_weights(x,y)
lse = rg.lse_error(x, y, w) 
mse = rg.mse_error(x, y, w)

print "weights: " + str(w)
print "lse: " + str(lse)
print "mse: " + str(mse)
