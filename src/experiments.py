import unicodecsv as csv
import math
import k_fold_validator as kfv 

def k_validation(data, rs, k, params): 
  errors = {}
  for key in rs.iterkeys():
    l = {}
    es, ts = kfv.k_fold_cvalidation(data, k, rs[key], kfv.test_regression, params)
    l["errors"] = [float(a) for a in es]
    l["terrors"] = [float(a) for a in ts]
    errors[key] = l
  return errors

def vary_k(data, rs, min_k, max_k, inc, params):
  errors = {} 
  for key in rs.iterkeys():
    print "On regression: " + str(key)
    l = []
    for k in range(min_k, max_k + 1, inc):
      print "On k value of " + str(k)
      es, ts = kfv.k_fold_cvalidation(data, k, rs[key], kfv.test_regression, params)
      l.append([k,kfv.mean_error(es), kfv.mean_error(ts)])
    errors[key] = l  
  return errors

def vary_alpha(data, k, alphas, iterations):
  errors = [] 
  params = {"iterations": iterations}
  for a in alphas:
    print "On alpha " + str(a)
    params["alpha"] = a
    es, ts = kfv.k_fold_cvalidation(data, k, kfv.train_grad_descent, kfv.test_regression, params)
    errors.append([a, kfv.mean_error(es), kfv.mean_error(ts)])
  return errors

def vary_iterations(data, k, alpha, iterations):
  errors = [] 
  params = {"alpha": alpha}
  for i in iterations:
    print "On iteration count " + str(i)
    params["iterations"] = i
    es, ts = kfv.k_fold_cvalidation(data, k, kfv.train_grad_descent, kfv.test_regression, params)
    errors.append([i, kfv.mean_error(es), kfv.mean_error(ts)])
  return errors

def print_valdiate_k(k, errors):
  e  = [["Reggression", "True Error", "Training Error"]]
  for key in errors.iterkeys(): 
    e.append([key, kfv.mean_error(errors[key]["errors"]), kfv.mean_error(errors[key]["terrors"])])
  w= csv.writer(open("data/error/" +str(k) + "_fold_validation.csv", "w+"))
  w.writerows(e) 
  return e

def print_vary_k(errors):
  e = [] 
  d = {}
  for k in errors.iterkeys(): 
    e = [["Fold Size", "True Error", "Training Error"]]
    e = e + [l for l in errors[k]]
    d[k] = e
    w = csv.writer(open("data/error/" + k + "_k_variation.csv", "w+"))
    w.writerows(e)
  return d 

def print_vary_alpha(errors):
  w = csv.writer(open("data/error/gd_alpha_variation.csv", "w+"))
  w.writerows(errors)
  
def print_vary_iter(errors):
  w = csv.writer(open("data/error/gd_iter_variation.csv", "w+"))
  w.writerows(errors)

k = 10 
gdp = {"alpha": 0.00001, "iterations":100000}
raw_dataf = open("data/features/full_raw_features.csv", "r")
raw_datac = csv.reader(raw_dataf)
next(raw_datac)
raw_datal = [row for row in raw_datac]

trainers = {
    "standard": kfv.train_regression, 
    # "gradient descent": kfv.train_grad_descent, 
    "ridge": kfv.train_ridge, 
    "lasso": kfv.train_lasso
    }
# alphas = [1/math.pow(10, i) for i in range(5,9)]
# vary_alpha_e = vary_alpha(raw_datal, 10, alphas, 100000)
# print_vary_alpha(vary_alpha_e)

# iterations = [int(math.pow(10, i)) for i in range(1,6)]
# vary_iter_e = vary_iterations(raw_datal, 10, 0.00001, iterations)
# print_vary_iter(vary_iter_e)

# k_val_e = k_validation(raw_datal, trainers, 10, gdp)
# p_e1 = print_valdiate_k(10, k_val_e)

vary_k_e = vary_k(raw_datal, trainers, 10, 33, 1, gdp)
p_e2 =  print_vary_k(vary_k_e)

# iterw = csv.writer(open("gd_iteration_variation.csv", "w+"))
