import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import chi2
import scipy


df=pd.read_csv('orignal.csv')
##############!!!!!!!!!!!!!!Prenatal doctor!!!!!!!!!!#############
# Create a plot of crosstab
pd.crosstab(df.Pre_doctor,df.Provience)
pd.crosstab(df.Pre_doctor,df.Provience).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","red","green","orange","yellow","black"]);
plt.title("Prenatal Doctor with Province")
plt.xlabel("?=No response, A= Recieved")
#####Chisquare test#############
ct_table_ind=pd.crosstab(df.Pre_doctor,df.Provience)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)

pd.crosstab(df.Pre_doctor,df.woman_age).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue"]);

ct_table_ind2=pd.crosstab(df.Pre_doctor,df.woman_education)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind2)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_doctor,df.woman_education).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red"]);
plt.title("Prenatal Doctor with woman education")
plt.xlabel("?=No response, A= Recieved")

ct_table_ind3=pd.crosstab(df.Pre_doctor,df.wealth_index_quintile)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind3)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_doctor,df.wealth_index_quintile).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Prenatal Doctor with wealth index")
plt.xlabel("?=No response, A= Recieved")

ct_table_ind4=pd.crosstab(df.Pre_doctor,df.Caste)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind4)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_doctor,df.Caste).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Prenatal Doctor with caste")
plt.xlabel("?=No response, A= Recieved")

pd.crosstab(index=df["Pre_doctor"], columns=["AGE"], values=df["woman_age"], aggfunc=np.mean).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
#pd.crosstab(df.Pre_doctor,df.woman_age).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Prenatal Doctor with woman age")
#plt.xlabel("?=No response, A= Recieved")

############!!!!!!!!!!!!!1Prenatal staffnurse!!!!!!!!!!!!!!!###############
ct_table_ind5=pd.crosstab(df.Pre_nurse,df.Provience)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind5)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_nurse,df.Provience).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange","black","green"]);
plt.title("Prenatal nurse with Provience")
plt.xlabel("?=No response, B= Recieved")

ct_table_ind6=pd.crosstab(df.Pre_nurse,df.woman_education)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind6)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_nurse,df.woman_education).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red"]);
plt.title("Prenatal nurse with woman education")
plt.xlabel("?=No response, B= Recieved")

ct_table_ind7=pd.crosstab(df.Pre_nurse,df.wealth_index_quintile)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind7)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_nurse,df.wealth_index_quintile).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Prenatal nurse with wealth index")
plt.xlabel("?=No response, B= Recieved")

ct_table_ind8=pd.crosstab(df.Pre_nurse,df.Caste)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind8)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_nurse,df.Caste).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Prenatal nurse with caste")
plt.xlabel("?=No response, B= Recieved")

#!!!!!!!!!!!!!!Pre_auxiliar!!!!!!!!!!!!!!!!!!!!!!##################
ct_table_ind9=pd.crosstab(df.Pre_auxiliaryNursing ,df.Provience)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind9)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_auxiliaryNursing ,df.Provience).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","red","green","orange","yellow","black"]);
plt.title("Prenatal Pre_auxiliaryNursing with Province")
plt.xlabel("?=No response, C= Recieved")

ct_table_ind10=pd.crosstab(df.Pre_auxiliaryNursing,df.woman_education)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind10)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_auxiliaryNursing,df.woman_education).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red"]);
plt.title("Prenatal Pre_auxiliaryNursing with woman education")
plt.xlabel("?=No response, C= Recieved")

ct_table_ind11=pd.crosstab(df.Pre_auxiliaryNursing,df.wealth_index_quintile)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind11)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_auxiliaryNursing,df.wealth_index_quintile).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Prenatal Auxiliary Nursing with wealth index")
plt.xlabel("?=No response, C= Recieved")

ct_table_ind12=pd.crosstab(df.Pre_auxiliaryNursing,df.Caste)
chi2_stat, p, dof, expected = scipy.stats.chi2_contingency(ct_table_ind12)
print(f"chi2 statistic:     {chi2_stat:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:\n",expected)
pd.crosstab(df.Pre_auxiliaryNursing,df.Caste).plot(kind="bar",figsize=(10,6),color=["salmon","lightblue","yellow","red","orange"]);
plt.title("Prenatal Auxiliary Nursing with caste")
plt.xlabel("?=No response, C= Recieved")










