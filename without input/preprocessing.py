import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load the dataset from the CSV file
dataset = pd.read_csv('Data.csv')

# 1. Filling in Missing Values
print("1. Filling in missing values")

# Create an imputer instance for numerical columns (mean strategy)
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Separate features and target variable
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Apply imputation
x[:, 1:3] = imputer.fit_transform(x[:, 1:3])

# Convert the imputed data back to a DataFrame for better readability
dataset_imputed = pd.DataFrame(x, columns=['Country', 'Age', 'Salary'])
dataset_imputed['Purchased'] = y
print(dataset_imputed)

# 2. Smoothing Using Binning
print("\n2. Smoothing using binning")

# Define bins and labels for 'Age'
age_bins = [20, 30, 40, 50, 60]
age_labels = ['20-30', '30-40', '40-50', '50-60']

# Define bins and labels for 'Salary'
salary_bins = [40000, 50000, 60000, 70000, 80000, 90000]
salary_labels = ['40K-50K', '50K-60K', '60K-70K', '70K-80K', '80K-90K']

# Apply binning
dataset_binned = dataset.copy()
dataset_binned['Age'] = pd.cut(dataset['Age'], bins=age_bins, labels=age_labels, include_lowest=True)
dataset_binned['Salary'] = pd.cut(dataset['Salary'], bins=salary_bins, labels=salary_labels, include_lowest=True)
print(dataset_binned)

# 3. Normalization Using Z-Score
print("\n3. Normalization using Z-score")

# Extract features for normalization
x = dataset_imputed.iloc[:, :-1].values

# Create a StandardScaler instance
scaler = StandardScaler()

# Apply normalization to 'Age' and 'Salary' columns (index 1 and 2)
x[:, 1:3] = scaler.fit_transform(x[:, 1:3])

# Convert the normalized data back to a DataFrame for better readability
dataset_normalized = pd.DataFrame(x, columns=['Country', 'Age', 'Salary'])
dataset_normalized['Purchased'] = y
print(dataset_normalized)