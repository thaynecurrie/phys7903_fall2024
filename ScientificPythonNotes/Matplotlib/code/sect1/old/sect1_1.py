import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np

def ex1_1():

 xarray=np.arange(20)   #an array of numbers from 0 to 19
 yarray=np.arange(20)+3*np.random.randn(20) 
 #y is same as x EXCEPT now we vary the value +/- some random number about x
 
 #scatter plot of xarray and yarray
 plt.scatter(xarray,yarray)
 
 #show the plot
 plt.show()

def ex1_2():
 xarray=np.arange(20)   
 yarray=np.arange(20)+3*np.random.randn(20) 
 
 #line plot of xarray and yarray
 plt.plot(xarray,yarray,marker='o')
 
 plt.show()

def ex1_3():
 xarray=np.arange(20)   
 yarray=np.arange(20)+3*np.random.randn(20) 

 #https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
 #a polynomial fit of degree one

 a,b=np.polyfit(xarray,yarray,1)
 
 #line plot of xarray and yarray
 plt.scatter(xarray,yarray)
 plt.plot(xarray,xarray*a+b)

 print(a,b)
 
 plt.show()

#with customization
def ex1_4():
 xarray=np.arange(20)   
 yarray=np.arange(20)+3*np.random.randn(20) 

 #https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
 #a polynomial fit of degree one

 a,b=np.polyfit(xarray,yarray,1)

#set symbol size to a random value between 0 and 1

 symsizeval=5*np.random.random(len(yarray))  #same as 5*np.random.rand(20) since the length of yarray is 20 elements
 symsizeval*=150

#set alpha value to be a random number drawn from a normal distribution with mean of 0.5 and sigma of 0.2
 mu,sigma=0.5,0.2
 alphaval=np.random.normal(mu,sigma,len(yarray))

# a simple cheat to catch randomized alpha values that are not between 0.1 and 1 
 bad=np.where((alphaval <= 0.1) | (alphaval > 1))
 alphaval[bad]=0.5
 
 #line plot of xarray and yarray
   #varying color, marker, size, and transparency
 plt.scatter(xarray,yarray,color='g',marker='o',s=symsizeval,edgecolor='black',alpha=alphaval,
      label=r'$Random_{num}$, $\mu = 0.5, \Sigma = 0.2$ for $\alpha$')

 plt.plot(xarray,xarray*a+b,color='tab:blue',linestyle='-.',label='Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b)) #linestyle is same as linestyle='dashdot'

 plt.xlabel('Initial $X_{Array}$',font='serif',size=14,color='gray',weight='heavy')
 plt.ylabel(r'Output,Y$_{\rm Array, random}$',font='Verdana',size=16,style='italic',weight='bold')

 plt.legend(loc='upper left',fontsize='small',borderpad=0.6,markerscale=0.5,
    shadow=False,framealpha=0.7,title='The Random Data')
 
 
 plt.show()

#with customization and fig, axes objects and a subplot call
def ex1_5():
 xarray=np.arange(20)   
 yarray=np.arange(20)+3*np.random.randn(20) 

 #https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
 #a polynomial fit of degree one

 a,b=np.polyfit(xarray,yarray,1)

#set symbol size to a random value between 0 and 1

 symsizeval=5*np.random.random(len(yarray))  #same as 5*np.random.rand(20) since the length of yarray is 20 elements
 symsizeval*=150

#set alpha value to be a random number drawn from a normal distribution with mean of 0.5 and sigma of 0.2
 mu,sigma=0.5,0.2
 alphaval=np.random.normal(mu,sigma,len(yarray))

# a simple cheat to catch randomized alpha values that are not between 0.1 and 1 
 bad=np.where((alphaval <= 0.1) | (alphaval > 1))
 alphaval[bad]=0.5


 fig,axes=plt.subplots(figsize=(9,5))
 
 #line plot of xarray and yarray
   #varying color, marker, size, and transparency
 axes.scatter(xarray,yarray,color='g',marker='o',s=symsizeval,edgecolor='black',alpha=alphaval,
      label=r'$Random_{num}$, $\mu = 0.5, \Sigma = 0.2$ for $\alpha$')

 axes.plot(xarray,xarray*a+b,color='tab:blue',linestyle='-.',label='Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b)) #linestyle is same as linestyle='dashdot'

 axes.set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
 axes.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')

 axes.legend(loc='upper left',fontsize='small',borderpad=0.6,markerscale=0.5,
    shadow=False,framealpha=0.7,title='The Random Data')
 
 
 plt.show()
