import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

def run():

 from scipy.optimize import leastsq
 N=1000 #number of data points
 t=np.linspace(0,4*np.pi,N)
 data=3*np.sin(t+0.001)+0.5+np.random.randn(N)
 guess_mean=np.mean(data)
 guess_std=3*np.std(data)
 guess_phase =0
 guess_freq=1
 guess_amp=1

 data_first_guess = guess_std*np.sin(t+guess_phase) + guess_mean
 optimize_func = lambda x: x[0]*np.sin(x[1]*t+x[2]) + x[3] - data
 est_amp, est_freq, est_phase, est_mean = leastsq(optimize_func, [guess_amp, guess_freq, guess_phase, guess_mean])[0]
 data_fit = est_amp*np.sin(est_freq*t+est_phase) + est_mean
 fine_t = np.arange(0,max(t),0.1)
 data_fit=est_amp*np.sin(est_freq*fine_t+est_phase)+est_mean
 #plt.plot(t,data,'.',color='tab:blue',alpha=0.7)

 fig,axes=plt.subplots()

 tp=t/np.pi
 axes.scatter(tp,data,color='lime',alpha=0.3,edgecolor='black')
 axes.plot(tp,data_first_guess,label='initial guess')
 axes.plot(fine_t/np.pi,data_fit,label='lst sq fit',color='magenta',linewidth=3)
 axes.fill_between(fine_t/np.pi,data_fit,alpha=0.35)
 axes.set_ylabel('Sine Function',size=14,weight='bold')
 axes.set_xlabel('Angle (Radians)/$\pi$',size=14,weight='bold')
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

 axes.legend(loc='best')
 plt.show()
 
def run2():

 xarray=np.arange(20)   #an array of numbers from 0 to 19
 yarray=np.arange(20)+3*np.random.randn(20)
 #y is same as x EXCEPT now we vary the value +/- some random number about x

 a,b=np.polyfit(xarray,yarray,1)
 #a polynomial fit of degree one look up the documentation if you are curious

 y_est=xarray*a+b
 #y_err=xarray.std()*np.sqrt(1/len(xarray)+(xarray-xarray.mean())**2/np.sum((xarray-xarray.mean())**2.))

#'variance of the predicted response': https://en.wikipedia.org/wiki/Variance_of_the_mean_and_predicted_responses
 y_err=(yarray-y_est).std()*np.sqrt(1/len(xarray) + (xarray-xarray.mean())**2/np.sum((xarray-xarray.mean())**2))

 yarray2=(np.arange(20))**2.+20*np.random.randn(20)

 #polynomial of degree two
 a2,b2,c2=np.polyfit(xarray,yarray2,2)

 poly=np.poly1d(np.polyfit(xarray,yarray2,2))
 #a convenience class to write the polynomial fit

#5 times 'variance of the predicted response': https://en.wikipedia.org/wiki/Variance_of_the_mean_and_predicted_responses
 y_err2=5*(yarray2-poly(xarray)).std()*np.sqrt(1/len(xarray) + (xarray-xarray.mean())**2/np.sum((xarray-xarray.mean())**2))

 fig,axes=plt.subplots(1,2,figsize=(9.6,4.8))
#the default width is 6.4 inches by 4.8 inches, here increase width by 50%

 fig.subplots_adjust(wspace=0.325)
 axes[0].plot(xarray,xarray*a+b,label='Linear fit with y = {0:.2f}*x + {1:.2f}'.format(a,b))
 
 axes[0].fill_between(xarray,y_est-y_err,y_est+y_err,alpha=0.2)
 axes[0].scatter(xarray,yarray,marker='o',s=150,alpha=0.7,label=r'$Random_{num}$',color='brown')
 axes[0].legend(loc='upper left',fontsize='xx-small',handlelength=1,markerscale=0.85)

 axes[1].plot(xarray,poly(xarray),c='tab:green',label=r'Quadratic fit with y = {0:.2f}*$x^2$+{1:.2f}*$x$+{2:.2f}'.format(a2,b2,c2))

 axes[1].fill_between(xarray,poly(xarray)-y_err2,poly(xarray)+y_err2,alpha=0.2)

 axes[1].scatter(xarray,yarray2,marker='s',c='orange',s=50, label=r'$Random_{num}$, quadratic')
 axes[1].legend(loc='upper left',fontsize='xx-small',handlelength=1)

 for i in range(len(axes)):

  axes[i].set_xlabel('Initial $X_{Array}$',font='Verdana',size=14,color='black',weight='bold')
  axes[i].set_ylabel(r'Output,$Y_{Array, random}$',font='Verdana',size=14,color='black',weight='bold')
 
 plt.show()

