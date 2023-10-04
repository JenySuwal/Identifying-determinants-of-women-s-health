import numpy as np
import pandas as pd
import pyreadstat 
import seaborn as sns

df1, meta = pyreadstat.read_sav('C:/Users/Jenna/Desktop/Nepal MICS6 SPSS Datasets/wm.sav')
wm = df1[["HH1","HH2","WB4","wscore","MN3A","MN3B","MN3C","MN3D","MN3E","MN19A","MN19B","MN19C","MN19D","MN19E","UN12A","UN12B","UN12C","UN12D","UN12F","UN12G","UN12H","TA8A","TA8B","TA8D","TA12A","TA12B","TA12C","welevel1","windex5"]]
wm_selected=wm.rename(columns={'HH1':'Cluster_no','HH2':'Household_no','WB4':'woman_age','wscore':'Wealth_score','MN3A':'Pre_doctor','MN3B':'Pre_nurse','MN3C':'Pre_auxiliaryNursing','MN3D':'Pre_healthAssitant','MN3E':'Pre_maternalChildHealthWorker','MN19A':'Birth_doctor','MN19B':'Birth_staffNurse','MN19C':'Birth_auxulliaryNursing','MN19D':'Birth_healthAssitant','MN19E':'Birth_maternalChildHealthWorker','UN12A':'Pregnant_noSex','UN12B':'Pregnant_menopausal','UN12C':'Pregnant_neverMensturated','UN12D':'Pregnant_hysterectomy','UN12F':'Pregnant_postpartumAmenorrheic','UN12G':'Pregnant_breastfeeding','UN12H':'Pregnant_tooOld','TA8A':'Smoked_cigars','TA8B':'Smoked_waterPipe','TA8D':'Smoked_sesha','TA12A':'Smokeless_chewingTobacco','TA12B':'Smokeless_snuff','TA12C':'Smokeless_gutka','welevel1':'woman_education','windex5':'wealth_index_quintile'})

df2, meta = pyreadstat.read_sav('C:/Users/Jenna/Desktop/Nepal MICS6 SPSS Datasets/hh.sav')
hh=df2[["HH1","HH2","HC2","HC13","HH7c","helevel1","WS11"]]
hh_selected=hh.rename(columns={'HH1':'Cluster_no','HH2':'Household_no','HC2':'Caste_of_household_head','HC13':'Internet_access','HH7c':'Provience','helevel1':'Househld_head_eduction','WS11':'Type_of_toilet'})


df_merged= pd.merge(wm_selected,hh_selected ,on=['Cluster_no','Household_no'])
df_merged
#df_merged = df_merged.replace('?', np.nan)

df_merged.to_csv(r'C:\Users\Jenna\Desktop\Spyder\colz_mics\orignal.csv',index=False)

