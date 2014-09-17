from bs4 import BeautifulSoup
from os import listdir 
from os.path import isfile, join 
import unicodecsv as csv 

path = "html/the-numbers/" 

files = [ join(path, f) for f in listdir(path) if isfile(join(path,f)) ]

data = [("Movie Name", "Release Date", "Genre", "Budget", "Gross Revenue", "Url")]

for f in files: 
    soup = BeautifulSoup(open(f, "r"), "lxml")
    cols = [ r.find_all("td") for r in soup.find_all("tr") if len(r.find_all("td")) > 5]

    for c in cols:
        data.append((c[1].get_text(), c[0].get_text(), c[2].get_text(), c[3].get_text(), c[4].get_text(), c[1].find("a")['href']))

writer = csv.writer(open("movie_data.csv", "wb"))
writer.writerows(data) 
