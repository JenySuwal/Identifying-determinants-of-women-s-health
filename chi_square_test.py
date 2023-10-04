from sklearn.feature_selection import chi2
from scipy.stats import chi2_contingency 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import pyreadstat 

df0=pd.read_csv('orignal.csv')

df2, meta = pyreadstat.read_sav('C:/Users/Jenna/Desktop/Nepal MICS6 SPSS Datasets/hh.sav')
df=df2["WS11"]
df3=df2.rename(columns={'WS11':'Sanitation'})
#result = pd.concat([df1, df4], ignore_index=True, sort=False)
result=pd.concat([df0, df3], axis=1)
