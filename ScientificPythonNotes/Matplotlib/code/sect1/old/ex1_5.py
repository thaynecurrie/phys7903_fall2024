import matplotlib.pyplot as plt
import numpy as np 
#this will allow use NumPy's random number generator AND use the polynomial fit

xarray=np.arange(20)   #an array of numbers from 0 to 19
yarray=np.arange(20)+3*np.random.randn(20) 
#y is same as x EXCEPT now we vary the value +/- some random number about x

a,b=np.polyfit(xarray,yarray,1) 
#a polynomial fit of degree one look up the documentation if you are curious

fig,axes=plt.subplots() # we will describe subplots in more detail in a bit: simmer down for now
axes.scatter(xarray,yarray)
axes.plot(xarray,xarray*a+b)
axes.set_xlabel('X') #note the different syntax
axes.set_ylabel('Y') #note the different syntax
plt.show()
