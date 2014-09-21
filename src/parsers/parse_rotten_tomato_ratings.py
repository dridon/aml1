from bs4 import BeautifulSoup
from os import listdir 
from os.path import isfile, join 
import unicodecsv as csv 

path = "../html/moviepages" 

files = [ join(path, f) for f in listdir(path) if isfile(join(path,f)) ]
data = [("Movie Name", "Critical Label", "Critic Rating", "Audience Label", "Audience Rating")]

ratings = csv.writer(open("../data/ratings/rotten_tomato_ratings2.csv", "w+"))

i = 0
for f in files:
    soup = BeautifulSoup(open(f, "r"), "lxml")

    mname = f
    mname = mname.split("/")[-1]
    mname = mname.replace(".html", "")

    table = soup.find('table', attrs={'id': 'movie_ratings'})
    if( not table): continue

    rows = table.findAll("tr")
    if(len(rows) < 3): continue 


    tds = rows[2].findAll("td")

    if len(tds) < 2: continue 

    text =  [t.get_text().strip() for t in tds if t.get_text().strip() != ""]

    if len(text) < 2 : continue 

    critic = text[0].split("\n")[1].split("-")
    audience = text[1].split("\n")[1].split("-")


    data.append((mname, critic[1].strip(), critic[0].strip(), audience[1].strip(), audience[0].strip()))
    i = i + 1 

ratings.writerows(data)
print i 
