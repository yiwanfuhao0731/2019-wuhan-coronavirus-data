# @zy20200204
# to fetch the day on day data of China new cases confirmed (ex Hubei)
# calculate the GDP weighted (ex Hubei) new cases
import pandas as pd
import glob

all_name_list = [n for n in glob.glob(r"d:\yangs\Third_yr_grad_English\relevant_file\workspace_zy\2019-wuhan-coronavirus-data\data-sources\dxy\data\2020*-dxy-2019ncov-data.csv")]
eod = {}
for n in all_name_list:
    d = n.split('-')[-5].split('\\')[-1]
    t = n.split('-')[-4]
    if d in eod.keys():
        if int(t) > int(eod[d]):
            eod[d] = t
    else:
        eod[d]=t

all_dir = []
for k,v in eod.items():
    before = "d:\\yangs\\Third_yr_grad_English\\relevant_file\workspace_zy\\2019-wuhan-coronavirus-data\data-sources\dxy\data\\"
    after = "-dxy-2019ncov-data.csv"
    dir =  before + str(k)+'-'+str(v)+after
    all_dir.append(dir)

df_list = []
for dir,date in zip(all_dir[:],eod.keys()):
    df = pd.read_csv(dir,sep='|',skiprows=2,header=0,index_col=0)
    df = df.loc[:,['confirmed_cases']]
    df.columns = [date]
    df_list.append(df)

df_comb = pd.concat(df_list,axis=1)
mask = [i not in ['CHINA TOTAL'] for i in df_comb.index]
print (mask)
df_comb = df_comb.loc[mask,:]
df_comb.to_csv('confirm_matrix_region.csv')
