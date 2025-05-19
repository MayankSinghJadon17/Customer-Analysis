import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def plot_elbow_curve(data, max_k=10):
            inertias = []
            for k in range(1, max_k + 1):
                model = KMeans(n_clusters=k, random_state=42)
                model.fit(data)
                inertias.append(model.inertia_)

            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(range(1, max_k + 1), inertias, marker='o')
            ax.set_title('Elbow Method For Optimal k')
            ax.set_xlabel('Number of clusters (k)')
            ax.set_ylabel('Inertia')
            ax.grid(True)
            st.pyplot(fig)

def show():
    st.markdown("<h1 style='text-align: center;'>📌 Customer Clustering</h1>", unsafe_allow_html=True)
    st.write("Configure clustering parameters and view customer segments.")

    # Load and preview data
    if "df_original" not in st.session_state:
        st.session_state.df_original = pd.read_csv(r"C:\Users\mayan\Downloads\df_encoded (1).csv")

    df = st.session_state.df_original.copy()
    st.subheader("📂 Input Data")
    st.dataframe(df.head())


    if "df_numeric" not in st.session_state:
        st.session_state.df_numeric = st.session_state.df_original.select_dtypes(include='number')


    st.subheader("📊 Elbow Curve for Optimal k")

    if st.button("Show Elbow Curve"):
        elbow_data = st.session_state.df_numeric
        plot_elbow_curve(elbow_data, max_k=10)

    # Select features to use
    st.subheader("🧮 Clustering Parameters")
    all_columns = df.columns[0:]  # Adjust index if first column is not usable

    select_all_option = "Select All"

    # Show multiselect with "Select All" on top
    selected_features = st.multiselect(
        "Select features for clustering",
        options=[select_all_option] + list(all_columns)
    )

    # Handle logic for Select All
    if select_all_option in selected_features:
        selected_features = list(all_columns)
        num_clusters = st.slider("Number of clusters", min_value=2, max_value=10, value=3)

    if st.button("Run Clustering"):
        st.success(f"Clustering with {num_clusters} clusters using features: {selected_features}")

        # Preprocess
        X = df[selected_features]

        # KMeans
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        df["Cluster"] = kmeans.fit_predict(X)

        st.session_state.clustered_df = df

        # Visualization (PCA to 2D)
        pca = PCA(n_components=2)
        components = pca.fit_transform(X)
        df["PC1"] = components[:, 0]
        df["PC2"] = components[:, 1]

        st.subheader("📌 Cluster Visualization")
        fig = px.scatter(df, x="PC1", y="PC2", color="Cluster")
        st.plotly_chart(fig)

        # Show full clustered data
        st.subheader("📋 Clustered Data")
        st.dataframe(df)

    if st.button("Generate Profiles"):
            
            if "clustered_df" not in st.session_state:
                st.error("Please run clustering first to generate cluster profiles.")
            else:
                df = st.session_state.clustered_df


            def generate_cluster_profiles(df, cluster_col='Cluster', top_n_features=7):
                profiles = []
                exclude_cols = [cluster_col, "PC1", "PC2"]
                numeric_cols = df.select_dtypes(include='number').columns.difference(exclude_cols)
                cluster_means = df.groupby(cluster_col)[numeric_cols].mean()
                global_mean = df[numeric_cols].mean()

                for cluster_id in cluster_means.index:
                    profile = f"### Cluster {cluster_id} Profile\n"
                    profile += f"Number of customers: {len(df[df[cluster_col]==cluster_id])}\n\n"

                    mean_diff = (cluster_means.loc[cluster_id] - global_mean).abs().sort_values(ascending=False)
                    top_features = mean_diff.head(top_n_features).index

                    for feature in top_features:
                        cluster_value = cluster_means.loc[cluster_id][feature]
                        global_value = global_mean[feature]

                        direction = "higher" if cluster_value > global_value else "lower"
                        profile += f"- **{feature}** is **{direction}** than average (Cluster: {cluster_value:.2f}, Overall: {global_value:.2f})\n"

                    profiles.append(profile)

                return profiles
            profiles = generate_cluster_profiles(df , cluster_col='Cluster')
            for p in profiles:
                st.markdown(p)
    st.subheader("📈 Cluster Assessment")

    if "clustered_df" in st.session_state:
        df = st.session_state.clustered_df
        numeric_cols = df.select_dtypes(include='number').columns.difference(["PC1", "PC2"])

        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("X-axis column", numeric_cols)
        with col2:
            y_axis = st.selectbox("Y-axis column", numeric_cols, index=1)

        point_size = st.slider("Scatter plot point size", 5, 20, 10)

        if st.button("Assess Clustering"):
            st.markdown("### 🔍 Scatter Plot by Cluster")
            fig1 = px.scatter(
                df,
                x=x_axis,
                y=y_axis,
                color="Cluster",
                title=f"Clusters: {x_axis} vs {y_axis}",
                opacity=0.8,
                size_max=point_size
            )
            st.plotly_chart(fig1)

            st.markdown("### 📊 Count Plot by Cluster")
            fig2 = px.histogram(
                df,
                x="Cluster",
                color="Cluster",
                barmode="group",
                title="Count of Data Points per Cluster"
            )
            st.plotly_chart(fig2)
    else:
        st.info("Please run clustering first to assess clusters.")

        