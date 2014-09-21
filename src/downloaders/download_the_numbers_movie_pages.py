import unicodecsv as csv 
import urllib2 
import time

reader = csv.reader(open("../data/urls/the_number_movie_urls.csv", "r"))
next(reader) 

target_dir = "../html/moviepages/"

for row in reader: 
    response = urllib2.urlopen(row[1])
    name = target_dir + row[0].replace("/","-") + ".html"
    file(name, "w").write(response.read())
    print("downloaded " + name + "!")

    time.sleep(1)
