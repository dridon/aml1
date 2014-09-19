from bs4 import BeautifulSoup
from os import listdir 
from os.path import isfile, join 
import unicodecsv as csv 

path = "html/moviepages" 

files = [ join(path, f) for f in listdir(path) if isfile(join(path,f)) ]
writer = csv.writer(open("actor_data.csv", "wb"))
writer.writerow( ["Movie Name", "Actor Name"] )
#data = [("Actor Name")]

for f in files:
    soup = BeautifulSoup(open(f, "r"), "lxml")
    mname = f
    mname = mname.split("/")[-1]
    mname = mname.replace(".html", "")
    #print (mname)
    content = soup.findAll('div', attrs={'id': 'cast'})
    if( not content ):
 	continue
    table = content[0].table
    i = 0;
    castCheck = content[0].find("h1")
    if( castCheck.get_text() != "Cast" ):
        continue
    for r in table.findAll('tr'):
       i = i + 1
       for c in r.find('td'):#Using "find" instead of "findAll" because we're only interested in the actor name and not character name
           writer.writerow( [mname, c.get_text()] )
       if( i == 5 ):
          break


