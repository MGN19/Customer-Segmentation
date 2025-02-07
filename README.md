# 🍔 **Customer Segmentation for Food Delivery Business** 🚴‍♂️

## 📋 **Project Overview**

This project aimed to analyze and segment customers for a food delivery business (ABCDEats Inc), leveraging advanced unsupervised machine learning techniques to derive meaningful insights. 
By grouping customers based on their behavior, demographics, and spending patterns, this will help the business to tailor their marketing strategies, improve customer satisfaction, and enhance service delivery.
Through various clustering algorithms, we created distinct customer segments that provided different business insights. 

Additionally, an interactive web app was developed, using Streamlit, as a visualization and interpretation tool for the project, allowing users to engage with the data and explore clustering results in a user-friendly manner.
Through various clustering algorithms, we created distinct customer segments that provide actionable business insights. 

This project was completed as part of the Data Mining course in my Master's degree program and is a collaborative group project.

<br>

---

## 🚀 **Key Features**

- **Data Exploration**: Identifying missing values, duplicates, inconsistencies, feature engineering and data patterns through the use of visualization. 

- **Data Preprocessing**: Handling missing values, removing outliers, and correlation between features.

- **Clustering Models**: A range of clustering algorithms, including K-Means, DBSCAN, GMM, and Self-Organizing Maps (SOM), applied to identify customer segments. Only for the customer segmentation a different model was applied (K-Prototypes).

- **Evaluation Metrics**: Assessing clustering performance using Silhouette Score, R², and Calinski-Harabasz Score.

- **Visualization**: Using UMAP for visualizing customer segments.

- **Business Applications**: Segment profiles to drive personalized marketing, product recommendations, and service improvements.

- **Web app development**: Creation of an app that allow users to interact with the data used in the project.

<br>

---

## 🧑‍💼 **Methodology**

### 1. **Data Exploration**
   - **Identification of duplicate values**: duplicated values were identified and removed from the dataset.
   
   - **Descriptive analysis**: Analysis of each feature based on summary statistics, such as mean/mode or standard deviation, for both numerical and caterogical variables. This was done to get a first overview of the data at hand.
   
   - **Incoherence Checking**: Identification and fixing of any incoeherence found, such as age of the customers.
   
   - **Missing Data analysis**: Checking missing values and correlation between them. For this, we first imputed the values using the median/mode, so visualizations could be done.
   
   - **Outlier identification**: Identification of outliers, to further be removed from the dataset in **Data Preprocessing**
   
   - **Feature Engineering**: Creation of new features and transformation on the ones that exist.
   
   - **Visualization**: Univariate, bivariate and multivariate data analysis.

### 1. **Data Preprocessing**
   - **Handling Missing Values**: Use of K-Nearest Neighbors (KNN) imputation for age.
   
   - **Outlier Treatment**: Based on data distribution, using boxplots, outliers were removed from the data set.
   
   - **Univariate Variable Removal**: Features with zero variance were removed (e.g., `HR_0`).
   
   - **Correlation between features**: Highly correlated features were identified and considered for dropping based on Spearman correlation.

### 2. **Clustering Models**
   - **Hierarchical Clustering**: Applied with various linkage and distance metrics, using dendrogram visualization for optimal clustering selection.
   
   - **K-Means Clustering**: Determined the optimal number of clusters using the Elbow Method and profiled each cluster.
   
   - **Density-Based Clustering (DBSCAN, HDBSCAN, MeanShift)**: Tuned hyperparameters for effective segmentation.
   
   - **Gaussian Mixture Model (GMM)**: Probabilistic approach for soft clustering with AIC/BIC evaluation.
   
   - **Self-Organizing Maps (SOM)**: Neural network-based clustering combined with K-Means to capture non-linear patterns.
   
   - **K-Prototype**: Mix of k-means and K-mode. USED ONLY FOR **CUSTOMER SEGMENTATION**.

