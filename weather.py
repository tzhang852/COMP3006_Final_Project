import pandas as pd

# data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


class temperature:
    # def _load_data(self):
    def _load_data(self):
        return pd.read_csv('data_files/tasmax.csv', usecols=range(5))

    def _clean_data(self):
        df_temp = self._load_data()
        df_temp = df_temp.drop(columns=[' ISO3'])
        df_temp = df_temp.rename(columns={' Year': 'year',
                                          ' Statistics': 'max_temp',
                                          ' Country': 'country'})
        df_temp['country'] = df_temp['country'].str.lstrip()
        df_temp = df_temp[df_temp['year'] >= 2008]
        df_temp = df_temp.groupby(['year', 'country']).mean().reset_index()
        df_temp = df_temp.groupby(['year', 'country']).mean()
        return df_temp

    def temp_map(self):
        df_temp = self._clean_data()
        fig = px.choropleth(df_temp,
                            locations="country",
                            locationmode='country names',
                            color="Max Temperature",
                            hover_name="Country",
                            range_color=[1, 1000],
                            color_continuous_scale="blues",
                            title='Density of Countries in 2020')
        fig.update(layout_coloraxis_showscale=True)
        fig.show()

    temp_map()

# def _load_data(self):
def _load_data(self):
    return pd.read_csv('data_files/tasmax.csv', usecols=range(5))

def _clean_data(self):
    df_temp = self._load_data()
    df_temp = df_temp.drop(columns=[' ISO3'])
    df_temp = df_temp.rename(columns={' Year': 'year',
                                      ' Statistics': 'max_temp',
                                      ' Country': 'country'})
    df_temp['country'] = df_temp['country'].str.lstrip()
    df_temp = df_temp[df_temp['year'] >= 2008]
    df_temp = df_temp.groupby(['year', 'country']).mean().reset_index()
    df_temp = df_temp.groupby(['year', 'country']).mean()
    return df_temp

def temp_map(self):
    df_temp = self._clean_data()
    fig = px.choropleth(df_temp,
                        locations="country",
                        locationmode='country names',
                        color="Max Temperature",
                        hover_name="Country",
                        range_color=[1, 1000],
                        color_continuous_scale="blues",
                        title='Density of Countries in 2020')
    fig.update(layout_coloraxis_showscale=True)
    fig.show()

temp_map()
