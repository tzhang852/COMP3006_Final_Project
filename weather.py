import pandas as pd


class temperature:
    # def _load_data(self):
    df_temp = pd.read_csv('data_files/tasmax.csv', usecols=range(5))

    # df_happy = pd.read_csv('data_files/WHR2021.csv')
    print(df_temp.columns)
    df_temp = df_temp.rename(
        columns={' Year': 'year',
                 ' Statistics': 'statistics',
                 ' Country': 'country'})

    df_temp = df_temp.drop(columns=[' ISO3'])

    print(df_temp.columns)

    df_temp['country'] = df_temp['country'].str.lstrip()

    df_temp = df_temp[df_temp['year'] >= 2008]
    df_temp = df_temp.groupby(['year', 'country']).mean().reset_index()
    # df_temp.groupby(['year','country']).mean().to_csv('year_country_mean.csv')
    # mapped_country_temp =
    #     (df_happy.merge(df_temp.rename(columns={'country': 'Country name'}), on=['Country name', 'year'], how='left'))

    print(df_temp)

    df_temp.to_csv("testing_mapped.csv")
