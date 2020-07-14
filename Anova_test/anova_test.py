# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:42:21 2020

@author: subham
"""

#loading the libraries
try:
    import scipy.stats as stats
    import pandas as pd
    import numpy as np
    from scipy.stats import chi2
    
except Exception as e:
    print("Unable to load library",e)

#loading the dataset 
dataset=pd.read_csv("tips_data.csv")

#splitting the data into X and Y
X=dataset["total_bill"]
Y=dataset["day"]
alpha=0.05

#finding the unique values from Y
uniq=pd.unique(Y.values)

#getting the X value for each unique value in Y and storing in an Dictionary
data_ad = {index:X[Y == index] for index in uniq}

#calculating the pvalue
f,p=stats.f_oneway(data_ad["Thur"],data_ad["Fri"],data_ad["Sat"],data_ad["Sun"])

#comparing the p value obtained from alpha value
if p<alpha:
    print("Reject null hypothesis")
else:
    print("Accept null hypothesis")