"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
from sklearn.datasets import load_sample_image
import matplotlib as plt

# This function has three inputs and returns an np-array containing the recolored image:
# img: an np-array containing an image, from sklearn.datasets.load_sample_image()sor plt.imread().
# n_clusters: the number of clusters used for MiniBatchKMeans. The default value is 4.
# random_state: the random seed used for the MiniBatchKMeans. The default value is 5.
# The function returns a recolored image, where each pixel is assigned the value of its cluster..
def coloring(img, n_clusters=4, random_state=5):
    new_img_ = (img/255)
    new_img_ = new_img_.reshape(img.shape[0] * img.shape[1], 3)
    kmeans = MiniBatchKMeans(n_clusters=n_clusters,
                             random_state=random_state).fit(new_img_)
    new_color_ = kmeans.cluster_centers_[kmeans.predict(new_img_)]
    return (new_color_.reshape(img.shape))