def run3(agefile='./files/table2cds.dat'):

 import numpy as np
 import math
 import scipy
 import matplotlib.pyplot as plt
 from astropy.io import ascii

 from scipy.stats import gaussian_kde
 import pandas as pd
 import seaborn as sns
 
 tab_sm=ascii.read(agefile)

 names=tab_sm['ID']
 median_age=np.log10(tab_sm['50AgeF']*1e6)

 bmvcolor=tab_sm['B-V']

 redstars=np.where(bmvcolor > 0.7)

 #now make the figure

 fig,ax=plt.subplots(1,1,figsize=(9,6))

#no weights needed
 #weights=np.ones_like(median_age)/len(median_age)
 ax.set_xlabel('log(Age) (yr)')
 ax.set_ylabel('Relative Number of Nearby Stars at a Given Age')
 ax.set_xlim(7,median_age.max())

#for density=True plot
# ax.set_ylim(0,1)

 ax.tick_params(which='both',direction='out',width=2,labelsize='large')
 ax.tick_params(which='major',length=7)
 ax.tick_params(which='minor',length=3.5)
 ax.xaxis.set_minor_locator(AutoMinorLocator(5))
 ax.yaxis.set_minor_locator(AutoMinorLocator(5))
 w=0.125
 nbin=math.ceil((9.75-7)/w)

#sets the maximum equal to ~1 in this case for all histogram plot contributions
 #ax.hist(median_age,bins=nbin,histtype='stepfilled',density='True',stacked='True',lw=3,alpha=0.6,label='All Stars')
 #ax.hist(median_age[redstars],bins=nbin,histtype='stepfilled',density='True',stacked='True',lw=3,alpha=0.25,color='lime',label=r'Red Stars (B-V) $>$ 0.7')

#sets the maximum to the actual maximum value in the bin
 #n,bins,patches=ax.hist(median_age,bins=nbin,histtype='stepfilled',stacked='True',lw=3,alpha=0.6,label='All Stars')

#returns a tuple to give you the number in each bin, number of bins, and patches
 n,bins,patches=ax.hist(median_age,bins=nbin,histtype='stepfilled',stacked='True',lw=3,alpha=0.6,label='All Stars')


 ax.hist(median_age[redstars],bins=nbin,histtype='stepfilled',stacked='True',lw=3,alpha=0.5,color='lime',label=r'Red Stars (B-V $>$ 0.7)')

 #pd.DataFrame(median_age).plot(kind='density')
 #kde=gaussian_kde(median_age)
 #mn,mx=ax.get_xlim()
 #kde_xs=np.linspace(mn,mx,nbin)
 #ax.plot(kde_xs,kde,lw=3)
 #sns.kdeplot(median_age)

 ax.set_ylim(0,n.max())

 ax.axvline(x=np.log10(5e8),c='C1',linestyle='dashed',linewidth=2)
 ax.axvline(x=np.log10(4e7),c='magenta',linestyle='dashed',lw=2)
 ax.axvline(x=np.log10(4.5e9),c='cyan',linestyle='dashed',lw=2)
 ax.text(np.log10(4.5e9)-.25,0.75*n.max(),'4.5 Gyr')
 ax.text(np.log10(5e8)+0.01,0.65*n.max(),'500 Myr')
 ax.text(np.log10(4e7)+0.01,0.5*n.max(),'40 Myr')
 ax.legend(loc='upper left',fontsize=14)

 plt.setp(ax.spines.values(),linewidth=2)
 plt.show()


