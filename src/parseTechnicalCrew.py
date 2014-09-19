from bs4 import BeautifulSoup
from os import listdir 
from os.path import isfile, join 
import unicodecsv as csv 

path = "html/moviepages" 

files = [ join(path, f) for f in listdir(path) if isfile(join(path,f)) ]
writer = csv.writer(open("technicalCrew.csv", "wb"))
writer.writerow( ["Movie Name", "Role", "Name"] )
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
    contentSize = 0
    for x in content:
        contentSize = contentSize + 1
    if( contentSize < 2 ): 
	continue
    castCheck = content[1].find("h1")
    if( castCheck.get_text() != "Production and Technical Credits" ):
        continue
    table = content[1].table
    for r in table.findAll('tr'):
       columns = r.findAll('td')
       role = columns[0].get_text()
       if( role != "Director" and role != "Producer" and role != "Screenwriter" ):
          continue
       writer.writerow( [mname, columns[0].get_text(), columns[2].get_text()] )

