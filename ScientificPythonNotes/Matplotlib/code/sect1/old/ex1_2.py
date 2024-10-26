import matplotlib.pyplot as plt
import numpy as np 
#this will allow use NumPy's random number generator

xarray=np.arange(20)   #an array of numbers from 0 to 19
yarray=np.arange(20)+3*np.random.randn(20) 
#y is same as x EXCEPT now we vary the value +/- some random number about x

#and now the fun stuff ...
plt.plot(xarray,yarray)
plt.show()
