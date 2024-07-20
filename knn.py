import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, MiniBatchKMeans
from yellowbrick.cluster import KElbowVisualizer

# Load the dataset
dataset = pd.read_csv("uber_data.csv")

# Display the shape and the first few rows of the dataset
print("Dataset Shape:", dataset.shape)
print("First few rows of the dataset:\n", dataset.head())

# Display distinct values in the 'Base' column
distinct_values = dataset['Base'].unique()
print("Distinct values in column:", distinct_values)

# Extract relevant features for clustering
clus = dataset[['Lat', 'Lon']]

# Display data types of the selected columns
print("Data types of 'Lat' and 'Lon' columns:\n", clus.dtypes)

# Standardize the features
scaler = StandardScaler()
features_std = scaler.fit_transform(clus)
print("Standardized features:\n", features_std)

# Use the Elbow Method to find the optimal number of clusters (K)
model = KMeans()
visualizer = KElbowVisualizer(model, k=(2, 10))  # Adjust the range of K as needed
visualizer.fit(features_std)
optimal_k = visualizer.elbow_value_

# # Display the Elbow Method plot
# visualizer.show()
print("Optimal number of clusters (K):", optimal_k)

# Fit MiniBatchKMeans for faster training with large datasets
kmeans = MiniBatchKMeans(n_clusters=optimal_k, max_iter=300, random_state=2)
kmeans.fit(clus)

# Get cluster centroids
centroids = kmeans.cluster_centers_
print("Cluster centroids:\n", centroids)

# Fit KMeans for labels and predictions
# kmeans = KMeans(n_clusters=optimal_k, random_state=42)  # Commented out since MiniBatchKMeans is used
labels = kmeans.fit_predict(clus)

# Specify the cluster index for analysis
cluster_index = 3

# Extract elements in the specified cluster
elements_in_cluster = clus[labels == cluster_index]
print("Elements in Cluster {}:\n{}".format(cluster_index, elements_in_cluster))

def location_check(A,B):
    new_location = np.array([[A, B]])
    predicted_cluster = kmeans.predict(scaler.transform(new_location))
    if predicted_cluster==0:
        return 'B02512'
    elif predicted_cluster==1:
        return  'B02598'
    elif predicted_cluster==2:
        return  'B02617'
    elif predicted_cluster==3:
        return  'B02682'
    else:
        return  'B02764'
    
# Make predictions for a new location
new_location = np.array([[40.6556, -73.5631]])
print(location_check(40.6556,-73.5631))
# predicted_cluster = kmeans.predict(scaler.transform(new_location))
# print("Predicted Cluster for New Location:", predicted_cluster[0])

# # Visualize the clusters and centroids
# plt.scatter(clus['Lat'], clus['Lon'], c=labels, cmap='viridis', s=50)
# plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200, label='Centroids')
# plt.scatter(new_location[:, 0], new_location[:, 1], marker='o', color='blue', label=f'Predicted Cluster {predicted_cluster[0]}')
# plt.legend()
# plt.title('Uber Data Clustering')
# plt.xlabel('Latitude')
# plt.ylabel('Longitude')
# plt.show()