### 3. **Segmentation Categories**
   - **Cuisine Segmentation**: Segmenting by the expenses of each customer in different cuisines. Applied all clustering models, except K-Prototypes.
   
   - **Customer Segmentation**: Grouping based on age, region, and repeat purchase behavior. Given the existence of a categorical feature (region of the purchase; cannot forget that binary features are also categorical), K-Prototypes was specifically used for clustering. The model evaluation was done exclusively using the Elbow Plot to determine the optimal number of clusters.
   
   - **Temporal Segmentation**: Composed by temporal-related data, such as times and days of the week at which purchases were made. Applied all clustering models, except K-Prototypes.
   
   - **Spending Segmentation**: All remaining information about purchases, such as total orders, the type of discount received and payment methods. Applied all clustering models, except K-Prototypes.
   
   - **Product Segmentation**: Composed by the total number of products the costumer has order, the number of distinct vendors they have purchased from, and the total number of orders placed with chain restaurants. Applied all clustering models, except K-Prototypes.

<br>

---

## 🏆 **Clustering Results**
After analyzing all the segments, the next step was to combine the clusters produced from each individual segmentation, resulting in a total of 330 non-zero clusters. Initially, we considered manually merging some of these clusters, but given the sheer volume, we opted against this approach. Instead, we leveraged the cluster centroids as input for a Hierarchical Clustering Algorithm in an effort to reduce the number of clusters. We applied the same optimization process as before, experimenting with different linkages, distance metrics, and the number of clusters. Ultimately, we determined that the optimal solution for our problem involved using Ward linkage with the Euclidean distance metric and 3 clusters.

This clustering strategy allowed us to define three distinct customer groups, each exhibiting unique behaviors:

- **Cluster 0 – Balanced Engagement Enthusiasts**: These customers demonstrate a balanced approach to spending, with moderate totals and average spending per product. Their order frequency is consistent, typically placing orders on weekdays. They have a varied preference for cuisines, with Italian and American being the most favored. Additionally, their activity peaks between 15:00–19:00.

- **Cluster 1 – Premium Early Birds**: This group is characterized by high spending, with both the highest total expenditure and significantly higher average spend per product. These customers are likely to order during the morning and lunch hours, showing a preference for high-value, premium items. Their favored cuisines include Asian and Street Food/Snacks, and they tend to spend more per cuisine, reflecting their focus on quality over quantity.

- **Cluster 2 – Cost-Conscious Shoppers**: Customers in this cluster are more cost-conscious, with lower total and average spending per product. However, they place a higher volume of orders, especially on weekends, resulting in a notable weekend-to-weekday order ratio. Their cuisine preferences are diverse, as they engage with a wider variety of cuisines compared to the other clusters. Additionally, they tend to place their orders primarily during morning and lunch hours (8:00–14:00).

These customer profiles helps to identify which segments are more likely to respond to targeted campaigns and personalized product recommendations.

<br>

---

## 💼 **Business Applications**

The results of this segmentation can be used to implement a range of business strategies, such as:

- **Cluster 0 – Balanced Engagement Enthusiasts**
• Offer loyalty rewards or exclusive deals to maintain their steady engagement.
• Design promotions for the afternoon (15–19h) to align with their activity patterns.
• Highlight Italian and American cuisine bundles or discounts to match their preferences.

- **Cluster 1 – Premium Early Birds**
• Focus on premium products and high-margin items in marketing campaigns.
• Create exclusive breakfast or lunch deals to capitalize on their morning/lunch time orders.
• Emphasize Asian and Street Food/Snacks cuisines in promotions, appealing to their preferences.

- **Cluster 2 – Diverse and Cost-Conscious Shoppers**
• Provide discounts, combo deals, or cash-back offers to cater to their budget-conscious habits.
• Launch targeted weekend promotions to match their high weekend activity.
• Offer personalized deals featuring multiple cuisines to reflect their diverse preferences.

<br>

---

## 📊 **Evaluation Metrics**

The performance of the clustering algorithms was evaluated using the following metrics:

- **R² Score**: Measures how well the clustering model fits the data.
- **Silhouette Score**: Assesses the cohesion and separation of clusters.
- **Calinski-Harabasz Score**: Evaluates the dispersion of clusters, ensuring they are distinct.
- **Elbow plot**: to understand the best number of clusters in K-Prototypes. ONLY FOR **CUSTOMER SEGMENTATION**

