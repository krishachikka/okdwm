import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# Creating the DataFrame
data = {
    "Country": [
        "France",
        "Spain",
        "Germany",
        "Spain",
        "Germany",
        "France",
        "Spain",
        "France",
        "Germany",
        "France",
    ],
    "Age": [44, 27, 30, 38, np.nan, 35, np.nan, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, np.nan, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"],
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Filling missing values with the mean
df[["Age", "Salary"]] = df[["Age", "Salary"]].fillna(df[["Age", "Salary"]].mean())
print("\nData after filling missing values:")
print(df)

# Binning the data
bins_age = pd.cut(df["Age"], bins=3, labels=False)
bins_salary = pd.cut(df["Salary"], bins=3, labels=False)
df["Age_Binned"] = bins_age
df["Salary_Binned"] = bins_salary
print("\nData after binning:")
print(df[["Age", "Salary", "Age_Binned", "Salary_Binned"]])

# Z-score normalization
scaler = StandardScaler()
df[["Age_Normalized", "Salary_Normalized"]] = scaler.fit_transform(
    df[["Age", "Salary"]]
)
print("\nData after Z-score normalization:")
print(df[["Age", "Salary", "Age_Normalized", "Salary_Normalized"]])
