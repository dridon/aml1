import unicodecsv as csv 

def seek(f, csv, line):
    f.seek(0)
    for i in range(line): 
        next(csv)

moviesf =  open("filtered_data.csv", "r")
actorsf =  open("actor_data.csv", "r")
tcrewf  =  open("technicalCrew.csv", "r")

moviesc = csv.reader(moviesf)
actorsc = csv.reader(actorsf)
tcrewc = csv.reader(tcrewf)

next(actorsc)
next(tcrewc) 

actors = { a[1] for a in actorsc}
directors = { t[2] for t in tcrewc if t[1] == "Director" }

seek(tcrewf, tcrewc, 1)
producers = { t[2] for t in tcrewc if t[1] == "Producer" }

seek(tcrewf, tcrewc, 1)
swriter = { t[2] for t in tcrewc if t[1] == "Screenwriter" }