def run4(agefile='./files/table2cds.dat'):

 import numpy as np
 import math
 import scipy
 import matplotlib.pyplot as plt
 from matplotlib import colors
 from astropy.io import ascii

 from scipy.stats import gaussian_kde
 import pandas as pd
 import seaborn as sns
 
 tab_sm=ascii.read(agefile)

 names=tab_sm['ID']
 median_age=np.log10(tab_sm['50AgeF']*1e6)

 bmvcolor=tab_sm['B-V']

 redstars=np.where(bmvcolor > 0.7)

 #now make the figure

 fig,ax=plt.subplots(1,1,figsize=(9,6))

#no weights needed
 #weights=np.ones_like(median_age)/len(median_age)
 ax.set_xlabel('log(Age) (yr)')
 ax.set_ylabel('Relative Number of Nearby Stars at a Given Age')
 ax.set_xlim(7,median_age.max())

#for density=True plot
# ax.set_ylim(0,1)

 ax.tick_params(which='both',direction='out',width=2,labelsize='large')
 ax.tick_params(which='major',length=7)
 ax.tick_params(which='minor',length=3.5)
 ax.xaxis.set_minor_locator(AutoMinorLocator(5))
 ax.yaxis.set_minor_locator(AutoMinorLocator(5))
 w=0.125
 nbin=math.ceil((9.75-7)/w)

#sets the maximum equal to ~1 in this case for all histogram plot contributions
 #ax.hist(median_age,bins=nbin,histtype='stepfilled',density='True',stacked='True',lw=3,alpha=0.6,label='All Stars')
 #ax.hist(median_age[redstars],bins=nbin,histtype='stepfilled',density='True',stacked='True',lw=3,alpha=0.25,color='lime',label=r'Red Stars (B-V) $>$ 0.7')

#sets the maximum to the actual maximum value in the bin
 #n,bins,patches=ax.hist(median_age,bins=nbin,histtype='stepfilled',stacked='True',lw=3,alpha=0.6,label='All Stars')

#returns a tuple to give you the number in each bin, number of bins, and patches
 #n,bins,patches=ax.hist(median_age,bins=nbin,histtype='stepfilled',stacked='True',lw=3,alpha=0.6,label='All Stars')



# ax.hist(median_age[redstars],bins=nbin,histtype='stepfilled',stacked='True',lw=3,alpha=0.5,color='lime',label=r'Red Stars (B-V $>$ 0.7)')

 ax.hist2d(median_age,bmvcolor,bins=[4*nbin,2*nbin],cmin=-1,cmax=60,norm=colors.PowerNorm(0.3))
#LogNorm())
#norm=colors.LogNorm())
 ax.set_xlim(7.5,10)
 ax.set_ylim(0.45,1.75)
 #cax=fig.add_axes([1,.1,0.1,1)
 #cb=plt.colorbar()
 #cb.set_label('counts in bin')

 #pd.DataFrame(median_age).plot(kind='density')
 #kde=gaussian_kde(median_age)
 #mn,mx=ax.get_xlim()
 #kde_xs=np.linspace(mn,mx,nbin)
 #ax.plot(kde_xs,kde,lw=3)
 #sns.kdeplot(median_age)

 #ax.set_ylim(0,n.max())

 #ax.axvline(x=np.log10(5e8),c='C1',linestyle='dashed',linewidth=2)
 #ax.axvline(x=np.log10(4e7),c='magenta',linestyle='dashed',lw=2)
 #ax.axvline(x=np.log10(4.5e9),c='cyan',linestyle='dashed',lw=2)
 #ax.text(np.log10(4.5e9)-.25,0.75*n.max(),'4.5 Gyr')
 #ax.text(np.log10(5e8)+0.01,0.65*n.max(),'500 Myr')
 #ax.text(np.log10(4e7)+0.01,0.5*n.max(),'40 Myr')
 #ax.legend(loc='upper left',fontsize=14)

 plt.setp(ax.spines.values(),linewidth=2)
 plt.show()

def run5():
 
 import matplotlib.pyplot as plt
 import numpy as np
 from matplotlib.ticker import AutoMinorLocator

 x=np.random.normal(size=10000)
 y=x*3 + np.random.normal(size=10000)-1.5*np.random.randn(10000)

 fig,axes=plt.subplots()
 
 hist_2d=axes.hist2d(x,y,bins=(25,25))

 axes.set_xlabel('X Variable')
 axes.set_ylabel('Y Variable')
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))
 fig.colorbar(hist_2d[3],ax=axes,label='Counts')
 plt.show() 

