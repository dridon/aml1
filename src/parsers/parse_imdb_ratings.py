import sys
import requests
import lxml.html
from os import listdir
from os.path import isfile, join 
import unicodecsv as csv 
import re

path = "../html//imdb_pages//"
data_reader = csv.reader(open("../data/movies/revenue_only_data.csv"), delimiter=',')
data_writer = csv.writer(open("../data/ratings/imdb_movie_rating.csv", "ab"))
output = [("Movie Name", "IMDB Rating")]
data_writer.writerows(output)

next(data_reader)
counter=0

for row in data_reader: 
    movie_title=row[0]
    user_rating=''
    html_path=path+re.sub(r"[:|?|']","",movie_title)+".html"
    if isfile(html_path):
        print movie_title
        html_page=lxml.html.document_fromstring(open(html_path,"r").read())
        try:
            user_rating=html_page.xpath('//*[@id="overview-top"]/div[3]/div[3]/strong/span/text()')[0]
        except Exception:
            user_rating=''
    #    try:
    #        metascore=html_page.xpath('//*[@id="overview-top"]/div[3]/div[3]/a[2]/text()')[0].strip().split('/')[0]
    #    except Exception:
    #        metascore=''
        if user_rating!='':
            output=[(movie_title,user_rating)]
            data_writer.writerows(output)
    #counter=counter+1
    #if counter==10:
    #    break
