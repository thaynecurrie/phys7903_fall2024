import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import ticker
import numpy as np

from astropy.io import fits
from astropy.wcs import WCS
from astropy.visualization import quantity_support
from matplotlib import animation

import astropy.units as u
from astropy.coordinates import SkyCoord

def ex2_1():
 R_eff=29*u.pc
 #R_eff=u.Quantity(29,unit=u.pc) # does the same thing

 print("""Half light radius
 value: {0}
 unit: {1}""".format(R_eff.value, R_eff.unit))

 #print("The Half light radius value is {0:.1f} and unit is {1:s}".format(R_eff.value,R_eff.unit))
 
 print("{0:.3g}".format(R_eff.to(u.m))) # meters
#8.95e+17 m
 print("{0:.3g}".format(R_eff.to(u.lyr))) # light-years
#94.6 lyr
 print("{0:.3g}".format(R_eff.to(u.um))) # microns
#8.95e+23 um

 vmean = 206
 sigin = 4.3
 v = np.random.normal(vmean, sigin, 500)*u.km/u.s

 import matplotlib.pyplot as plt
 fig,axes=plt.subplots()
 axes.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
 axes.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
 axes.tick_params(which='both', axis='x',direction='in')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 axes.set_xlabel('Velocity in {0:s}'.format(v.unit),fontsize=14)
 axes.set_ylabel('Relative Number',fontsize=14)

 axes.hist(v.value,bins=50,density=True,color='tab:green')
 plt.show() 


 
def ex2_2():
 R_eff=29*u.pc
 #R_eff=u.Quantity(29,unit=u.pc) # does the same thing

 print("""Half light radius
 value: {0}
 unit: {1}""".format(R_eff.value, R_eff.unit))

 #print("The Half light radius value is {0:.1f} and unit is {1:s}".format(R_eff.value,R_eff.unit))
 
 print("{0:.3g}".format(R_eff.to(u.m))) # meters
#8.95e+17 m
 print("{0:.3g}".format(R_eff.to(u.lyr))) # light-years
#94.6 lyr
 print("{0:.3g}".format(R_eff.to(u.um))) # microns
#8.95e+23 um

 vmean = 206
 sigin = 4.3
 v = np.random.normal(vmean, sigin, 500)*u.km/u.s

 import matplotlib.pyplot as plt

 fig,axes=plt.subplots()
 quantity_support()

 axes.tick_params(which='both', axis='x',direction='in')
 axes.tick_params(which='major',length=6)
 axes.tick_params(which='minor',length=3)
 axes.set_ylabel('Relative Number',fontsize=14)
 axes.hist(v,bins='auto',histtype='step')

 plt.show()
 
def ex2_3():
 from astropy.constants import G, h, k_B

 R_eff=29*u.pc
 #R_eff=u.Quantity(29,unit=u.pc) # does the same thing

 print("""Half light radius
 value: {0}
 unit: {1}""".format(R_eff.value, R_eff.unit))

 #print("The Half light radius value is {0:.1f} and unit is {1:s}".format(R_eff.value,R_eff.unit))
 
 print("{0:.3g}".format(R_eff.to(u.m))) # meters
#8.95e+17 m
 print("{0:.3g}".format(R_eff.to(u.lyr))) # light-years
#94.6 lyr
 print("{0:.3g}".format(R_eff.to(u.um))) # microns
#8.95e+23 um

 vmean = 206
 sigin = 4.3
 v = np.random.normal(vmean, sigin, 500)*u.km/u.s

 sigma = np.sqrt(np.sum((v - np.mean(v))**2) / np.size(v))
 print("Velocity dispersion: {0:.2f}".format(sigma))

 sigma_scalar = np.sqrt(np.sum((v - np.mean(v))**2) / len(v))

 M = 4*sigma**2*R_eff/G
 M
 M.decompose()
 print(M)
 print(M.decompose())

 print("""Galaxy mass
 in solar units: {0:.3g}
 SI units: {1:.3g}
 CGS units: {2:.3g}""".format(M.to(u.Msun), M.si, M.cgs))
 print(np.log10(M.to_value(u.Msun)))
 print(np.log10(M.value))
def ex1_1b():

 directory='./files/'
  
 hdu=fits.open(directory+'keckimage.fits')
 #or, hdu=fits.open('./files/n0023f.fits')


#info 
 hdu.info()

#data
 image=hdu[0].data
