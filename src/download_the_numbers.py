import urllib2
import time 

url = "http://www.the-numbers.com/movies/letter/"
indices = [str(i + 1) for i in range(9)] + [ chr(ord('A') + i) for i in range(26)]

for i in indices: 
    response = urllib2.urlopen(url + i) 
    file("numbers_html_" + i, "w").write(response.read())
    time.sleep(1)
