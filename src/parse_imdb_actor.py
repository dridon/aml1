import sys
import requests
import lxml.html
from os import listdir
from os.path import isfile, join 
import unicodecsv as csv 
import re

path = "html//imdb_pages//"
data_reader = csv.reader(open("filtered_data.csv"), delimiter=',')
data_writer = csv.writer(open("imdb_movie_actor.csv", "ab"))
output = [("Movie Name","Actor")]
data_writer.writerows(output)

next(data_reader)

counter=0

for row in data_reader:
    movie_title=row[0]
    html_path=path+re.sub(r"[:|?|']","",movie_title)+".html"
    if isfile(html_path):
        html_page=lxml.html.document_fromstring(open(html_path,"r").read())
        table=html_page.find_class("cast_list")
        if len(table)==0:
            continue
        rows=table[0].findall('tr')
        i=0
        while (i < len(rows)) and (i <= 3):            
            actor=rows[i].xpath('td[2]/a/span/text()')
            if len(actor)==1:
                output = [(movie_title,actor[0])]
                data_writer.writerows(output)
            i=i+1