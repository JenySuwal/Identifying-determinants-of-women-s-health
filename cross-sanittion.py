import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import chi2
import scipy


df=pd.read_csv('C:/Users/Jenna/Desktop/Spyder/colz_mics/final.csv')

df1=pd.read_csv('C:/Users/Jenna/Desktop/Spyder/colz_mics/orignal.csv')
pd.crosstab(df1.Type_of_toilet,df.Provience)
pd.crosstab(df1.Type_of_toilet,df.Provience).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","red","green","orange","yellow","black"]);
plt.title("Sanitation with Province")

ct_table_inde=pd.crosstab(df1.Type_of_toilet,df.Provience)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_inde)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")

pd.crosstab(df1.Type_of_toilet,df.woman_education)
pd.crosstab(df.Type_of_toilet,df.woman_education).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","red","green","orange","yellow","black"]);
plt.title("Sanitation with woman_education")
ct_table_inde2=pd.crosstab(df.Pre_doctor,df.woman_education)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_inde2)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")

pd.crosstab(df.Type_of_toilet,df.Wealth)
ct_table_inde3=pd.crosstab(df.Type_of_toilet,df.Wealth)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_inde3)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
pd.crosstab(df.Type_of_toilet,df.Wealth).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange","black"]);
plt.title("Sanitation with wealth index")

pd.crosstab(df1.Type_of_toilet,df1.Caste)
pd.crosstab(df.Type_of_toilet,df1.Caste).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Sanitation with caste")
ct_table_inde4=pd.crosstab(df.Type_of_toilet,df1.Caste)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_inde4)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")

