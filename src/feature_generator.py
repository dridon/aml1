import unicodecsv as csv 
import time
import numpy as np 

data = [("Hot Season", "Budget", "Director RT Average", "Director RT Public Average", "Director IMDB Average", "Producer RT Critical Average", "Producer RT Public Average", "Producer IMDB Average", "Screenwriter RT Critical Average", "Screenwriter RT Public Average", "Screenwriter IMDB Average","Actors RT Critical Average", "Actors RT Public Average", "Actors IMDB Average", "Gross")]

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

def person_exists(p, s):
  return p in s.split("|")

def load_key(k, d, i, l): 
  if not k in d: 
    d[k] = [i]*l 

def person_ratings(p, d, raw_data, ri):
  load_key(p, d, [], 3)

  for k in raw_data.iterkeys():
    if person_exists(p, raw_data[k][ri]):
      d[p][0].append(raw_data[k][6])
      d[p][1].append(raw_data[k][8])
      d[p][2].append(raw_data[k][9])

def all_person_ratings(s, raw_data, i):
  d = {} 
  for p in s: 
    p = p[0]
    person_ratings(p, d, raw_data, i)
  return d

next(raw_datac)
raw_data = csv_dict(raw_datac, raw_dataf)

directord = all_person_ratings(directorsc, raw_data, 10) 
producerd = all_person_ratings(producersc, raw_data, 11) 
swriterd = all_person_ratings(swriterc, raw_data, 12) 
actord = all_person_ratings(actorsc, raw_data, 13)

def critic_ratings(d, k):


def imdb_ratings(d, k): 

def rt_ratings(d, k): 

for m in raw_data.iterkeys():
  data.append((
    hot_season(m[1]), 
    m[3],
    critic_ratings(
    ))

# data_writer = csv.writer(open("feature_data.csv", "w+"))
# data_writer.writerows(data)
