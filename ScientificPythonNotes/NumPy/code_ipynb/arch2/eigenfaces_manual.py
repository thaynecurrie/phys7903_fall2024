#### A from-scratch demonstration of the eigenfaces application of PCA
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


#Step 1
 faces_mean=faces.data-np.mean(faces.data,axis=0)

#Step 2
 cov=np.matmul(faces_mean.T,faces_mean)

#Step 3
 eig_val,eig_vec=np.linalg.eigh(cov)

#Step 4 
 indices=np.argsort(eig_val)[::-1]
 eig_val=eig_val[indices]
 eig_vec=eig_vec[:,indices]

#Step 5
 n_comp=numpca
 eig_vec=eig_vec[:,:n_comp]
 eig_val=eig_val[:n_comp]

 pca_components=((faces_mean).dot(eig_vec))  


### Plotting the Eigenvectors
 fig, axes = plt.subplots(3, 8, figsize=(9, 4),
                          subplot_kw={'xticks':[], 'yticks':[]},
                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i, ax in enumerate(axes.flat):
     ax.imshow(eig_vec[:,i].reshape(62,47),cmap='bone')
 

 plt.show()


####Computing the Cumulative Variance of each eigenvector/PC
# plt.plot(np.cumsum(skpca.explained_variance_ratio_))
# plt.xlabel('number of components')
# plt.ylabel('cumulative explained variance');
# plt.show()
 
 
 
 # Compute the components and projected faces
 #pca = RandomizedPCA(numpca).fit(faces.data)
 #components = pca.transform(faces.data)
 #projected = pca.inverse_transform(components)


#Step 6 
 pca_inverse_transform=pca_components.dot(eig_vec.T)+np.mean(faces.data,axis=0)


#### Plotting the Real Images and PC-Projected Images
 fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
                        subplot_kw={'xticks':[], 'yticks':[]},
                        gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i in range(10):
     ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
     ax[1, i].imshow(pca_inverse_transform[i].reshape(62, 47), cmap='binary_r')
     
 ax[0, 0].set_ylabel('full-dim\ninput')
 ax[1, 0].set_ylabel(str(numpca)+'-dim\nreconstruction');

 plt.show()
