import matplotlib.pyplot as plt
import numpy as np

from scipy import interpolate
from mpl_toolkits.axes_grid.inset_locator import inset_axes
from matplotlib.ticker import AutoMinorLocator

file_in='./files/broadband_contrast.txt'

dstar=40 #assume a distance of 40 pc
dtypes={'names':('angsep','contrast'), 'formats':(np.float64,np.float64)}

a = np.loadtxt(file_in,usecols=range(2),dtype=dtypes)
#a=np.loadtxt(file_in)

ang_sep=a['angsep']
contrast_5sig=a['contrast']

nhour=2
scalefact=(nhour*3600/1800.)**(0.5)

fscexao=interpolate.interp1d(ang_sep,contrast_5sig/scalefact)

ang_sep_new=np.arange(0.15,0.9,0.05)
contrast_5sig_twohours=fscexao(ang_sep_new)


#approximate performance for Keck/NIRC2

ang_sep_keck=np.array([0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
contrast_keck=np.array([1e-2,1e-3,3e-4,1e-4,3e-5,1.5e-5,1.25e-5,1e-5,8e-6])

fkeck=interpolate.interp1d(ang_sep_keck,contrast_keck)
#print(fkeck)
#exit()
contrast_5sig_keck=fkeck(ang_sep_new)
#estimate for new performance, SCExAO

improve_fact=4
contrast_5sig_twohours_new=contrast_5sig_twohours/improve_fact
igood=np.where(ang_sep_new < 0.25)
contrast_5sig_twohours_new[igood]/=(3-ang_sep_new[igood]*8.)
ibad=np.where(ang_sep_new > 0.7)
contrast_5sig_twohours_new[ibad]*=(1+1.75*ang_sep_new[ibad]-.7)

print(ang_sep)

fig,axes=plt.subplots(figsize=(9,5))
axes.plot(ang_sep_new,contrast_5sig_keck,linewidth=4,markersize=np.sqrt(50),color='tab:blue',label='Keck/NIRC2')
axes.plot(ang_sep_new,contrast_5sig_twohours,linewidth=5,color='magenta',label='SCExAO/CHARIS (Early 2023 Performance)')
axes.plot(ang_sep_new,contrast_5sig_twohours_new,linewidth=4,ls='-.',color='tab:green',label='SCExAO/CHARIS (2024 Performance, predicted)')

axes.set_yscale('log')
axes.set_ylim(5e-8,2e-3)
axes.set_xlim(0.1,1.01)

#note:setting to 'both' instead of 'bottom' would draw tick marks at top of plot:
  #would mismatch with secondary axis tick marks
axes.xaxis.set_ticks_position('bottom')

axes.tick_params(labeltop=False,labelbottom=True,labelright=False,labelleft=True)
axes.tick_params(which='both',direction='in',labelsize=14)
axes.tick_params(which='major',length=10,width=1.5)
axes.tick_params(which='minor',length=5,width=1.5)
axes.xaxis.set_minor_locator(AutoMinorLocator(5))
#log scale automatically sets minor tick marks to be reasonable here
axes.yaxis.set_ticks_position('both')

axes.set_ylabel(r'5$\sigma$ Contrast (Bright Mid-A Star)',fontsize=16)
axes.set_xlabel('Angular Separation(\u2033)',fontsize=16)
axes.set_title('SCExAO Contrast Plot With An Inset and Zoom-In',fontsize=18)

###IMPORTANTLINES

#secondaxis=inset_axes(axes,width=1.3,height=0.9,[0.5,0.6])
secondaxis=axes.inset_axes([0.625, 0.65, 0.33, 0.25])
#,width=1.3,height=0.9)
#left,bottom,width,height=[0.5,0.6,0.33,0.25]
#secondaxis=fig.add_axes([left,bottom,width,height])
#secondaxis=axes.secondary_xaxis('top',functions=(lambda x: dstar*x, lambda x: x/dstar))

secondaxis.plot(ang_sep_new,contrast_5sig_twohours,linewidth=5,color='magenta')
secondaxis.plot(ang_sep_new,contrast_5sig_twohours_new,ls='-.',linewidth=5,color='tab:green')
secondaxis.set_ylabel(r'5$\sigma$ Contrast (Bright Mid-A Star)',fontsize=7)
secondaxis.set_xlabel('Angular Separation(\u2033)',fontsize=7)
secondaxis.set_xlim(0.15,0.4)
secondaxis.set_ylim(5e-7,1e-4)
#secondaxis.set_ylim(5e-8,2e-3)
secondaxis.tick_params(which='both',direction='in',labelsize=8)
secondaxis.tick_params(which='major',length=10,width=1.5)
secondaxis.tick_params(which='minor',length=5,width=1.5)
secondaxis.xaxis.set_minor_locator(AutoMinorLocator(5))
#secondaxis.yaxis.set_minor_locator(AutoMinorLocator(5))
secondaxis.set_yscale('log')

secondary_axis2=secondaxis.secondary_xaxis('top',functions=(lambda x: dstar*x, lambda x: x/dstar))
secondary_axis2.set_xlabel('Projected Separation (au) for d = 40 pc',fontsize=7)
secondary_axis2.tick_params(which='both',direction='in',labelsize=7)
secondary_axis2.tick_params(which='major',length=10,width=1.5)
secondary_axis2.tick_params(which='minor',length=5,width=1.5)
secondary_axis2.xaxis.set_minor_locator(AutoMinorLocator(5))


axes.indicate_inset_zoom(secondaxis)

#thicken the spines
for axl in ['top','bottom','left','right']:
  axes.spines[axl].set_linewidth(2)

#movethe legend location b/c otherwise it clashes with the inset
#axes.legend(loc=[0.4,0.75])
axes.legend(loc=[0.025,0.05],fontsize=8)

plt.show()

