import pandas as pd
import AppConfig
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import boto3
import argparse
import os


class Happiness:
    def __init__(self):
        self.df = self._clean_data()

    def _load_data(self):
        """
        :returns dataframe built from happiness dataset:
        """
        appConfig = AppConfig.AppConfig()
        s3 = boto3.client('s3', aws_access_key_id=appConfig.accessKeyId,
                          aws_secret_access_key=appConfig.secretAccessKey,
                          region_name=appConfig.region)
        s3.download_file(appConfig.bucket, 'data_files/WHR2021.csv', 'data_files/happiness.csv')
        return pd.read_csv('data_files/happiness.csv')

    def _clean_data(self):
        """
        Loads in data _load_data function
        Drops irrelevant columns, renames columns to more appropriate names, strips from leading spaces from strings,
        removes data for years prior to 2008 as world happiness dataset only goes back to 2008
        Takes average over year for each country (the month column is lost in this process)

        :returns cleaned dataset:
        """
        exists = os.path.exists("data_files/WHR2021.csv")
        if not exists:
            df_happiness = self._load_data()
        else:
            df_happiness = pd.read_csv('data_files/happiness.csv', usecols=range(5))

        df_happiness = df_happiness.drop(columns=['Log GDP per capita', 'Social support',
                                                  'Healthy life expectancy at birth',
                                                  'Freedom to make life choices', 'Generosity',
                                                  'Perceptions of corruption', 'Positive affect',
                                                  'Negative affect'])
        print(df_happiness.columns)
        df_happiness = df_happiness.rename(columns={'Country name': 'country',
                                                    'year': 'year',
                                                    'Life Ladder': 'happiness'})
        df_happiness = df_happiness[df_happiness['year'] >= 2008]
        print(df_happiness.columns)
        df_happiness = df_happiness.groupby(['year', 'country']).mean().reset_index()
        return df_happiness.reset_index()

    def happiness_map(self):
        """
        Displays an interactive map of all countries
        User can select year to see heat map for countries in selected year
        """
        fig = px.choropleth(self.df,
                            locations="country",
                            locationmode='country names',
                            color="happiness",
                            hover_name="country",
                            range_color=[self.df.happiness.min(), self.df.happiness.max()],
                            color_continuous_scale="blues",
                            title='Happiness by Country',
                            animation_frame="year")
        fig.update(layout_coloraxis_showscale=True)
        fig.show()

    def happiness_bar(self):
        """
        Displays a bar graph of happiness by countries in 2020
        """
        current_year = self.df[self.df['year'] == 2020][:166]
        plt.rcParams['figure.figsize'] = (30, 7)
        graph = sns.barplot(x=current_year['country'][:166], y=current_year['happiness'][:166])
        graph.set_xlabel(xlabel='Country', fontsize=10)
        graph.set_ylabel(ylabel='Happiness Index', fontsize=10)
        graph.set_title(label='Happiness by Country', fontsize=20)
        plt.xticks(rotation=90)
        plt.show()

    # def happiness_line(self):
    #     """
    #     Displays a line graph for each country with relative parameters that influence happiness
    #     """
    #     current_year = self.df[self.df['year'] == 2020][:166]
    #     #df.loc[df['happiness'] < 100, 'country'] = 'Other countries' # Represent only large countries
    #     fig = px.pie(current_year, values='happiness', names='country', title='Happiness by Country in 2020')
    #     fig.show()

    def top_n_happiest_countries(self, n, year=None):
        """
        Returns the top n happiest (country with highest happiness index) countries for all time (over the dataset)
        If years parameter is provided then it will return the top n saddest countries for that year

        :param n:
        :param year:
        :return:
        """
        if year is None:
            return self.df.sort_values(by=['happiness'], ascending=False).head(n)[['year', 'country', 'happiness']]
        return_df = self.df.loc[self.df['year'] == int(year)]
        return return_df.sort_values(by=['happiness'], ascending=False).head(n)[['year', 'country', 'happiness']]

    def top_n_saddest_countries(self, n, year=None):
        """
        Returns the top n saddest (country with lowest happiness index) countries for all time (over the dataset)
        If years parameter is provided then it will return the top n saddest countries for that year

        :param n:
        :param year:
        :return:
        """
        if year is None:
            return self.df.sort_values(by=['happiness']).head(n)[['year', 'country', 'happiness']]
        return_df = self.df.loc[self.df['year'] == int(year)]
        return return_df.sort_values(by=['happiness']).head(n)[['year', 'country', 'happiness']]
