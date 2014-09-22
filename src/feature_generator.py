import unicodecsv as csv 
import feature_lib as flib

raw_dataf = open("data/features/full_raw_features.csv", "r")
raw_datac = csv.reader(raw_dataf)

next(raw_datac)
flib.raw_data = csv_dict(raw_datac, raw_dataf)
directord, producerd, swriterd, actord = flib.people_dicts(raw_data)

data = flib.get_data(raw_data, directord, producerd, swriterd, actord) 
dataw= [("Hot Season", "Budget", "Director RT Critical Average", "Director RT Public Average", "Director IMDB Average", "Producer RT Critical Average", "Producer RT Public Average", "Producer IMDB Average", "Screenwriter RT Critical Average", "Screenwriter RT Public Average", "Screenwriter IMDB Average","Actors RT Critical Average", "Actors RT Public Average", "Actors IMDB Average", "Gross")] + data

directors = [("Name", "RTC Mean", "RTA Mean", "IMDB Mean")] + dict2list(directord) 
producers = [("Name", "RTC Mean", "RTA Mean", "IMDB Mean")] + dict2list(producerd)
swriters = [("Name", "RTC Mean", "RTA Mean", "IMDB Mean")] + dict2list(swriterd)
actors = [("Name", "RTC Mean", "RTA Mean", "IMDB Mean")] + dict2list(actord)

director_writer = csv.writer(open("data/features/director_data.csv", "w+"))
producer_writer = csv.writer(open("data/features/producer_data.csv", "w+"))
swriter_writer = csv.writer(open("data/features/swriter_data.csv", "w+"))
actor_writer = csv.writer(open("data/features/actor_data.csv", "w+"))
data_writer = csv.writer(open("data/features/feature_data.csv", "w+"))

director_writer.writerows(directors)
producer_writer.writerows(producers)
swriter_writer.writerows(swriters)
actor_writer.writerows(actors)
data_writer.writerows(dataw)
