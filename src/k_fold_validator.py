import feature_lib as fl 
import regression as rg 
import numpy as np 
import scipy as sp
import random
import math
from itertools import chain

def partition(l, k):
  n  = int(len(l) / k)
  x =  [l[i:i+n] for i in range(0, len(l), n)]
  if len(x) >= 2 and len(x[-1]) < n: 
    x = x[:-2] + ([x[-2] + x [-1]])
  return x 

def merge(l): 
  return list(chain.from_iterable(l))

def train_regression(training): 
  t = fl.list2ordered_dict(training)
  data,ds = fl.get_data2(t)
  m = rg.iter2matrix(data)
  x = m.T[:-1].T
  x = rg.append_ones(x)
  y =  m.T[-1:].T

  w = rg.regression_weights(x,y)
  terror = rg.mse_error(x,y,w)

  return (w, ds, terror)

def test_regression(w, test, ds): 
  data = fl.format_inputs(test, ds)
  m = rg.iter2matrix(data)
  x = m.T[:-1].T
  x = rg.append_ones(x)
  y =  m.T[-1:].T

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

import unicodecsv as csv
raw_dataf = open("data/features/full_raw_features.csv", "r")
raw_datac = csv.reader(raw_dataf)
next(raw_datac)
raw_datal = [row for row in raw_datac]

k = 25
errors, terrors = k_fold_cvalidation(raw_datal, k, train_regression, test_regression)
errors = [ math.pow(10, float(a)) for a in errors ] 
error = np.average(errors)
terrors = [ math.pow(10, float(a)) for a in terrors ] 
terror = np.average(terrors)

print "The MSE error with " + str(k) + " validation is $" + str(error)  + " and " + "the training error is $" + str(terror) 