<br>

---

### 📚 Lessons Learned & Future Improvements

Throughout this project, we gained valuable insights into the clustering process and how to approach data analysis in a more effective and efficient manner. Here are some potential improvements for this projects:

1. **Data Preprocessing - Scaling the Data**:
   - One of the key mistakes in our data preprocessing was failing to scale the data before applying KNN imputation. As KNN relies on the distance between data points, it is essential to normalize the data to ensure that all features contribute equally to the distance calculations.

2. **Customer Segmentation - Feature Selection**:
   - In the customer segmentation process, we could have discarded the binary feature `is_repeat_customer`, as it did not have a significant impact on the clustering results. Including this feature did not provide meaningful information for segmenting customers. 

3. **Clustering - Final Clustering Approach**:
   - For the final clusters, we could have taken a more refined approach by first selecting the best clusters identified during the segmentation process, for instance the 2 or 3 best. By focusing on the most meaningful segments and using them for the final merging step, we could have avoided ending up with more than 300 clusters. A more selective merging process based on cluster performance would likely have resulted in more cohesive and manageable clusters. 


<br>

---

## 🛠 **Getting Started**

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MGN19/Customer-Segmentation.git
   ```

2. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Run the Project**:
   - **Data Exploration**:  
     ```bash
     jupyter notebook DM2425_Part1_77.ipynb
     ```

   - **Data Preprocessing**:  
     ```bash
     jupyter notebook DM2425_Part2_77_01.ipynb
     ```

   - **Cuisine Segmentation**:  
     ```bash
     jupyter notebook DM2425_Part2_77_02.ipynb
     ```

   - **Customer Segmentation**:  
     ```bash
     jupyter notebook DM2425_Part2_77_03.ipynb
     ```

   - **Temporal Segmentation**:  
     ```bash
     jupyter notebook DM2425_Part2_77_04.ipynb
     ```

   - **Spending Segmentation**:  
     ```bash
     jupyter notebook DM2425_Part2_77_05.ipynb
     ```

   - **Product Segmentation**:  
     ```bash
     jupyter notebook DM2425_Part2_77_06.ipynb
     ```

   - **Final Segmentation**:  
     ```bash
     jupyter notebook DM2425_Part2_77_07.ipynb
     ```

<br>

---
---


### 🌐 Interactive Website

To enhance the user experience and provide an interactive tool for exploring our clustering results, we developed an **interactive website**. The website serves as a visualization and interpretation tool for the project and includes the following main features:

---

#### **Website Features**:

1. **Project Overview**:
   - A clear explanation of the project’s objectives, allowing users to understand the scope and goals of the work.

2. **Data Exploration**:
   - **Interactive Visualizations** that enable users to explore the dataset used in the project.
   - Features include:
     - Assessing pairwise relationships between numerical features.
     - Plotting histograms for both numerical and categorical features.
   - **Customization** options:
     - Users can customize the visualizations, including color schemes.
     - Adjust the number of bins for numerical data histograms.

3. **Cluster Analysis**:
   - Users can select the segment to analyze or use the combination of all segments.
   - **Drop-down Menus** to view features that compose each segment.
   - The clustering section includes:
     - **Cluster Profiles**: Users can choose features to compare across different clusters (e.g., `customer_age`, `vendor_count`).
     - **Boxplots**: To view the distribution of specific variables within each cluster.
     - **Dimensionality Reduction**: Visualize the data with T-SNE or UMAP. Users can choose the number of neighbors (for UMAP) and plot the resulting visualization.

5. **About Us Page**:
   - Provides information about the roles of team members, academic backgrounds, relevant experience, extracurricular activities, and contact details (phone, email, and LinkedIn profiles).
   - Includes a brief history of **TargetSphere Advisors**, along with our **Vision**, **Values**, and **contact options**.

<br>

#### 🛠 **Prerequisites to Run the Streamlit App**:
To run the interactive website using Streamlit, make sure to run the following:

- **Functions used in the app**:  
     ```bash
     python file extra_functions.py
     ```

   - **Application**:  
     ```bash
     python file extra_work.py
     ```

To launch the app, use the following command:
streamlit run extra_work.py
