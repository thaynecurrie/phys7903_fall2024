import matplotlib.pyplot as plt
import numpy as np 

#this will allow use NumPy's random number generator AND use the polynomial fit

xarray=np.arange(20)   #an array of numbers from 0 to 19
yarray=np.arange(20)+3*np.random.randn(20) 
#y is same as x EXCEPT now we vary the value +/- some random number about x

a,b=np.polyfit(xarray,yarray,1) 
#a polynomial fit of degree one look up the documentation if you are curious

yarray2=(np.arange(20))**2.++3*np.random.randn(20) 
#a2,b2=np.polyfit(xarray.flatten(),yarray2.flatten(),2)
#z=np.polyfit(xarray.flatten(),yarray2.flatten(),2)
#poly=np.poly1d(np.polyfit(xarray.flatten(),yarray2.flatten(),2))
poly=np.poly1d(np.polyfit(xarray,yarray2,2))
#a second array with a second fit


fig,axes=plt.subplots(1,2,figsize=(12,6))
axes[0].scatter(xarray,yarray)
axes[0].plot(xarray,xarray*a+b)
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

axes[1].scatter(xarray,yarray2)
#axes[1].plot(xarray,xarray*a2+b2)
axes[1].plot(xarray,poly(xarray))
axes[1].set_xlabel('X2')
axes[1].set_ylabel('Y2')

plt.show()
