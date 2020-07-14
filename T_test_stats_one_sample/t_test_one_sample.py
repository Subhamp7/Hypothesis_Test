# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:21:12 2020

@author: subham
"""
#loading the dataset
try:
    import pandas as pd
    import numpy as np
    from scipy.stats import ttest_1samp
except Exception as index:
    print("Unable to load the Libraries",index)
    
#initializing the sample size and alpha value
sample_size=10
alpha=0.0

#loading the dataset
data=pd.read_csv("golf.csv").iloc[:,0]

#mean of the dataset
data_mean=data.mean()

#selecting random 10 data from dataset
sample=np.random.choice(data,sample_size)

#applying the function to get the p_value
ttest,p_value=ttest_1samp(sample,data_mean)

#comparing the P value with alpha value
if p_value < alpha:    # alpha value is 0.05 or 5%
    print("Rejecting Null Hypothesis")
else:
    print("Accepting Null Hypothesis")
