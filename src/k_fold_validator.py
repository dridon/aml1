import feature_lib as fl 
import regression as rg 
import numpy as np 
import scipy as sp
import random
import math
from itertools import chain
import ridge_lasso as rl
import grad_descent as gd

def partition(l, k):
  n  = int(len(l) / k)
  x =  [l[i:i+n] for i in range(0, len(l), n)]
  if len(x) >= 2 and len(x[-1]) < n: 
    x = x[:-2] + ([x[-2] + x [-1]])
  return x 

def merge(l): 
  return list(chain.from_iterable(l))

def transform_train_set(training):
  t = fl.list2ordered_dict(training)
  return fl.get_data2(t)

def train_regression(training, params={}): 
  # get data
  data,ds = transform_train_set(training)

  # generate regression
  m = rg.iter2matrix(data)
  x = m.T[:-1].T
  x = rg.append_ones(x)
  y =  m.T[-1:].T

  w = rg.regression_weights(x,y)

  # get training error
  terror = rg.mse_error(x,y,w)

  return (w, ds, terror)

def train_grad_descent(training, params): 
  data,ds = transform_train_set(training)

  # generate regression
  m = rg.iter2matrix(data)
  x = m.T[:-1].T
  x = rg.append_ones(x)
  y =  m.T[-1:].T

  init_weight = np.ones((x.shape[1],1))
  w = gd.grad_descent(x,y,init_weight,params["alpha"],params["iterations"])
  # get training error
  terror = rg.mse_error(x,y,w)

  return (w, ds, terror)

def train_ridge(training, params={}): 
  # get data
  # t = fl.list2ordered_dict(training)
  # data,ds = fl.get_data2(t)
  data,ds = transform_train_set(training)

  # generate regression
  m = rg.iter2matrix(data)
  x = m.T[:-1].T
  y =  m.T[-1:].T
  w = rl.ridge_reg(x,y)

  # get training error
  x = rg.append_ones(x)
  terror = rg.mse_error(x,y,w)

  return (w, ds, terror)

def train_lasso(training, params={}): 
  # get data
  # t = fl.list2ordered_dict(training)
  # data,ds = fl.get_data2(t)
  data,ds = transform_train_set(training)

  # generate regression
  m = rg.iter2matrix(data)
  x = m.T[:-1].T
  y =  m.T[-1:].T
  w = rl.lasso_reg(x,y)

  # get training error
  x = rg.append_ones(x)
  terror = rg.mse_error(x,y,w)

  return (w, ds, terror)

def test_regression(w, test, ds): 
  # get data
  data = fl.format_inputs(test, ds)

  # predict results
  m = rg.iter2matrix(data)
  x = m.T[:-1].T
  x = rg.append_ones(x)
  y =  m.T[-1:].T

  # test error
  return rg.mse_error(x, y, w)

def k_random_folds(l, k):
  p = l[:] 
  random.shuffle(p)
  return partition(p, k)

def k_fold_cvalidation(l, k, trainer, tester, params={}):
  rdf = k_random_folds(l, k)
  errors = []
  terrors = [] 

  for i in range(k):
    training = merge(rdf[0:i] + rdf[i+1:])
    test = rdf[i]

    predictor, formatters, terror  = trainer(training, params)
    terrors.append(terror)
    errors.append(tester(predictor, test, formatters))

  return (errors, terror)

def mean_error(errors): 
  return np.average([float(a) for a in errors])

