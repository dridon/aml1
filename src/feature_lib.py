import time
import numpy as np 
import scipy.stats.mstats as ms
import math

def seek(f, csv, line):
    f.seek(0)
    for i in range(line): 
        next(csv)

def csv_dict(csv, f): 
  d = {} 
  for row in csv:
    d[row[0].strip()] = row 

  seek(f, csv, 1)
  return d 

def hot_season(date): 
  month_index = 1 
  m = time.strptime(date, "%Y/%m/%d")[month_index]
  h = 0
  if (m > 4 and m < 9) or (m == 11) or (m == 12): 
    h = 1
  return h 

def keys(s):
  return s.split("|")

def load_key(k, d): 
  if not k in d: 
    d[k] = [[], [], []] 

def add_ratings(d, ks, rtc_rating, rta_rating, imdb_rating): 
  for k in ks: 
    load_key(k, d) 
    d[k][0].append(rtc_rating)
    d[k][1].append(rta_rating)
    d[k][2].append(imdb_rating)

def percent2float(s): 
  return float(s.strip().strip('%'))
    
def people_dicts(raw_data): 
  dd = {} 
  pd = {} 
  sd = {} 
  ad = {}

  for k in raw_data.iterkeys():
    m = raw_data[k]
    dkeys = keys(m[10])
    pkeys = keys(m[11])
    skeys = keys(m[12])
    akeys = keys(m[13])

    rtc_rating = percent2float(m[6])
    rta_rating = percent2float(m[8])
    imdb_rating = percent2float(m[9])

    add_ratings(dd, dkeys, rtc_rating, rta_rating, imdb_rating) 
    add_ratings(pd, pkeys, rtc_rating, rta_rating, imdb_rating) 
    add_ratings(sd, skeys, rtc_rating, rta_rating, imdb_rating) 
    add_ratings(ad, akeys, rtc_rating, rta_rating, imdb_rating) 
  return (dd, pd, sd, ad)

def dict2list(d):
  l = [] 
  for k in d.iterkeys():
    v = (k, ms.gmean(d[k][0]), ms.gmean(d[k][1]), ms.gmean(d[k][2]))
    l.append(v)
  return l

def ratings(d, ks, rating_index):
  avgs = [] 
  for k in ks:
    v =  d[k][rating_index]
    avgs.append(ms.gmean(v))
  return np.average(avgs)

def get_data(raw_data, directord, producerd, swriterd, actord):
  data = [] 
  for k in raw_data.iterkeys():
    m = raw_data[k]
    dkeys = keys(m[10])
    pkeys = keys(m[11])
    skeys = keys(m[12])
    akeys = keys(m[13])

    revenue = float(m[4])
    budget = float(m[3])
    if revenue <= 0 : 
      revenue = 1
    if budget <= 0: 
      budget = 1 

    data.append((
      hot_season(m[1].strip()), 
      math.log(budget, 10),
      ratings(directord, dkeys, 0),
      ratings(directord, dkeys, 1),
      ratings(directord, dkeys, 2),
      ratings(producerd, pkeys, 0),
      ratings(producerd, pkeys, 1),
      ratings(producerd, pkeys, 2),
      ratings(swriterd, skeys, 0),
      ratings(swriterd, skeys, 1),
      ratings(swriterd, skeys, 2),
      ratings(actord, akeys, 0),
      ratings(actord, akeys, 1),
      ratings(actord, akeys, 2),
      math.log(revenue, 10)
      ))
  return data 
