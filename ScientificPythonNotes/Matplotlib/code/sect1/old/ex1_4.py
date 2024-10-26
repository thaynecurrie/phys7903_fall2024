import matplotlib.pyplot as plt
import numpy as np 
#this will allow use NumPy's random number generator AND use the polynomial fit

xarray=np.arange(20)   #an array of numbers from 0 to 19
yarray=np.arange(20)+3*np.random.randn(20) 
#y is same as x EXCEPT now we vary the value +/- some random number about x

a,b=np.polyfit(xarray,yarray,1) 
#a polynomial fit of degree one look up the documentation if you are curious

plt.scatter(xarray,yarray)
plt.plot(xarray,xarray*a+b)
#print(a,b) # this shows as 1.008, -0.839 for my example

plt.xlabel('x') 
plt.ylabel('y')
plt.show()
