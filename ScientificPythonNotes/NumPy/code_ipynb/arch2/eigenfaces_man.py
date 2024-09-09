import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_lfw_people

def run(numpca=150):

 faces = fetch_lfw_people(min_faces_per_person=60)
 print(faces.target_names)
 print(faces.images.shape)

 from sklearn.decomposition import PCA #as RandomizedPCA
 skpca = PCA(numpca)
 skpca.fit(faces.data)

 #manual PCA

 faces_mean=faces.data-np.mean(faces.data,axis=0)

 #cov=np.cov(faces_mean,rowvar=False)
 cov=np.matmul(faces_mean.T,faces_mean)

 eig_val,eig_vec=np.linalg.eigh(cov)
 
 indices=np.argsort(eig_val)[::-1]
 eig_val=eig_val[indices]
 eig_vec=eig_vec[:,indices]

 n_comp=numpca
 eig_vec=eig_vec[:,:n_comp]
 eig_val=eig_val[:n_comp]

 #pca_comp=eig_vec.T
 #print(eig_vec.shape)
 #exit()

 #print(pca.components_.shape)

 #print(pca.components_[0:5,0:5])
 #exit()

 pca_components=((faces_mean).dot(eig_vec))

 fig, axes = plt.subplots(3, 8, figsize=(9, 4),
                          subplot_kw={'xticks':[], 'yticks':[]},
                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i, ax in enumerate(axes.flat):
#     ax.imshow(pca_comp[i].reshape(62, 47), cmap='bone')

     ax.imshow(eig_vec[:,i].reshape(62,47),cmap='bone')
     #ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')
 

 plt.show()
 plt.plot(np.cumsum(skpca.explained_variance_ratio_))
 plt.xlabel('number of components')
 plt.ylabel('cumulative explained variance');
 plt.show()
 
 
 
 # Compute the components and projected faces
 #pca = RandomizedPCA(numpca).fit(faces.data)
 #components = pca.transform(faces.data)
 #projected = pca.inverse_transform(components)
 
 pca_inverse_transform=pca_components.dot(eig_vec.T)+np.mean(faces.data,axis=0)
 #print(pca_inverse_transform.shape)
 #exit() 
 # Plot the results
 fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
                        subplot_kw={'xticks':[], 'yticks':[]},
                        gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i in range(10):
     ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
     ax[1, i].imshow(pca_inverse_transform[i].reshape(62, 47), cmap='binary_r')
     #ax[1, i].imshow(projected[i].reshape(62, 47), cmap='binary_r')
     
 ax[0, 0].set_ylabel('full-dim\ninput')
 ax[1, 0].set_ylabel(str(numpca)+'-dim\nreconstruction');

 plt.show()
