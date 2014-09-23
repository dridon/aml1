import unicodecsv as csv
import regression as rg 

dataf = open('data/features/feature_data.csv', 'rt')
datac = csv.reader(dataf)
next(datac)
m = rg.iter2matrix(datac) 
x = m.T[:-1].T
x = rg.append_ones(x)
y =  m.T[-1:].T
init_weight = np.ones((x.shape[1],1))
final_weight = grad_descent(x,y,init_weight,0.00004,1000)
print final_weight
print rg.mse_error(x,y,final_weight)
