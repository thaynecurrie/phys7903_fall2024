import numpy as np
from scipy import stats

from astropy.io import ascii

import matplotlib.pyplot as plt

def create_file():

 

 a=ascii.read('aw.txt')

 name=np.char.strip(a['Name'])
 SED=np.array(a['SED'])
 lmass=np.array(a['l_Mass'])
 mass=np.array(a['Mass'])
 mass=np.where(lmass == '<',-999,mass)
 SpType=np.array(a['SpType'])
 
 good=np.where(lmass != '<')

 print(mass)

 af=np.arange(len(mass))
 print(af)

 f=open('diskmasses.txt','w')
 
 for i in range(len(mass)):
  if (mass[i] > -1):
   f.write("%s %s %s %f\n" % (name[i].replace(" ",""),SpType[i],SED[i],np.log10(mass[i])))
 f.close()
 #np.savetxt('diskmasses.txt',np.array((name,SpType,SED,mass)).T,fmt="%s %s %s %.4f",delimiter=",")
 #np.savetxt('diskmasses.txt',np.column_stack((name,SpType,SED,mass)),fmt="%s" "" "%s" "" "%s" "" "%.4f",delimiter=",")
 #np.savetxt('diskmasses.txt',np.column_stack((name,SpType,SED,mass)),fmt="%s" " " "%s" " " "%s" "%.2f")
# np.savetxt('diskmasses.txt',np.column_stack((name,SpType,af)),fmt="%s" "%s" "%.2f")
 #np.savetxt('diskmasses.txt',mass)
 
 

def get_stats():

 dtypes={'names':('name','SpType','SED','mass'),'formats':(np.unicode_,np.unicode_,np.unicode_,np.float64)}
 a=np.loadtxt('diskmasses.txt',dtype=dtypes)
 
# name=a[:,0]
# SpType=a[:,1]
# SED=a[:,2]
#mass=a[:,3]

 name=a['name']
 SpType=a['SpType']
 SED=a['SED']
 mass=(a['mass'])

 plt.hist(mass)
 plt.show()

 print(np.median(mass)) 

 print(np.var(mass))

 print(np.nanpercentile(mass,25))

