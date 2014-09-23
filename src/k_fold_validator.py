import feature_lib as fl 
import regression as rg 
import numpy as np 
import scipy as sp
import random
import math
from itertools import chain
import ridge_lasso as rl

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

def train_regression(training): 
  # get data
  # t = fl.list2ordered_dict(training)
  # data,ds = fl.get_data2(t)
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

def train_ridge(training): 
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
  terror = rg.mse_error(x,y,w)

  return (w, ds, terror)


def train_lasso(training): 
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

def k_fold_cvalidation(l, k, trainer, tester):
  rdf = k_random_folds(l, k)
  errors = []
  terrors = [] 

  for i in range(k):
    training = merge(rdf[0:i] + rdf[i+1:])
    test = rdf[i]

    predictor, formatters, terror  = trainer(training)
    terrors.append(terror)
    errors.append(tester(predictor, test, formatters))

  return (errors, terror)

def mean_error(errors): 
  return np.average([float(a) for a in errors])

import unicodecsv as csv
raw_dataf = open("data/features/full_raw_features.csv", "r")
raw_datac = csv.reader(raw_dataf)
next(raw_datac)
raw_datal = [row for row in raw_datac]

k = 25

errors, terrors = k_fold_cvalidation(raw_datal, k, train_regression, test_regression)
error = mean_error(errors) 
terror = mean_error(terrors)
print "The MSE with standard regression is " + str(k) + " validation is " + str(error)  + " and " + "the training error is " + str(terror) 
# errors = [float(a) for a in errors ] 
# error = np.average(errors)
# terrors = [float(a) for a in terrors ] 
# terror = np.average(terrors)

errors, terrors = k_fold_cvalidation(raw_datal, k, train_ridge, test_regression)
error = mean_error(errors) 
terror = mean_error(terrors)
print "The MSE with ridge regression is " + str(k) + " validation is " + str(error)  + " and " + "the training error is " + str(terror) 

errors, terrors = k_fold_cvalidation(raw_datal, k, train_lasso, test_regression)
error = mean_error(errors) 
terror = mean_error(terrors)
print "The MSE with lasso regression is " + str(k) + " validation is " + str(error)  + " and " + "the training error is " + str(terror) 
