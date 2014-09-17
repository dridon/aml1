import unicodecsv as csv 

reader = csv.reader(open("movie_data.csv"), delimiter=',')
data_writer = csv.writer(open("filtered_data.csv", "a+"))
url_writer = csv.writer(open("movie_urls.csv", "a+"))
base_url = "http://www.the-numbers.com"

def date(release_date): 
    month = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3, 
            "Apr": 4, 
            "May": 5, 
            "Jun": 6, 
            "Jul": 7,
            "Aug": 8, 
            "Sep": 9,
            "Oct": 10, 
            "Nov": 11, 
            "Dec": 12,
            }
    split = release_date.split(",")
    split2 = split[0].strip().split()

    return split[1] +  "/" +  str(month[split2[0]]) + "/" +  split2[1]

def currency_number(amt):
    return float("".join(amt[1:].split(",")))

def movie_url(item):
    return (item[0], base_url + item[5])

def movie_data(item):
    return (item[0], date(item[1]), item[2], currency_number(item[3]), currency_number(item[4]))

def load_item(item, data,  url_data): 
    load = True 
    for i in item: 
        if i.strip() == "":
            load = False

    if load: 
        data.append(movie_data(item))
        url_data.append(movie_url(item))

# skip headers
next(reader)

data = [("Movie Name", "Release Date", "Genre", "Budget", "Gross")] 
urls = [("Movie Name", "Url")] 

for row in reader: 
    load_item(row, data, urls)

data_writer.writerows(data)
url_writer.writerows(urls)
