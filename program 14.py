import numpy as np
from scipy.stats import skew, kurtosis
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def tail_proportion(data, percentile=95):
    threshold = np.percentile(data, percentile)
    return np.mean(data > threshold)

def compute_asymmetry_score(data, weights=(1, 1, 1), tail_percentile=95):
    skewness = skew(data)
    kurt = kurtosis(data)
    tail_prop = tail_proportion(data, percentile=tail_percentile)
    asymmetry_score = (weights[0] * skewness) + (weights[1] * kurt) + (weights[2] * tail_prop)
    return asymmetry_score

np.random.seed(0)
gene_expression_data = np.random.lognormal(mean=0, sigma=1, size=1000)

asymmetry_score = compute_asymmetry_score(gene_expression_data)
print("Asymmetry Score:", asymmetry_score)

transformed_data = np.log(gene_expression_data)

kmeans_original = KMeans(n_clusters=2, random_state=0).fit(gene_expression_data.reshape(-1, 1))

kmeans_transformed = KMeans(n_clusters=2, random_state=0).fit(transformed_data.reshape(-1, 1))

print("Original Clusters Centers:", kmeans_original.cluster_centers_)
print("Transformed Clusters Centers:", kmeans_transformed.cluster_centers_)