#print(image.shape)


 image_header=hdu[0].header
#print(image_header[0:10])

#read out some of the header
 print(image_header['LAT'])

#update the header 
# print(image_header['OBJECT'])
# image_header['OBJECT']='kappa And'
# print(image_header['OBJECT'])

 fig,axes=plt.subplots(figsize=(8,6))
 clims=np.nanpercentile(image,[0,99.5])

# axes.imshow(image) #default
 axes.imshow(image,origin='lower',cmap='viridis',clim=clims) #change the origin, note: viridis is the default

#do this if you want to later add a colorbar
# image1=axes.imshow(image,origin='lower',cmap='viridis',clim=clims) #change the origin, note: viridis is the default

#customize
 #center=np.array(imdim)//2
 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)
 axes.set_xlabel('X Pixel Value',fontsize=14)
 axes.set_title('Keck/NIRC2 Image',fontsize=16)
 axes.set_ylabel('Y Pixel Value',fontsize=14) 
 
 #axes.set_xlabel()
 #axes.set_ylabel()
 #axes.xaxis.set_ticklabels([])
 #axes.yaxis.set_ticklabels([])
 axes.tick_params(which='both',width='1.75',labelsize=12)
 #axes.tick_params(which='major',length=7)
 #axes.tick_params(which='minor',length=3.5)
 #axes.xaxis.set_ticks_position('none')
 #axes.yaxis.set_ticks_position('none')
 #axes.xaxis.set_minor_locator(AutoMinorLocator(5))

#if you want to add a colorbar
#note: colorbar is a property of figure, not axes
# fig.colorbar(image1,ax=axes,orientation='vertical')

 plt.show()


def ex1_1b():

 directory='./files/'

 hdu=fits.open(directory+'keckimageext.fits')
 hdu.info()

#data
 image=hdu[1].data
 #or ...
 #image=fits.getdata(directory+'keckimageext.fits')

 primary_header=hdu[0].header
 ext_header=hdu[1].header


def ex1_2():
 directory='./files/'

#First Image
 hdu=fits.open(directory+'keckimage.fits')

#data
 image=hdu[0].data
#header
 image_header=hdu[0].header

#dimensions of the image

#Second Image

 hdu2=fits.open(directory+'secondkeckimage.fits')
 image2=hdu2[0].data

 meanval=np.nanmean(image)
 meanval2=np.nanmean(image2)

 psfsubimage=image-image2*(meanval/meanval2)
 #psfsubimage=image-image2

 #update the header
 image_header['OBJECT']='kappa And'

#write the new file
 fits.writeto(directory+'psfsubimage.fits',psfsubimage,image_header,overwrite=True)
 
#display the new file
 fig,axes=plt.subplots(figsize=(8,6))

 clims=np.nanpercentile(psfsubimage,[3,99])

 axes.imshow(psfsubimage,origin='lower',clim=clims) #change the origin

 axes.set_title('Simple PSF Subtraction',fontsize=18)
 axes.set_xlabel('X Pixel Value',fontsize=14)
 axes.set_ylabel('Y Pixel Value',fontsize=14)

 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 axes.add_patch(plt.Circle([318,111],10,color='white',fill=False))

 #Other way ...
 #from matplotlib.patches import Circle
 #circle1=Circle([318,111],10,color='white',fill=False)
 #axes.add_patch(circle1)

 plt.show()
def ex1_2b():

 directory='./files/'

#First Image
 hdu=fits.open(directory+'keckimageext.fits')

#data
 image=hdu[1].data
#header
 image_header0=hdu[0].header
 image_header1=hdu[1].header

#dimensions of the image

#Second Image

 hdu2=fits.open(directory+'secondkeckimage.fits')
 image2=hdu2[0].data

 meanval=np.nanmean(image)
 meanval2=np.nanmean(image2)

 psfsubimage=image-image2*(meanval/meanval2)
 #psfsubimage=image-image2

 #update the header
 image_header0['OBJECT']='kappa And'

 fits.HDUList([fits.PrimaryHDU(header=image_header0),fits.ImageHDU(psfsubimage,header=image_header1)]).writeto('psfsubext.fits',overwrite=True)

