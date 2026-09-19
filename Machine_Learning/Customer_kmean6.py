import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():
    # Load the dataset
    csv = "Mall_Customers.csv"
    df = pd.read_csv(csv)
    print("Dataset loaded successfully!")
    print(df.head())
    print("Missing values")
    print(df.isnull().sum())

    # Step 2 :Feature selection
    X = df[["AnnualIncome","SpendingScore"]]
    print("Selected features:")
    print(X.head())

    # Step 3 : Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Scaled features:")
    print(X_scaled[:5])

    # Step 4 : Elbow Method to find optimal number of clusters
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)
    print("WCSS values for different number of clusters:")
    for i in range(len(wcss)):
        print(f"Number of clusters: {i+1}, WCSS: {wcss[i]}")

    # Step 5 : Plotting the Elbow Method graph
    plt.plot(range(1, 11), wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.show()

    # Step 5 : model
    model = KMeans(n_clusters=4, n_init=10, random_state=42)
    clusters = model.fit_predict(X_scaled)
    df['Cluster'] = clusters
    print("Cluster assignments:")
    print(df.head(100))

if __name__ == "__main__":
    main()