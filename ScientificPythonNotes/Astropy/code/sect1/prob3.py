import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np

from astropy.io import fits
from astropy.wcs import WCS
from matplotlib import animation

def prob3():

 import matplotlib as mpl
 #from mpl import animation
 R,G,B,A = mpl.cm.get_cmap('gist_heat')(np.linspace(0.0,1.0,256)).T
 color_vals = np.array([B,G,R,A]).T
 cmap1 = mpl.colors.ListedColormap(color_vals) # colormap for CHARIS image
 cmap1.set_bad('k')

 directory='./files/'
 data_cube=(fits.open(directory+'asdicomb_indiv.fits'))[0].data

 n_lambda=(data_cube.shape)[0]

#general formatting

 rmax=.9 #in units of arc-seconds
 pixelscale=0.01615
 extrange=[rmax,-1*rmax,-1*rmax,rmax]

 fullext_image=pixelscale*(data_cube.shape)[1]/2.0

 cmapval='plasma'
 cmapval=cmap1

 fig,axes=plt.subplots(figsize=(9,9))
 immovie=[]

 axes.set_xlim(rmax,-1*rmax)
 axes.set_ylim(-1*rmax,rmax)
 axes.tick_params(which='both',direction='out',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))
 axes.set_xlabel('$\Delta RA(^{\prime\prime})$',fontsize=16)
 axes.set_ylabel('$\Delta DEC(^{\prime\prime})$',fontsize=16)

 axes.text(0.95*rmax,0.85*rmax,'Exoplanet HIP 99770 b\nSCExAO/CHARIS',fontsize=16,color='w')
 axes.scatter(0,0,marker='*',c='yellow',edgecolor='black',s=500)

# wvlhlabel=axes.text(0.95*rmax,-0.85*rmax,'Wavelength Slice {0:d}'.format(0+1),fontsize=14)
 for i in range(0,n_lambda):
  climsp=np.nanpercentile(data_cube[i,:,:],[0,99.9])
  clims=[-1.5*climsp[1],climsp[1]]
  interpval='hanning'

  im=axes.imshow(data_cube[i,:,:],animated=True,clim=clims,origin='lower',extent=[fullext_image,-1*fullext_image,-1*fullext_image,fullext_image],interpolation=interpval,cmap=cmapval)

  wvlhlabel=axes.text(0.95*rmax,-0.85*rmax,'Wavelength Slice {0:d}'.format(i+1),fontsize=14,animated=True,color='w')
  

  if i== 0:
   im=axes.imshow(data_cube[i,:,:],clim=clims,origin='lower',extent=[fullext_image,-1*fullext_image,-1*fullext_image,fullext_image],interpolation=interpval,cmap=cmapval)
 #  wvlhlabel=axes.text(0.95*rmax,-0.85*rmax,'Wavelength Slice {0:d}'.format(i+1),fontsize=14,color='w')

  immovie.append([im,wvlhlabel])


 ani = animation.ArtistAnimation(fig,immovie,interval=50, blit=False,
                                 repeat_delay=50,repeat=True)

 plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'
 #writergif = animation.PillowWriter(fps=5)
 #ani.save(directory+'problem3.gif',writer=writergif)
 mywriter=animation.FFMpegWriter(fps=5,extra_args=['-vcodec', 'libx264'])
 ani.save(directory+'problem3_.mp4',writer=mywriter)

 plt.show()
