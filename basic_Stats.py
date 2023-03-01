''' Author: Paras M Salunkhe
Date: 28/02/23
Basic Statistics Assignment 1
'''

import pandas as pd
import statistics
import scipy

# Importing the dataset
dataset = pd.read_csv('Q7.csv')
Points = dataset.iloc[:, 1].values
Score = dataset.iloc[:, 2].values
Weight = dataset.iloc[:, 3].values
Marks = [34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]
'''print(Points)
print(Score)
print(Weight)
'''
arr = Marks

# calculate mean
mean =  sum(arr) / len(arr)
print("mean = ", mean)

#calculate median
sorted_arr = sorted(arr)
n = len(arr)
mid = n // 2
if n % 2 == 0:
    median = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    print("Median = ", median)
else:
    median = sorted_arr[mid]

#calculate mode
mode = statistics.mode(arr)
print("Mode = ", mode)

#calculate varience

variance = statistics.variance(arr)
print("Variance = ", variance)
#calculate standard deviation

standard_dev = statistics.stdev(arr)
print("Standard Deviation = ", standard_dev)

#calculate range

range = max(arr) - min(arr)
print("Range = " , range)

# calculate skewness

dataset = pd.read_csv('Q9_b.csv')
SP = dataset.iloc[:, 1].values
Weight = dataset.iloc[:, 2].values

arr2 = Weight
from scipy.stats import skew
from scipy.stats import kurtosis

Skew = skew(arr2, axis=0, bias=True)
print("Skew = ", Skew)

Kurtosis = kurtosis(arr2, axis=0, bias=True)
print("Kurtosis = ", Kurtosis)
