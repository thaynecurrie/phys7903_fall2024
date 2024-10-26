import matplotlib.pyplot as plt
import numpy as np

def run():
 t = np.arange(0.01, 10.0, 0.01)
 data1 = np.exp(t)
 data2 = np.sin(2 * np.pi * t)
 
 fig, ax1 = plt.subplots()
 
 color = 'tab:red'
 ax1.set_xlabel('time (s)')
 ax1.set_ylabel('exp', color=color)
 ax1.plot(t, data1, color=color)
 ax1.tick_params(axis='y', labelcolor=color)
 
 ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
 
 color = 'tab:blue'
 ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
 ax2.plot(t, data2, color=color)
 ax2.tick_params(axis='y', labelcolor=color)
 
 fig.tight_layout()  # otherwise the right y-label is slightly clipped
 plt.show()


def run2():

 from matplotlib import ticker
 from matplotlib.ticker import MultipleLocator,AutoMinorLocator

 xarray=np.arange(20)   #an array of numbers from 0 to 19

# in this example, we are just going to do one linear plot and one quadratic plot
#Panel 1 determination
 yarray=np.arange(20)+3*np.random.randn(20)

 #y is same as x EXCEPT now we vary the value +/- some random number about x

 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

#Panel 2 determination
 yarray2=(np.arange(20))**2.+20*np.random.randn(20)

#this is equivalent to yarray2[where(yarray2 le 0)] > 0.01 in IDL
  #it basically sets to 0.01 any value from the random number generator that is less than 0
 (yarray2 > 0.0).choose(yarray2,0.01)

 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit


 standardsize=np.array((6.4,4.8))
 scaleval=2
 newsize=list(scaleval*standardsize)

 colors_fit=['tab:blue','tab:green','tab:gray']
 colors_data=['tab:blue','orange']

 eq=[xarray*a+b,poly(xarray)]

 dataarr=[yarray,yarray2]
 sizes_data=[150,100]
 marker_data=['o','s']
 alphas_data=[0.7,0.6]
 
 fig,axes=plt.subplots(figsize=newsize)

 labels_fits = ['Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b),
             r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2)] 

 labels_data=[r'$Random_{num}$',r'$Random_{num}$, quadratic']

 axes.plot(xarray,eq[0],label=labels_fits[0],c=colors_fit[0])
 axes.scatter(xarray,dataarr[0],marker=marker_data[0],c=colors_data[0],s=sizes_data[0],alpha=alphas_data[0],label=labels_data[0])
 axes.legend(loc='upper left',fontsize='small',handlelength=1,markerscale=0.85)
 axes.set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
 axes.set_ylabel(r'Output,$Y_{Array, random,linear}$',font='Verdana',size=14,color='black',weight='bold')

 axes.tick_params(which='both',direction='in',labelsize=18)
 axes.tick_params(which='major',length=7,width=2)
 axes.tick_params(which='minor',length=3.5,width=2)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

 axes.set_ylim(-5,30)

 axes2=axes.twinx()
 
 axes2.set_ylabel(r'Output,$Y_{Array, random,quadratic}$',font='Verdana',size=14,color='black',weight='bold')
 axes2.plot(xarray,eq[1],label=labels_fits[1],c=colors_fit[1])
 axes2.scatter(xarray,dataarr[1],marker=marker_data[1],c=colors_data[1],s=sizes_data[1],alpha=alphas_data[1],label=labels_data[1])
 axes2.legend(loc='upper right',fontsize='small',handlelength=1,markerscale=0.85)
 axes2.tick_params(which='both',direction='in',labelsize=18)
 axes2.tick_params(which='major',length=7,width=2)
 axes2.tick_params(which='minor',length=3.5,width=2)
 axes2.yaxis.set_minor_locator(AutoMinorLocator(10))
 
 axes2.set_ylim(-5,1.2*np.max(dataarr[1]))

 plt.setp(axes.spines.values(),linewidth=2)
 


 
 plt.show() 
