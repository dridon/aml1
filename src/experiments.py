import unicodecsv as csv
import k_fold_validator as kfv 

raw_dataf = open("data/features/full_raw_features.csv", "r")
raw_datac = csv.reader(raw_dataf)
next(raw_datac)
raw_datal = [row for row in raw_datac]

trainers = {
    "standard": kfv.train_regression, 
    "gradient descent": kfv.train_grad_descent, 
    "ridge": kfv.train_ridge, 
    "lasso": kfv.train_lasso
    }

def k_validation(data, rs, k, params): 
  errors = {}
  for key in rs.iterkeys():
    l = {}
    es, ts = kfv.k_fold_cvalidation(data, k, rs[key], kfv.test_regression, params)
    l["errors"] = es
    l["terrors"] = ts
    errors[key] = l 
  return errors

def vary_k(data, rs, min_k, max_k, inc, params):
  errors = {} 
  for key in rs.iterkeys():
    l = {} 
    for k in range(min_k, max_k, inc):
      es, ts = kfv.k_fold_cvalidation(data, k, rs[key], kfv.test_regression, params)
      l.append([k,kfv.mean_error(es), kfv.mean_errors(ts)])
    errors[key] = l
  return errors

def vary_alpha(data, grad_descent, k, alphas, iterations):
  errors = [] 
  for a in alphas:
    params = {"alpha": a, "iterations": iterations}
    es, ts = kfv.k_fold_cvalidation(data, k, kfv.train_grad_descent, kfv.test_regression, params)
    errors.append([a, kfv.mean_error(es), kfv.mean_error(ts)])
  return errors

def vary_iterations(data, grad_descent, k, alpha, iterations):
  errors = [] 
  for i in iterations:
    params = {"alpha": alpha, "iterations": i}
    es, ts = kfv.k_fold_cvalidation(data, k, kfv.train_grad_descent, kfv.test_regression, params)
    errors.append([a, kfv.mean_error(es), kfv.mean_error(ts)])
  return errors

k = 10 
gdp = {"alpha": 0.00004, "iterations":100000}

# errors, terrors = k_fold_cvalidation(raw_datal, k, train_regression, test_regression)
# error = mean_error(errors) 
# terror = mean_error(terrors)
# print "The MSE with standard regression with " + str(k) + "-fold validation is " + str(error)  + " and " + "the training error is " + str(terror) 

# errors, terrors = kfv.k_fold_cvalidation(raw_datal, k, kfv.train_grad_descent, kfv.test_regression, gdp)
# error = kfv.mean_error(errors) 
# terror = kfv.mean_error(terrors)
# print "The MSE with gradient descent with " + str(k) + "-fold validation is " + str(error)  + " and " + "the training error is " + str(terror) 

# errors, terrors = k_fold_cvalidation(raw_datal, k, train_ridge, test_regression)
# error = mean_error(errors) 
# terror = mean_error(terrors)
# print "The MSE with ridge regression with " + str(k) + "-fold validation is " + str(error)  + " and " + "the training error is " + str(terror) 

# errors, terrors = k_fold_cvalidation(raw_datal, k, train_lasso, test_regression)
# error = mean_error(errors) 
# terror = mean_error(terrors)
# print "The MSE with lasso regression with " + str(k) + "-fold validation is " + str(error)  + " and " + "the training error is " + str(terror) 
