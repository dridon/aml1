import unicodecsv as csv 
import time
import numpy as np 
import scipy.stats.mstats as ms

data = [("Hot Season", "Budget", "Director RT Critical Average", "Director RT Public Average", "Director IMDB Average", "Producer RT Critical Average", "Producer RT Public Average", "Producer IMDB Average", "Screenwriter RT Critical Average", "Screenwriter RT Public Average", "Screenwriter IMDB Average","Actors RT Critical Average", "Actors RT Public Average", "Actors IMDB Average", "Gross")]

actorsf = open("actors.csv", "r")
directorsf = open("directors.csv", "r")
producersf = open("producers.csv", "r")
swriterf = open("screenwriter.csv", "r")
raw_dataf = open("full_raw_features.csv", "r")

actorsc = csv.reader(actorsf)
directorsc = csv.reader(directorsf)
producersc = csv.reader(producersf)
swriterc = csv.reader(swriterf)
raw_datac = csv.reader(raw_dataf)

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

def load_key(k, d, i, l): 
  if not k in d: 
    d[k] = [i]*l 

def add_ratings(d, ks, rtc_rating, rta_rating, imdb_rating): 
  for k in ks: 
    load_key(k, d, [], 3) 
    d[k][0].append(rtc_rating)
    d[k][1].append(rta_rating)
    d[k][2].append(imdb_rating)

    print "imdb :" + d[k][0]

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

# def person_exists(p, s):
#   return p in s.split("|")

# def person_ratings(p, d, raw_data, ri):
#   load_key(p, d, [], 3)

#   for k in raw_data.iterkeys():
#     if person_exists(p, raw_data[k][ri]):
#       d[p][0].append(raw_data[k][6])
#       d[p][1].append(raw_data[k][8])
#       d[p][2].append(raw_data[k][9])

# def all_person_ratings(s, raw_data, i):
#   d = {} 
#   for p in s: 
#     p = p[0]
#     person_ratings(p, d, raw_data, i)
#   return d

next(raw_datac)
raw_data = csv_dict(raw_datac, raw_dataf)
directord, producerd, swriterd, actord = people_dicts(raw_data)

def ratings(d, ks, rating_index):
  avgs = [] 
  for k in ks:
    v =  d[k][rating_index]
    avgs.append(np.average(v))
  return np.average(avgs)

def get_data(raw_data, directord, producerd, swriterd, actord):
  data = [] 
  for k in raw_data.iterkeys():
    m = raw_data[k]
    dkeys = keys(m[10])
    pkeys = keys(m[11])
    skeys = keys(m[12])
    akeys = keys(m[13])

    data.append((
      hot_season(m[1].strip()), 
      m[3],
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
      m[4]
      ))
  return data 

data = get_data(raw_data, directord, producerd, swriterd, actord) 
# data_writer = csv.writer(open("feature_data.csv", "w+"))
# data_writer.writerows(data)
