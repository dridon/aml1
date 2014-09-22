import sys
import requests
import lxml.html
from os import listdir
from os.path import isfile, join 
import unicodecsv as csv 
import re

path = "../html//imdb_pages//"
data_reader = csv.reader(open("../data/movies/revenue_only_data.csv"), delimiter=',')
data_writer1 = csv.writer(open("../data/people/imdb_movie_crew.csv", "ab"))
data_writer2 = csv.writer(open("../data/people/imdb_movie_actor.csv", "ab"))
output = [("Movie Name","Type","Value")]
data_writer1.writerows(output)
output = [("Movie Name","Actor")]
data_writer2.writerows(output)

next(data_reader)

counter=0

for row in data_reader:
    movie_title=row[0]
    #print movie_title
    html_path=path+re.sub(r"[:|?|']","",movie_title)+".html"
    if isfile(html_path):
        counter=counter+1
        html_page=lxml.html.document_fromstring(open(html_path,"r").read())
        top_div=html_page.get_element_by_id("overview-top")
        if len(top_div)==0:
            continue
        directors=top_div.xpath('*[@itemprop="director"]/a/span/text()')
        for i in range(0,len(directors)):
                output = [(movie_title,"Director",directors[i])]
                data_writer1.writerows(output)
        writers=top_div.xpath('*[@itemprop="creator"]/a/span/text()')
        for i in range(0,len(writers)):
                output = [(movie_title,"Screenwriter",writers[i])]
                data_writer1.writerows(output)
        actors=top_div.xpath('*[@itemprop="actors"]/a/span/text()')
        for i in range(0,len(actors)):
                output = [(movie_title,actors[i])]
                data_writer2.writerows(output)
                
        movie_details=html_page.xpath('//*[@id="titleDetails"]')
        if len(movie_details) !=0:
            prod_cos=movie_details[0].find_class("itemprop")
            if len(prod_cos) !=0:
                output = [(movie_title,"Producer",prod_cos[0].text_content())]
                data_writer1.writerows(output)
    
    #if counter==10:
    #    break
        
