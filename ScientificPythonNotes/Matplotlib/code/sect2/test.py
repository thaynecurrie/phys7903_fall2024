import matplotlib.pyplot as plt
import numpy as np

def run():

 #from matplotlib.ticker import FormatStrFormatter
 from matplotlib import ticker
 from matplotlib.ticker import MultipleLocator,AutoMinorLocator

 xarray=np.arange(20)   #an array of numbers from 0 to 19

#in this example, we are just going to do linear plots

#Panel 1 determination
 yarray=np.arange(20)+3*np.random.randn(20)

 #y is same as x EXCEPT now we vary the value +/- some random number about x

 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

#the default width is 6.4 inches by 4.8 inches, here increase width by 25% using variables
 fig,axes=plt.subplots()
 #fig.subplots_adjust(hspace=0,wspace=0.25)

# turn the fit labels, fit data points, fit colors, data point colors, data point sizes, ...
## data markers (symbols), data alphas ... all to lists

 labels_fits = ['Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b)]

 labels_data=[r'$Random_{num}$',r'$Random_{num}$, quadratic']

 colors_fit=['tab:blue','tab:green','tab:gray']

 colors_data=['tab:blue','orange']

 sizes_data=[150,100]
 marker_data=['o','s']
 alphas_data=[0.7,0.6]

#turn the functional fits into a list

 eq=[xarray*a+b]

#turn the generated data arrays into a list
 dataarr=[yarray]

 i=0

 axes.plot(xarray,eq[i],label=labels_fits[i],c=colors_fit[i])
 axes.scatter(xarray,dataarr[i],marker=marker_data[i],c=colors_data[i],s=sizes_data[i],alpha=alphas_data[i],label=labels_data[i])
 axes.legend(loc='upper left',fontsize='small',handlelength=1,markerscale=0.85)
 axes.set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
 axes.set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')

 axes.tick_params(which='both',width=1.5,direction='in',labelsize='large')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))
 plt.show()
