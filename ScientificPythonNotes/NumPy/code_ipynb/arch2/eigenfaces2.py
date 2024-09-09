import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_lfw_people
from sklearn.utils.extmath import svd_flip

#this time, do the PCA from scratch

def run(numpca=150):

 faces = fetch_lfw_people(min_faces_per_person=60)
 print(faces.target_names)
 print(faces.data.shape)
 from sklearn.decomposition import PCA as RandomizedPCA

#Step 1
 faces_mean=faces.data-np.mean(faces.data,axis=0)


# U,S,Vt=np.linalg.svd(faces_mean,full_matrices=False)
#,full_matrices=False)

#Step 2

# cov=np.matmul(faces_mean.T,faces_mean)
# print(faces.data.shape)
 #print(cov.shape)
 cov=np.cov(faces_mean,rowvar=False)

#Step 3
 eig_val,eig_vec=np.linalg.eigh(cov)

#Step 4

 indices=np.argsort(eig_val)[::-1]
 eig_val=eig_val[indices]
 eig_vec=eig_vec[:,indices]


 #print(eig_vec)
# print(eig_vec.shape)
# print(eig_vec[0:5,0:5])

#Step 5a
 
 n_comp=numpca
 eig_vec=eig_vec[:,:n_comp]
 eig_val=eig_val[:n_comp]

 pca_components=((faces_mean).dot(eig_vec))
 #pca_components=((faces_mean.T).dot(eig_vec)).T

 print('eig vec.shape',eig_vec.shape) 
 print(pca_components.shape)

 print(eig_vec.T[0:5,0:5])
 print(" ")
 print(pca_components[0:5,0:5])
 exit()

 
# pca = RandomizedPCA(numpca)
#pca.fit(faces.data)
 
# print(pca.components_.shape)
 fig, axes = plt.subplots(3, 8, figsize=(9, 4),
                          subplot_kw={'xticks':[], 'yticks':[]},
                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i, ax in enumerate(axes.flat):
     ax.imshow(pca_components[i,:].reshape(62, 47), cmap='bone')
     #ax.imshow(pca_components_[i].reshape(62, 47), cmap='bone')
     #ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')
 

 plt.show()
 
# plt.plot(np.cumsum(pca.explained_variance_ratio_))
# plt.xlabel('number of components')
# plt.ylabel('cumulative explained variance');
# plt.show()
 
 
 
 # Compute the components and projected faces
 pca = RandomizedPCA(numpca).fit(faces.data)
 pca.shape
 components = pca.transform(faces.data)
 projected = pca.inverse_transform(components)
 
 # Plot the results
 fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
                        subplot_kw={'xticks':[], 'yticks':[]},
                        gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i in range(10):
     ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
     ax[1, i].imshow(projected[i].reshape(62, 47), cmap='binary_r')
     
 ax[0, 0].set_ylabel('full-dim\ninput')
 ax[1, 0].set_ylabel(str(numpca)+'-dim\nreconstruction');

 plt.show()