#simple display
 fig,axes=plt.subplots(figsize=(8,6))

 clims=np.nanpercentile(psfsubimage,[3,99])

 axes.imshow(psfsubimage,origin='lower',clim=clims) #change the origin

 axes.set_title('Simple PSF Subtraction',fontsize=18)
 axes.set_xlabel('X Pixel Value',fontsize=14)
 axes.set_ylabel('Y Pixel Value',fontsize=14)

 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)


 plt.show()
def ex1_3a():

 directory='./files/'

 hdu=fits.open(directory+'psfsubimage.fits')

#data
 image=hdu[0].data
 image_header=hdu[0].header

#dimensions of the image

 wcs=WCS(image_header)
#simple display
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(8,6))

 clims=np.nanpercentile(image,[3,99])

 axes.imshow(image,origin='lower',clim=clims) #change the origin

#customize
 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 plt.show()
def ex1_3b():
 directory='./files/'

 hdu=fits.open(directory+'psfsubimage.fits')

#data
 image=hdu[0].data
 image_header=hdu[0].header

 wcs=WCS(image_header)
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(8,6))

 axes.coords[0].set_ticklabel_visible(False)
 axes.coords[1].set_ticklabel_visible(False)
 overlay=axes.get_coords_overlay('fk5')
 overlay[0].set_major_formatter('hh:mm:ss.s') #to move the formatting out of degrees for RA
 overlay.grid(color='white',ls='solid',alpha=0.5)

 overlay[0].set_axislabel('Right Ascension (J2000)',fontsize=16)
 overlay[1].set_axislabel('Declination (J2000)',fontsize=16)
 overlay[0].set_axislabel_position('b') #b=bottom,l=left,t=top,r=right
 overlay[1].set_axislabel_position('l')

 overlay[0].set_ticklabel_position('bt')
 overlay[1].set_ticklabel_position('lr')

 clims=np.nanpercentile(image,[3,99])

 axes.imshow(image,origin='lower',clim=clims) #change the origin
 #padding more than the default of 6 to make sure labels don't collide
 axes.set_title('With Overlays',fontsize=18,pad=30) 
#customize
 center=np.array([173,252])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 plt.show()

def ex1_3c():

 directory='./files/'

 #doing this instead of image=(fits.open[filename])[0].data
 image=fits.getdata(directory+'psfsubimage_northup.fits')

 image_header=(fits.open('./files/psfsubimage_northup.fits'))[0].header

 wcs=WCS(image_header)
 fig,axes=plt.subplots(subplot_kw={'projection':wcs},figsize=(10,6))

 axes.coords[0].set_ticklabel_visible(False)
 axes.coords[1].set_ticklabel_visible(False)
 overlay=axes.get_coords_overlay('fk5')
 overlay[0].set_major_formatter('hh:mm:ss.s')
 overlay.grid(color='white',ls='solid',alpha=0.3)

 overlay[0].set_axislabel('Right Ascension (J2000)',size=14)
 overlay[1].set_axislabel('Declination (J2000)',size=14)
 overlay[0].set_axislabel_position('b')
 overlay[1].set_axislabel_position('l')


 overlay[0].set_ticklabel(size=12)
 overlay[1].set_ticklabel(size=12)
 overlay[0].set_ticklabel_position('bt')
 overlay[1].set_ticklabel_position('lr')

 clims=np.nanpercentile(image,[3,99])

 #axes.imshow(image,origin='lower',clim=clims,cmap='magma') #change the origin
#you need to do the below in order to display a colorbar
 image1=axes.imshow(image,origin='lower',clim=clims,cmap='magma') #change the origin

