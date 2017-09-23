from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6] , dtype = np.float64)
ys = np.array([5,4,6,5,6,7], dtype = np.float64)

def best_fit_slope_and_intercept(xs,ys) :
	m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
			((mean(xs)*mean(xs)) - mean(xs*xs) ))
	b = mean(ys) - m*mean(xs)
	return m ,b 
def squared_error(ys_orig,ys_line):
	return sum((ys_line-ys_orig)**2)

def coefficent_of_determination(ys_orig,ys_line):
	y_mean_line =[mean(ys_orig)for y in ys_orig]
	squared_error_regr = squared_error(ys_orig,ys_line)
	squared_error_y_mean = squared_error(ys_orig,y_mean_line)
	return 1- (squared_error_regr/squared_error_y_mean)

m,b = best_fit_slope_and_intercept(xs,ys)
regression_line =[(m*x)+b for x in xs] # Get every x in the xs array and get the y values from it while calculating the (mx+b) !
#We can now predict the outputs from this equation ! We have a equation that we found out the m and b of it !
r_squared = coefficent_of_determination(ys,regression_line)
print(r_squared)
plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()