def run6():
 
 import matplotlib.pyplot as plt
 import numpy as np
 from matplotlib.ticker import AutoMinorLocator

 x=np.random.normal(size=10000)
 y=x*3 + np.random.normal(size=10000)-1.5*np.random.randn(10000)

 #fig,axes=plt.subplots()
 fig=plt.figure(figsize=(7,7))
 gs=fig.add_gridspec(2,2,width_ratios=(4,1),height_ratios=(1,4),left=0.1,right=0.9,bottom=0.1,top=0.9,wspace=0.05,hspace=0.05)
 axes=fig.add_subplot(gs[1,0])
 ax_histx=fig.add_subplot(gs[0,0],sharex=axes)
 ax_histy=fig.add_subplot(gs[1,1],sharey=axes)
 
 hist_2d=axes.hist2d(x,y,bins=(25,25))

 axes.set_xlabel('X Variable')
 axes.set_ylabel('Y Variable')
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))
 axes.tick_params(labeltop=True)
 #fig.colorbar(hist_2d[3],ax=axes,label='Counts')

 ax_histx.hist(x,bins=25)
#now, re-set the ticks
 #ax_histx.tick_params(labeltop=True,labelbottom=False,bottom=False,top=True,left=True,labelleft=True)
 #ax_histx.tick_params(labeltop=True)
 ax_histx.xaxis.set_ticks_position('top')
 ax_histx.xaxis.set_label_position('top')
 ax_histx.xaxis.set_minor_locator(AutoMinorLocator(5))
 ax_histx.yaxis.set_minor_locator(AutoMinorLocator(5))
 ax_histx.set_ylabel('Number')
 ax_histx.set_xlabel('X Variable')

 #ax_histy.tick_params(labeltop=True,labelbottom=True,top=True,bottom=False)
 ax_histy.hist(y,bins=25,orientation='horizontal')
 ax_histy.xaxis.set_ticks_position('top')
 ax_histy.xaxis.set_label_position('top')
 ax_histy.yaxis.set_ticks_position('right')
 ax_histy.yaxis.set_label_position('right')
 ax_histy.xaxis.set_minor_locator(AutoMinorLocator(5))
 ax_histy.yaxis.set_minor_locator(AutoMinorLocator(5))
 ax_histy.set_xlabel('Number')
 #ax_histy.set_ylabel('Y Variable')
 ax_histy.set_ylabel('Y Variable',rotation=270)
#,rotation=180,ha='right')
#ax_histy.getyticks()rotation=180,ha='right')
 #ax_histy.set_yticklabels(ax_histy.get_yticklabels(),rotation=180)
 

 plt.show() 

def run7():
#From Scientific Computing With Python

 import matplotlib.pyplot as plt
 import numpy as np
 from matplotlib.ticker import AutoMinorLocator

 rosenbrockfunction= lambda x,y: (1-x)**2+100*(y-x**2)**2
 X,Y=np.meshgrid(np.linspace(-0.5,2,100),np.linspace(-1,4,100))
 Z=rosenbrockfunction(X,Y)
 
 fig,axes=plt.subplots(figsize=(7,7))
 
 axes.set_xlabel('X Variable')
 axes.set_ylabel('Y Variable')
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

 contour=axes.contour(X,Y,Z,np.logspace(-0.5,3.5,20,base=10),cmap='rainbow')
 axes.clabel(contour,contour.levels[1:],inline=True,fontsize=10,colors='black')

 plt.show() 


def run8():

 import matplotlib.pyplot as plt
 import numpy as np
 from matplotlib.ticker import AutoMinorLocator
 import matplotlib.colors
 from matplotlib.colors import LogNorm

 from astropy.io import fits
 from astropy.wcs import WCS

 hst_stis=fits.open('./files/stisabaurcomball.fits')[0]
 image=hst_stis.data
 
 wcs=WCS(hst_stis.header)

 imdim=image.shape
 center=np.array(imdim)//2
 print(center)