#customize
#it's different than before since the star was not at the center and the program I use to 'north-up' the image rotates from the image center
 center=np.array([340,250])
 windowsize=150
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 axes.tick_params(which='both',width='1.75')
 axes.tick_params(which='major',length=7)
 axes.tick_params(which='minor',length=3.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.set_title("North-Up Image, With Colorbar",fontsize=18,pad=30)

 axes.add_patch(plt.Circle([182,397],10,color='white',fill=False))

 cbar=fig.colorbar(image1,orientation='vertical',pad=0.15,shrink=0.95)
 cbar.set_label(label='Counts (e/s)',size=14)


 plt.show()

def ex1_4():
#RGB images

 directory='./files/'
 jband=(fits.open(directory+'jband2.fits'))[0].data
 hband=(fits.open(directory+'hband2.fits'))[0].data
 kband=(fits.open(directory+'kband2.fits'))[0].data

 cmaps=['Blues','Greens','Reds']

 fig,axes=plt.subplots(figsize=(9,9))

 #import img_scale
 imagecomb=np.zeros((201,201,3),dtype=float)
 print(kband.shape)
 jnorm=0.04
 hnorm=0.03
 knorm=0.035

 jnorm=0.0375
 hnorm=0.0325
 knorm=0.0325
 imagecomb[:,:,0]=kband/knorm
 imagecomb[:,:,1]=hband/hnorm
 imagecomb[:,:,2]=jband/jnorm


 windowsize=60
 center=((jband.shape)[0]//2,(jband.shape)[0]//2)
 axes.set_ylim(center[0]-windowsize,center[0]+windowsize)
 axes.set_xlim(center[1]-windowsize,center[1]+windowsize)

 import astropy.units as u

 #converting to arcsec
 print((jband.shape)[0])
 pixscale=0.01615*(u.arcsec/u.pixel)

 dim=(jband.shape)[0]
 distfromcenter=np.array([0,dim,0,dim])-100.5

 distfromcenter=distfromcenter << u.pixel
 pixscale = pixscale << u.arcsec/u.pixel
 distfromcenter_arcsec=(distfromcenter*pixscale).value

 #distfromcenter=(np.array([0,201,0,201])-100.5)
 #distfromcenter_arcsec=distfromcenter*0.01615
 #print(distfromcenter_arcsec)

 distfromcenter_arcsec[0]*=-1.0
 distfromcenter_arcsec[1]*=-1.0

 #print(distfromcenter_arcsec[0])
 #exit()

 rmax=0.9 #in units of arc-seconds
 extrange=[rmax,-1*rmax,-1*rmax,rmax]

 #extent goes 'left right bottom top'
 pixelscale=0.01615
 fullext_image=pixelscale*(jband.shape)[0]/2.0

 #axes.imshow(imagecomb,origin='lower',extent=distfromcenter_arcsec)
 #print(extrange)
 #exit()
 interpval='hanning'
 axes.imshow(imagecomb,origin='lower',extent=[fullext_image,-1*fullext_image,-1*fullext_image,fullext_image],interpolation=interpval)

 axes.set_xlim(rmax,-1*rmax)
 axes.set_ylim(-1*rmax,rmax)
 #axes.set_xlim(distfromcenter_arcsec[0],-1*distfromcenter_arcsec[0])
 #axes.set_ylim(distfromcenter_arcsec[1],-1*distfromcenter_arcsec[1])
 axes.tick_params(which='both',direction='out',labelsize=14)
 axes.tick_params(which='major',length=10,width=1.5)
 axes.tick_params(which='minor',length=5,width=1.5)
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

 axes.set_xlabel('$\Delta RA(^{\prime\prime})$',fontsize=16)
 axes.set_ylabel('$\Delta DEC(^{\prime\prime})$',fontsize=16)
 #axes.set_title('HIP 99770 b (JHK Composite Image)',fontsize=18,pad=25)

 axes.scatter(0,0,marker='*',c='yellow',edgecolor='black',s=500)
 axes.text(0.95*rmax,0.75*rmax,'Exoplanet HIP 99770 b\nSCExAO/CHARIS\nJHK Composite Image',fontsize=18,color='w')

 #axes.imshow(imagecomb,origin='lower',interpolation='hanning')

 plt.show()

def datacube():

 directory='./files/'
 data_cube=(fits.open(directory+'asdicomb_indiv.fits'))[0].data

 print(data_cube.shape)

def ex1_5():
 fig, ax = plt.subplots()


 directory='./files/'
 x = np.linspace(0, 2 * np.pi, 120)
 y = (np.linspace(0, 2 * np.pi, 100))[:,None]
 #y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1) #this also works ... basically, though, we need to create a 2D array from the combination of x and y either way

 # ims is a list of lists, each row is a list of artists to draw in the
 # current frame; here we are just animating one artist, the image, in
 # each frame
 ims = []
 for i in range(60):
     x += np.pi / 45 #15
     y += np.pi / 30
     im = ax.imshow(f(x, y), animated=True,cmap='magma',origin='lower')
     if i == 0:
         ax.imshow(f(x, y),cmap='magma',origin='lower')  # show an initial one first
     ims.append([im])

 ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                 repeat_delay=1000)

 # To save the animation, use e.g.
 #
 # writer = animation.FFMpegWriter(fps=10,bitrate=1800)
 # ani.save("movie.mp4", writer=writer)

 #for a gif

 writergif = animation.PillowWriter(fps=10)
 ani.save(directory+'ex1_5.gif',writer=writergif)

 plt.show() #displays a quick-look animation, often useful

def ex1_6():

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

 #wvlhlabel=axes.text(0.95*rmax,-0.85*rmax,'Wavelength Slice {0:d}'.format(0+1),fontsize=14)
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
 #ani.save(directory+'ex1_6.gif',writer=writergif)
 mywriter=animation.FFMpegWriter(fps=5,extra_args=['-vcodec', 'libx264'])
 ani.save(directory+'ex1_6v2.mp4',writer=mywriter)

 plt.show()

#now on to coordinates

def ex2_4():

 c1 = SkyCoord('00h42m30s', '+41d12m00s', frame='icrs')
 c2 = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')

 print(c1)
 print(c2)

 c = SkyCoord(ra=[10, 11, 12, 13]*u.degree, dec=[41, -5, 42, 0]*u.degree)

 print(c)
#<SkyCoord (ICRS): (ra, dec) in deg
#    [(10., 41.), (11., -5.), (12., 42.), (13.,  0.)]>

 print(c[1])
#<SkyCoord (ICRS): (ra, dec) in deg
#    (11., -5.)>

 print(c.reshape(2, 2))
#<SkyCoord (ICRS): (ra, dec) in deg
#    [[(10., 41.), (11., -5.)],
#     [(12., 42.), (13.,  0.)]]>

 print(np.roll(c, 1))
#<SkyCoord (ICRS): (ra, dec) in deg
#    [(13.,  0.), (10., 41.), (11., -5.), (12., 42.)]>

 c = SkyCoord(ra=10.68458*u.degree, dec=41.26917*u.degree)

 print(c.to_string('decimal'))
 #'10.6846 41.2692'
 print(c.to_string('dms'))
 #'10d41m04.488s 41d16m09.012s'

 print(c.to_string('hmsdms'))
 #00h42m44.2992s +41d16m09.012s

 c_icrs = SkyCoord(ra=10.68458*u.degree, dec=41.26917*u.degree, frame='icrs')
 print(c_icrs.galactic  )
#<SkyCoord (Galactic): (l, b) in deg
#   (121.17424181, -21.57288557)>

 from astropy.coordinates import FK5
 c_fk5 = c_icrs.transform_to('fk5')
 #<SkyCoord (FK5: equinox=J2000.000): (ra, dec) in deg
#    (10.68459154, 41.26917146)>

 c_fk5.transform_to(FK5(equinox='J1975')) 
 print(c_fk5)
#<SkyCoord (FK5: equinox=J1975.000): (ra, dec) in deg
#    (10.34209135, 41.13232112)>

def ex2_5():

 c = SkyCoord(x=1, y=2, z=3, unit='kpc', representation_type='cartesian')
 print(c.x, c.y, c.z )
 #(<Quantity 1. kpc>, <Quantity 2. kpc>, <Quantity 3. kpc>)
 
 c.representation_type = 'cylindrical'
 print(c)
 #<SkyCoord (ICRS): (rho, phi, z) in (kpc, deg, kpc)
 #   (2.23606798, 63.43494882, 3.)>
 
 c = SkyCoord(ra=10.68458*u.degree, dec=41.26917*u.degree, distance=770*u.kpc)
 
 print(c.cartesian.x  )
 #<Quantity 568.71286542 kpc>
 
 print(c.cartesian.y)
 #<Quantity 107.3008974 kpc>
 
 print(c.cartesian.z  )
 #<Quantity 507.88994292 kpc>
 
 
def ex2_6(): 
 c1 = SkyCoord(ra=10*u.degree, dec=9*u.degree, distance=10*u.pc, frame='icrs')
 c2 = SkyCoord(ra=11*u.degree, dec=10*u.degree, distance=11.5*u.pc, frame='icrs')

 angsep=c1.separation_3d(c2) 
 print('angsep 1 ',angsep)

 c1 = SkyCoord(ra=10*u.degree, dec=9*u.degree, frame='icrs')
 c2 = SkyCoord(ra=11*u.degree, dec=10*u.degree, frame='fk5')

 sep=c1.separation(c2)  # Differing frames handled correctly  
 print('sep 2 ',sep.deg)
#<Angle 1.40453359 deg>


