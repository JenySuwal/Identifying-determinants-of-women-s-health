import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1=pd.read_csv('C:/Users/Jenna/Desktop/Spyder/colz_mics/orignal.csv')
df=pd.read_csv('C:/Users/Jenna/Desktop/Spyder/colz_mics/final.csv')
df1.woman_age.plot.hist(edgecolor="black");
df1.Provience.plot.hist(edgecolor="black")
df.Wealth.plot.hist(edgecolor="black")
df.woman_education.plot.hist(edgecolor="black")
df.Caste.plot.hist(edgecolor="black")
