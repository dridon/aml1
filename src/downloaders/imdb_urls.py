import lxml.html
import requests
import unicodecsv as csv
import time

data_reader = csv.reader(open("../data/movies/revenue_only_data.csv"), delimiter=',')
data_writer = csv.writer(open("../data/urls/imdb_urls.csv", "ab"))
base_url = "http://www.imdb.com"

next(data_reader)

output = [("Movie Name", "IMDB URL")]

data_writer.writerows(output)

for row in data_reader: 
    movie_title=row[0]
    search_page=lxml.html.document_fromstring(requests.get("http://www.imdb.com/search/title?title="+movie_title+"&title_type=feature").content)
    mv_count=len(search_page.find_class("number"))
    find_chk=0
    for i in range(2,mv_count+2):
        search_mv_title=search_page.xpath('//*[@class="results"]/tr['+str(i)+']/td[3]/a/text()')[0].strip()
        if movie_title.lower()==search_mv_title.lower():
            imdb_url=search_page.xpath('//*[@class="results"]/tr['+str(i)+']/td[3]/a/@href')[0].strip()
            output=[(movie_title,base_url+imdb_url)]
            find_chk=1
            break
    if find_chk==0:
        output=[(movie_title,"")]
    data_writer.writerows(output)
    print movie_title +" - "+ str(find_chk)
