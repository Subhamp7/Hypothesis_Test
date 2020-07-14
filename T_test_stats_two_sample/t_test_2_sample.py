# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:03:34 2020

@author: subham
"""

#loading the dataset
try:
    import pandas as pd
    import numpy as np
    from scipy.stats import ttest_ind
except Exception as index:
    print("Unable to load the Libraries",index)
    
#initializing the alpha value
alpha=0.05

#loading the dataset
data_A=pd.read_csv("golf.csv").iloc[:,0]
data_B=pd.read_csv("golf.csv").iloc[:,1]

#mean of the dataset
data_mean=data_A.mean()

#applying the function to get the p_value
ttest,p_value=ttest_ind(a=data_A, b=data_B)

#comparing the P value with alpha value
if p_value < alpha:    # alpha value is 0.05 or 5%
    print("Rejecting Null Hypothesis")
else:
    print("Accepting Null Hypothesis")