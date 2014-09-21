import unicodecsv as csv 
import urllib2 
import time

reader = csv.reader(open("../data/urls/imdb_urls.csv", "r"))
next(reader) 

target_dir = "html/imdb_pages/"

for row in reader:
    if row[1]!='':
        response = urllib2.urlopen(row[1])
        name = target_dir + row[0].replace("/","-") + ".html"
        file(name, "w").write(response.read())
        print("downloaded " + name + "!")
    time.sleep(1)
