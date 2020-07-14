# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 23:56:37 2020

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
data=pd.read_csv("tips_data.csv")

#describing the data
print('Describe numerical Data\n',data.describe())

#assign the values
X=data['sex']
Y=data['smoker']

#relation btw categorical value
data_observed=pd.crosstab(X,Y)
print('\nRelation between gender and somker\n',data_observed)

cont=stats.chi2_contingency(data_observed.values)
data_expected=cont[3]
data_observed=data_observed.to_numpy()

#getting the no of rows and columns
no_of_rows=data_observed.shape[0]
no_of_columns=data_observed.shape[1]

#calculating degree of freedom
degree_of_freedom=(no_of_rows-1)*(no_of_columns-1)
print("\nThe degree of freedom is :",degree_of_freedom)

#chi square statistic
chi_square=sum([(o-e)**2./e for o,e in zip(data_observed,data_expected)])
chi_square_stat=np.sum(chi_square)
print("The chi square statistic is :",chi_square_stat)

#calculating p value
p_value=1-chi2.cdf(x=chi_square_stat,df=degree_of_freedom)
print("The P value is :",p_value)

alpha = 0.05

#comparing the p and alpha value
if p_value<=alpha:
    print("\nReject H0,There is a relationship between 2 categorical variables")
else:
    print("\nRetain H0,There is no relationship between 2 categorical variables")