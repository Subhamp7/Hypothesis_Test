# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 23:56:37 2020

@author: subham
"""
#loading the libraries
try:
    import scipy.stats as stats
    import seaborn as sns
    import numpy as np
    import pandas as pd
except Exception as e:
    print("Unable to load library",e)

#loading the dataset
data=pd.read_csv("tips_data.csv")

#describing the data
print('Describe numerical Data\n',data.describe())

#relation btw categorical value
data_cat=pd.crosstab(data['sex'],data['smoker'])
print('\nRelation between gender and somker\n\n',data_cat)

