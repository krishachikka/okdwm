# Data Preprocessing in WEKA

## Table of Contents
- [Remove Missing Values](#remove-missing-values)
- [Outliers](#outliers)

---

## Remove Missing Values

### Steps to Remove Missing Values
1. Open WEKA Explorer.
2. Click on **Open File** -> **Choose**.
3. Select the **Associate** tab.
### CSV File: data1
1. Choose -> **Filters** -> **Unsupervised** -> **Attributes** -> **ReplaceMissingValues**.
3. In **Attributes**, tick one.
4. 4. Click **Edit** -> will show the loaded file data before data cleaning
5. Click **Apply**.
6. Click **Edit** -> will show the loaded file data

---

## Outliers

### Steps to Handle Outliers
1. Navigate to: `This PC` -> `C Drive` -> `Program Files (x86)` -> `Weka` -> `Data` -> `Diabetes`.
2. Copy the file to your Desktop.
3. Open WEKA software and click **Open ARFF file**.
4. Open the file: **Diabetes**.
5. Choose -> **Filters** -> **Unsupervised** -> **Attributes** -> **IQR**.
6. Click **Edit** -> Check the 2nd last column: **Yes/No** (Observe the values).
7. In **Attributes**, checkmark the tick for outlier.
8. Choose -> **Filters** -> **Unsupervised** -> **Attributes** -> **Remove**.
9. Right-click on **Remove** -> **Show Properties** -> **AttributeIndices** -> Type `10` -> Click **OK**.
10. Click **Apply**.
11. Click **Edit**.
12. Confirm there is no **Yes/No** column.
