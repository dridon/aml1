import numpy as np 
import scipy as sp 
import math 
import regression as rg 
import unicodecsv as csv


def grad_descent(x,y,init_weight,alpha,iterations):
    for i in range(1,iterations):
        loss = y-(x*init_weight)
        cost = (-2.0 / y.shape[0]) *x.T * loss
        init_weight = init_weight - (alpha * cost)
    return init_weight

    
dataf = open('data/features/feature_data.csv', 'rt')
datac = csv.reader(dataf)
next(datac)
m = rg.iter2matrix(datac) 
x = m.T[:-1].T
x = rg.append_ones(x)
y =  m.T[-1:].T
init_weight = np.ones((x.shape[1],1))
final_weight = grad_descent(x,y,init_weight,0.00004,1000)
print final_weight
print rg.mse_error(x,y,final_weight)
