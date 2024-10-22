import numpy as np
import matplotlib.pyplot as plt

def five_number_summary(data):
    data = np.array(data)
    
    # Five-number summary
    minimum = np.min(data)
    Q1 = np.percentile(data, 25)
    median = np.median(data)
    Q3 = np.percentile(data, 75)
    maximum = np.max(data)
    
    return minimum, Q1, median, Q3, maximum

def detect_outliers(data):
    data = np.array(data)
    
    # Calculate Q1, Q3 and IQR
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    
    # Define outlier boundaries
    lower_boundary = Q1 - 1.5 * IQR
    upper_boundary = Q3 + 1.5 * IQR
    
    # Find outliers
    outliers = data[(data < lower_boundary) | (data > upper_boundary)]
    
    return outliers

def plot_boxplot(data):
    plt.boxplot(data, vert=False)  # Set vert=False for horizontal box plot
    plt.title('Boxplot of the Data')
    plt.xlabel('Values')  # Change ylabel to xlabel for horizontal plot
    plt.show()

# Example data
data = [22, 24, 26, 28, 29, 31, 35, 37, 41, 53, 64]

# Five-number summary
summary = five_number_summary(data)
print("Five Number Summary: Minimum, Q1, Median, Q3, Maximum")
print(summary)

# Detect outliers
outliers = detect_outliers(data)
print("Outliers:", outliers)

# Box plot
plot_boxplot(data)
