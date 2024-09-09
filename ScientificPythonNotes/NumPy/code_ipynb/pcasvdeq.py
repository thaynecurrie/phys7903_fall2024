import numpy as np

def run():


 #create a random matrix

 #a=np.random.rand(27,13)
 a=np.random.rand(7,3)

#mean-subtract
 am=a-np.mean(a,axis=0)

#A. do SVD

 U,S,Vt=np.linalg.svd(am)


#B. do PCA w/ eigenstuff

 cov=np.matmul(am.T,am)
 eig_val,eig_vec=np.linalg.eigh(cov) 

 indices=np.argsort(eig_val)[::-1]

 eig_val=eig_val[indices]
 eig_vec=eig_vec[:,indices]

 print("eig_vec")
 print(eig_vec)
 print(" ")
 print("VT")
 print(Vt.T)

 print("differences")
 print(eig_vec-Vt.T)

 print(" second vers")

 print(eig_vec.T)
 print(" ")
 print(Vt)


 print('S squared are ',S**2)
 print('eig_vals are ',eig_val)