# x,y=np.meshgrid(imdim,imdim)
# print('x is',x)

 #fig,axes=plt.subplots(figsize=(10,8)) #x and y coordinates
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(10,8))


 windowsize=75
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))
 axes.tick_params(which='both',width='1.5',labelsize='large')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 axes.xaxis.set_ticks_position('both')
 axes.yaxis.set_ticks_position('both')
 axes.set_xlabel('Right Ascension',fontsize=16)
 axes.set_ylabel('Declination',fontsize=16)

 axes.imshow(image,origin='lower',norm=LogNorm(),clim=(.5,1000),cmap='jet')

 plt.show()

def run9a():

 import matplotlib.pyplot as plt
 import numpy as np
 from matplotlib.ticker import AutoMinorLocator
 import matplotlib.colors
 from matplotlib.colors import LogNorm

 from astropy.io import fits
 from astropy.wcs import WCS

 hst_stis=fits.open('./files/stisabaurcomball.fits')[0]
 image=hst_stis.data
 
 wcs=WCS(hst_stis.header)

 imdim=image.shape
 center=np.array(imdim)//2
 print(center)

# x,y=np.meshgrid(imdim,imdim)
# print('x is',x)

 #fig,axes=plt.subplots(figsize=(10,8)) #x and y coordinates
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(10,8))


 windowsize=75
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))
 axes.tick_params(which='both',width='1.5',labelsize='large')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 axes.xaxis.set_ticks_position('both')
 axes.yaxis.set_ticks_position('both')
 axes.set_xlabel('Right Ascension',fontsize=16)
 axes.set_ylabel('Declination',fontsize=16)

 axes.imshow(image,origin='lower',norm=LogNorm(),clim=(.5,1000),cmap='jet')

 levels=np.logspace(np.log10(1),np.log10(1000),10)
 imagecontour=axes.contour(image,levels,linestyles='-',colors='white')

 axes.clabel(imagecontour,imagecontour.levels,inline=True,fontsize=11,colors='black')


 norm=matplotlib.colors.LogNorm(levels.min(),levels.max())
 sm=plt.cm.ScalarMappable(cmap='jet',norm=norm)
 sm.set_clim(vmin=0.5,vmax=1000)
 sm.set_array([])
 fig.colorbar(sm,ticks=(levels[0],100,1000),cmap='jet',format='%d')

 axes.set_title('AB Aurigae, with Contours',fontsize=16,fontweight='bold',pad=15)

 plt.show()
def run9b():

 import matplotlib.pyplot as plt
 import numpy as np
 from matplotlib.ticker import AutoMinorLocator
 import matplotlib.colors
 from matplotlib.colors import LogNorm

 from astropy.io import fits

 image=fits.open('./files/stisabaurcomball.fits')[0].data
 imdim=image.shape
 center=np.array(imdim)//2
 print(center)

 x,y=np.meshgrid(imdim,imdim)
 print('x is',x)

 fig,axes=plt.subplots()

 axes.imshow(image,origin='lower',norm=LogNorm(),clim=(.5,1000),cmap='jet')

 #axes.imshow(image,origin='lower',clim=(1,300),cmap='magma')
#cmap='nipy_spectral')
 #axes.set_cmap('nipy_spectral')
 
#,extent=(-50+center[0],+50+center[0],-50+center[1],+50+center[1]))
 #axes.set_xlim(-50+center[0],+50+center[0])
 #axes.set_ylim(-50+center[1],+50+center[1])

 windowsize=75
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

#this gets messy with the color bar
 levels=np.logspace(np.log10(1),np.log10(1000),10)
 #levels=[1,10,100,200,500,1000]
 imagecontour=axes.contour(image,levels,alpha=0.5,colors='magenta')
#,levels=levels,alpha=0.5)

 norm=matplotlib.colors.LogNorm(imagecontour.cvalues.min(),imagecontour.cvalues.max())
 sm=plt.cm.ScalarMappable(cmap='jet',norm=norm)
 sm.set_clim(vmin=0.5,vmax=1000)
 sm.set_array([])

 fig.colorbar(sm,ticks=(levels[0],100,1000),cmap='jet',format='%d')
 plt.show()
