import numpy as np
from sklearn.decomposition import PCA
import scipy as sp

def run():


 data=np.array([[7., 4., 3.],
               [4., 1., 8.],
               [6., 3., 5.],
               [8., 6., 1.],
               [8., 5., 7.],
               [7., 2., 9.],
               [5., 3., 3.],
               [9., 5., 8.],
               [7., 4., 5.],
               [8., 2., 2.]])
 data -= data.mean(axis=0)
 cov = np.cov(data, rowvar=False)
 print("cov shape",cov.shape)
 eig_val,eig_vec=np.linalg.eigh(cov)
 #eig_val,eig_vec=sp.linalg.eig(cov)

 num_components=2
 indices=np.argsort(eig_val)[::-1]
 #num_components=2
 #sorted_key = np.argsort(eig_val)[::-1][:num_components]
 #eig_val, eig_vec = eig_val[sorted_key], eig_vec[:, sorted_key]

 eig_val=eig_val[indices]
 eig_vec=eig_vec[:,indices]

 eig_vec=eig_vec[:,:num_components]
 eig_val=eig_val[:num_components]

 principal_components=np.dot(data,eig_vec)

 print("Principal Components:\n", principal_components)
 print(principal_components.shape)

def run2():

 # Create dataset
 data=np.array([[7., 4., 3.],
               [4., 1., 8.],
               [6., 3., 5.],
               [8., 6., 1.],
               [8., 5., 7.],
               [7., 2., 9.],
               [5., 3., 3.],
               [9., 5., 8.],
               [7., 4., 5.],
               [8., 2., 2.]])
 
# Create and fit PCA Model
 pca_model = PCA(n_components=2)
 components = pca_model.fit_transform(data)
 print(components)
 
 print(components.shape)

