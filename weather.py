import pandas as pd

df_temp = pd.read_csv('data_files/tas_mean_per_month_per_country.csv')
df_happy = pd.read_csv('data_files/WHR2021.csv')
print(df_temp.columns)

df_temp = df_temp.drop(columns=['iso3'])
df_temp = df_temp[df_temp['year'] >= 2008]

df_temp = df_temp.groupby(['year','country']).mean().reset_index()
#df_temp.groupby(['year','country']).mean().to_csv('year_country_mean.csv')

mapped_country_temp = (df_happy.merge(df_temp.rename(columns={'country':'Country name'}), on=['Country name', 'year'], how='left'))

mapped_country_temp.to_csv("testing_mapped.csv")