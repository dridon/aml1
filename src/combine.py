import unicodecsv as csv 

def seek(f, csv, line):
    f.seek(0)
    for i in range(line): 
        next(csv)

moviesf =  open("filtered_data.csv", "r")
actorsf =  open("imdb_movie_actor.csv", "r")
tcrewf  =  open("imdb_movie_crew.csv", "r")
tomatorf = open("movie_ratings.csv", "r")
imdbrf = open("imdb_movie_rating.csv", "r")

moviesc = csv.reader(moviesf)
actorsc = csv.reader(actorsf)
tcrewc = csv.reader(tcrewf)
tomatorc = csv.reader(tomatorf)
imdbrc = csv.reader(imdbrf)

next(moviesc)
next(actorsc)
next(tcrewc) 
next(tomatorc)
next(imdbrc)

actors = [[a] for a in { a[1].strip() for a in actorsc}]
seek(actorsf, actorsc, 1)
directors = [[d] for d in { t[2].strip() for t in tcrewc if t[1] == "Director" }]
seek(tcrewf, tcrewc, 1)
producers = [[p] for p in { t[2].strip() for t in tcrewc if t[1] == "Producer" }]
seek(tcrewf, tcrewc, 1)
swriter = [[s] for s in { t[2].strip() for t in tcrewc if t[1] == "Screenwriter"}]
seek(tcrewf, tcrewc, 1)
movies = [[m] for m in { m[0].strip() for m in moviesc }]
seek(moviesf, moviesc, 1)

def csv_dict(csv, f): 
  d = {} 
  for row in csv:
    d[row[0].strip()] = row 

  f.seek(0)
  next(csv)
  return d 

def load_dic_list(d, k, v): 
  k = k.strip()
  if not k in d: 
    d[k] = [] 
  d[k].append(v) 

movied = csv_dict(moviesc, moviesf) 
tomatord = csv_dict(tomatorc, tomatorf)  
imdbrd = csv_dict(imdbrc, imdbrf) 

actorsd = {} 
directord = {}
producerd = {}
swriterd = {}

for a in actorsc: 
  load_dic_list(actorsd, a[0], a[1])

for t in tcrewc:
  if t[1] == "Director": 
    load_dic_list(directord, t[0], t[2])
  elif t[1] == "Producer": 
    load_dic_list(producerd, t[0], t[2])
  elif t[1] == "Screenwriter": 
    load_dic_list(swriterd, t[0], t[2])

ds = [movied, tomatord, imdbrd, actorsd, directord, producerd, swriterd]

def key_in_all(k, ds):
  in_all = True

  for d in ds:
    if not k in d: 
      in_all = False 

  return in_all

raw_data = [("Movie Name", "Release Date", "Genre", "Budget", "Gross", "RT Critic Label", "RT Critic Rating", "RT Audience Label", "RT Audience Rating", "IMDB Rating", "Directors", "Producers", "Sreenwriters", "Actors")]

i = 0 
for k in movied.iterkeys(): 
  if key_in_all(k, ds):
    i = i + 1
    raw_data.append((
      movied[k][0], 
      movied[k][1], 
      movied[k][2], 
      movied[k][3], 
      movied[k][4], 
      tomatord[k][1], 
      tomatord[k][2], 
      tomatord[k][3], 
      tomatord[k][4],
      imdbrd[k][1],
      "|".join(directord[k]),
      "|".join(producerd[k]),
      "|".join(swriterd[k]),
      "|".join(actorsd[k]),
    ))
print i

actors_writer = csv.writer(open("actors.csv", "w+"))
directors_writer = csv.writer(open("directors.csv", "w+"))
producers_writer = csv.writer(open("producers.csv", "w+"))
screenwriter_writer = csv.writer(open("screenwriter.csv", "w+"))
raw_writer = csv.writer(open("full_raw_features.csv", "w+"))

actors_writer.writerows(actors) 
directors_writer.writerows(directors)
producers_writer.writerows(producers)
screenwriter_writer.writerows(swriter)
raw_writer.writerows(raw_data)
