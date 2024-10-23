# Clustering

**Definition:**  
Clustering is the process of grouping similar patterns into the same cluster.

**Applications:**

- Image processing
- Classification

## Clustering Techniques

1. **Partitioning Methods:**

   - **K-Means**
   - **K-Medoids**

2. **Hierarchical Methods:**
   - **Agglomerative**
     - Single Linkage
     - Complete Linkage
     - Average Linkage
     - Centroid Linkage
   - **Divisive Methods**

### K-Means Algorithm

**Steps:**

1. Select random initial means (centroids).
2. Assign each data point to the nearest centroid to form clusters.
3. Calculate the distance of elements from the centroids.
4. Update the centroids based on the mean of the assigned clusters.
5. If the centroids do not change (previous mean = current mean), stop; otherwise, repeat from step 2.

### K-Medoids Algorithm

Similar to K-Means, but:

- Calculate the old cost and new cost.
- Swapping cost = old cost - new cost.
- If the swapping cost is greater than or equal to zero, stop; otherwise, repeat with other medoids.

### Hierarchical Clustering

1. **Single Linkage:**
   - Find the distance matrix.
   - Identify the minimum distance.
   - Merge those elements and repeat until all elements are merged.
   - Dendrogram is created to represent the hierarchy.

---

# Classification

**Definition:**  
Classification is the process of categorizing data based on specified parameters.

**Algorithms:**

- Decision Tree Induction (ID3)
- Bayesian Classification

### ID3 Algorithm

1. Calculate information gain: \( I(p, n) \).
2. Calculate entropy and information gain: \( Gain = I - E \).
3. Select the attribute with the maximum gain as the root node.
4. Repeat the process for each branch.

### Bayesian Classification

1. Calculate the probability of each class (e.g., yes or no) based on given conditions.
2. Compute the summation of probabilities.
3. Assign the class with the maximum probability.

### Methods to Calculate Accuracy

- **Bootstrap Method:** Sample part of the data for training and testing.
- **Holdout Method:** Divide data into two parts for training and testing.

---

# Data Warehousing Fundamentals

**Definition:**  
A data warehouse is a subject-oriented, integrated collection of data where new data can be added, but old data is not removed.

### Key Concepts

- **Metadata:** Provides additional information about the data.
- **Data Mart:** A subset of a data warehouse, typically smaller than 100GB, often used by small businesses.
- **Dimension Modeling:** Represented by a cube, which can be rotated for different views.
- **Entity-Relationship (ER) Modeling**

### Schemas

1. **Star Schema:** Simplified schema where a central fact table is connected to multiple dimension tables.
2. **Snowflake Schema:** A normalized version of the star schema, where some dimension tables are further normalized.
3. **Fact Constellation:** Contains multiple fact tables and connected dimensions.

### OLAP Operations

- **Rollup:** Aggregate the data.
- **Drill Down:** Expand the data for more detail.
- **Slice:** Display only two dimensions of the data.
- **Dice:** Create a smaller data cube by selecting specific dimensions.
- **Pivot:** Rotate the view of the data table anticlockwise.

**Comparison:**

- **OLTP (Online Transaction Processing):** Focuses on transaction-oriented tasks, using ER Modeling and typically involves isolated data.
- **OLAP (Online Analytical Processing):** Focuses on data analysis and reporting, using Dimension Modeling with integrated data.

---

# Preprocessing

**Definition:**  
Preprocessing converts raw data into a more useful format for analysis.

### Statistical Measures

- **Mean**
- **Median**
- **Mode**
- **Variance**
- **Standard Deviation:** The square root of variance.

### Quartiles

- **Q1 and Q3:** First and third quartiles.
- **Q2:** Median of the dataset.
- **IQR (Interquartile Range):** \( Q3 - Q1 \).
- **Box Plot:** A graphical representation summarizing the five-number summary of data.

**Upper Boundary Calculation:**  
\[ \text{Upper Boundary} = Q3 + 1.5 \times IQR \]

### Preprocessing Steps

1. **Data Cleaning:**
   - Fill in missing values.
   - Binning (data smoothing).
2. **Data Integration:**
   - Use Carl’s coefficient for integration.
3. **Data Transformation**
4. **Data Reduction:**
   - Data aggregation (rollup).

### Visualization

- **Histogram:** A graphical representation used to reduce the volume of data and visualize frequency distributions.
