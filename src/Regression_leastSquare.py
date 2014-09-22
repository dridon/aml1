from bs4 import BeautifulSoup
import math
import unicodecsv as csv 
import numpy as np
import scipy as sp

cols = 3
datapoints = 1500

#Training Matrices
arr = [[0 for x in xrange(cols + 1)] for x in xrange(datapoints)]
X = np.matrix(arr, float, 0)
arrY = [[0] for x in xrange(datapoints)]
Y = np.matrix(arrY, float, 0)

#Test Matrices
'''arrTest = [[0 for x in xrange(cols)] for x in xrange(datapoints + 500)]
XTest = np.matrix(arrTest, float, 0)
arrYTest = [[0] for x in xrange(datapoints + 500)]
YTest = np.matrix(arrYTest, float, 0)
'''
f = open('data/features/feature_data.csv', 'rt')
try:
    reader = csv.reader(f)
    i = -1
    for row in reader:
	i += 1        
	if i == 0 : continue
        elif i > datapoints:
	    break
	for j in xrange(-1, 15) :
	    if( j == -1 ):
		X[(i - 1, j + 1)] = 1
            elif j == 14:
		try:
                     Y[i - 1] = math.log(float(row[j].strip())) #Last column value is "gross"
		except:
	             Y[i - 1] = 1
            elif j == 1:
          	try:
                     X[(i - 1, j + 1)] = math.log(float(row[j + 1].strip()))
		except:
	             X[(i - 1, j + 1)] = 1
		#X[(i - 1, j)] = math.log(X[(i - 1, j)])
	    elif j < cols:
           	X[(i - 1, j)] = row[j]
finally:
    f.close()

#Math
Xprod = X.T*X
XTYProd = X.T*Y
W = Xprod.I * XTYProd
#End of Math

print "For Training Data:"
print Y[1225]
print X[1225]*W

err = Y - (X*W)
err = err.T * err
print err
#Error value =  5.75436772e+18
#Building Test Matrices
'''f = open('feature_data.csv', 'rt')
try:
    reader = csv.reader(f)
    i = -1
    for row in reader:
	i += 1        
	if i == 0 : continue
        elif i > datapoints + 500: #only difference
	    break
	for j in xrange(0, cols + 1) :
            if j == cols:
                YTest[i - 1] = row[j]
	    else:
           	XTest[(i - 1, j)] = row[j]

finally:
    f.close()


print "For Test Data:"
print YTest[datapoints + 24]
print XTest[datapoints + 24]*W
'''
'''
for f in files:
    soup = BeautifulSoup(open(f, "r"), "lxml")
    mname = f
    
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

'''
