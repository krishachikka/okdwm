# okdwm
# Data Mining Algorithms in WEKA

## Table of Contents
- [K-Means Clustering](#k-means-clustering)
- [Decision Tree Induction](#decision-tree-induction)
- [Apriori Algorithm](#apriori-algorithm)

---

## K-Means Clustering

### Steps to Implement K-Means in WEKA
1. Open WEKA Explorer.
2. Click on "Open file" to load your ARFF file.
3. Select the "Cluster" tab.
4. Choose "K-Means" from the clustering algorithms.
5. Click "Start" to run the algorithm.
6. View the results in the "Result list" pane.

### Input ARFF File - save as iris.arff
```arff
@RELATION iris
@ATTRIBUTE x NUMERIC
@DATA
1
2
3
8
9
10
25
```
---

# Decision Tree induction

### Steps to Implement ID3 in WEKA
1. Open WEKA Explorer.
2. Click on "Open file" to load your ARFF file.
3. Select the "Classify" tab.
4. Click on "Choose" and select "Trees" -> "J48".
5. Click "Start" to run the classification.
6. Right-click on the result list to visualize the decision tree.

### Input ARFF File - save as weather.arff
```arff
@relation weather
@attribute outlook {sunny, overcast, rain}
@attribute temperature {hot, mild, cool}
@attribute humidity {high, normal}
@attribute windy {true, false}
@attribute Play {P, N}

@data
sunny, hot, high, false, N
sunny, hot, high, true, N
overcast, hot, high, false, P
rain, mild, high, false, P
rain, cool, normal, false, P
rain, cool, normal, true, N
overcast, cool, normal, true, P
sunny, mild, high, false, N
sunny, cool, normal, false, P
rain, mild, normal, false, P
sunny, mild, normal, true, P
overcast, mild, high, true, P
overcast, hot, normal, false, P
rain, mild, high, true, N
```
# Apriori Algorithm

1. Open WEKA Explorer.
2. Click on "Open file" to load your ARFF file.
3. Select the "Associate" tab.
4. Click on "Choose" and select "Associators" -> "Apriori".
5. Click "Start" to run the association rule mining.
6. View the generated association rules in the results list.

### Input ARFF File - save as test_apriori.arff
```arff
@relation TEST_APRIORI
@attribute A {TRUE, FALSE}
@attribute B {TRUE, FALSE}
@attribute C {TRUE, FALSE}
@attribute D {TRUE, FALSE}
@attribute E {TRUE, FALSE}
@attribute F {TRUE, FALSE}
@attribute G {TRUE, FALSE}
@attribute H {TRUE, FALSE}

@data
TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE
TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE
FALSE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, TRUE
FALSE, TRUE, FALSE, FALSE, TRUE, FALSE, TRUE, TRUE
TRUE, TRUE, FALSE, TRUE, TRUE, FALSE, TRUE, TRUE
TRUE, FALSE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE
FALSE, TRUE, FALSE, TRUE, TRUE, FALSE, TRUE, TRUE
TRUE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE
FALSE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, TRUE
TRUE, FALSE, TRUE, FALSE, TRUE, TRUE, FALSE, TRUE
FALSE, FALSE, TRUE, FALSE, TRUE, FALSE, FALSE, TRUE
TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE
FALSE, TRUE, TRUE, FALSE, TRUE, TRUE, FALSE, TRUE
TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, FALSE, TRUE
TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, FALSE, TRUE
```


