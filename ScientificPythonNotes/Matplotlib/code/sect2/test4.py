import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,AutoMinorLocator


def run():


 CO2concentration=np.array([289,288,291,295,294,298,297,299,310,317,325,338,354,370,390.1,401,420]) #roughly estimated from NOAA

 CO2years=np.array([1700,1750,1800,1850,1875,1900,1925,1950,1960,1970,1980,1990,2000,2005,2010,2015,2020])

 sval=0.25 #add some noise
 pirate_attacks=5000*np.exp(-1*(CO2years-CO2years[0])/150)*(1+sval*0.25*np.random.randn(len(CO2years)))

 fig,axes=plt.subplots(figsize=(9,9))

 #now fit an exponential to the pirate attacks

 piratefit=np.polyfit(CO2years,np.log(pirate_attacks),1)

 atest=np.exp(piratefit[1])
 btest=piratefit[0]
 #print(atest,btest,result[1])
 #exit()

 axes.scatter(CO2years,CO2concentration,marker='o',s=250,color='darkblue',edgecolor='black',alpha=0.9,label='CO2')
 axes.set_xlabel('Year',fontsize=14)
 axes.set_ylabel(r'CO$_{\rm 2}$ Concentration (PPM)',fontsize=16,color='darkblue')

 axes.set_ylim(275,425)

 axes.tick_params(which='both',width=1.5,direction='in',labelsize=14)

 axes.tick_params(which='major',length=7,width=3)
 axes.tick_params(which='minor',length=3.5,width=1.5)

#this makes the labels appear at top and bottom
 axes.tick_params(labeltop=False,labelbottom=True,bottom=True,top=True,labelright=True)
 axes.xaxis.set_ticks_position('both')
 axes.xaxis.set_minor_locator(AutoMinorLocator(5))
 

 axes.yaxis.set_ticks_position('both')
 axes.yaxis.set_minor_locator(AutoMinorLocator(5))

 

 for axl in ['top','bottom','left','right']:
   axes.spines[axl].set_linewidth(2)

 #duh=3
 #if duh < 10: 

 axes2=axes.twinx()
 axes2.tick_params(which='both',direction='in',labelsize=14)
 axes2.set_ylim(0,5100)

 axes2.scatter(CO2years,pirate_attacks,marker='s',s=150,color='tab:green',edgecolor='black',alpha=0.9)

 axes2.plot(CO2years,atest*np.exp(btest*CO2years),ls='-',label='Exponential Fit to Pirate Attacks/Year',color='tab:green',)
 axes2.set_ylabel(r'Pirate Attacks Per Year (Source: The Pirate News Network)',fontsize=14,color='darkgreen',alpha=0.9)

 axes2.legend(loc=[0.25,0.9],fontsize='large',markerscale=0.85)


 axes2.tick_params(which='both',width=1.5,direction='in',labelsize=14)

 axes2.tick_params(which='major',length=7,width=3)
 axes2.tick_params(which='minor',length=3.5,width=1.5)
 axes2.xaxis.set_ticks_position('both')
 axes2.xaxis.set_minor_locator(AutoMinorLocator(5))

 axes2.yaxis.set_ticks_position('right')
 axes2.yaxis.set_minor_locator(AutoMinorLocator(5))

 axes2.tick_params(labeltop=True)
 #axes2.tick_params(which='both',width=1.5,direction='in',labelsize='large')
 #axes2.tick_params(which='major',length=7,width=3)
 #axes2.tick_params(which='minor',length=3.5,width=1.5)
 #axes2.xaxis.set_minor_locator(AutoMinorLocator(5))
 #axes.scatter(CO2years,pirate_attacks,marker='o',c='tab:green',s=50)
 #fig.tight_layout() #note: see what this does
 plt.show()

