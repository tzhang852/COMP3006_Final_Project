import pandas as pd
import AppConfig
import plotly.express as px
import boto3
import os


class Temperature:
    def __init__(self):
        self.df = self._clean_data()

    def _load_data(self):
        """
        Forces 5 columns since some country names contain comma

        :returns dataframe built from weather dataset:
        """
        appConfig = AppConfig.AppConfig()
        file_path = 'data_files/tasmax.csv'
        s3 = boto3.client('s3', aws_access_key_id=appConfig.accessKeyId,
                          aws_secret_access_key=appConfig.secretAccessKey,
                          region_name=appConfig.region)
        s3.download_file(appConfig.bucket, file_path, file_path)
        return pd.read_csv(file_path, usecols=range(5))

    def _clean_data(self):
        """
        Loads in data _load_data function
        Drops irrelevant columns, renames columns to more appropriate names, strips from leading spaces from strings,
        removes data for years prior to 2008 as world happiness dataset only goes back to 2008
        Takes average over year for each country (the month column is lost in this process)

        :returns cleaned dataset:
        """
        file_path = "data_files/tasmax.csv"
        exists = os.path.exists(file_path)
        if not exists:
            df_temp = self._load_data(self)
        else:
            df_temp = pd.read_csv(file_path, usecols=range(5))

        df_temp = df_temp.drop(columns=[' ISO3'])
        df_temp = df_temp.rename(columns={' Year': 'year',
                                          ' Statistics': 'month',
                                          'tasmax': 'max_temp',
                                          ' Country': 'country'})
        df_temp['country'] = df_temp['country'].str.lstrip()
        df_temp = df_temp[df_temp['year'] >= 2008]
        df_temp = df_temp.groupby(['year', 'country']).mean().reset_index()
        return df_temp.reset_index()

    def temp_heat_map(self):
        """
        Displays an interactive map of all countries
        User can select year to see heat map for countries in selected year
        """
        fig = px.choropleth(self.df,
                            locations="country",
                            locationmode='country names',
                            color="max_temp",
                            hover_name="country",
                            range_color=[self.df.max_temp.min(), self.df.max_temp.max()],
                            color_continuous_scale="blues",
                            title='Max Temperature by countries from 2008 to 2020',
                            animation_frame="year")
        fig.update(layout_coloraxis_showscale=True)
        fig.show()

    def temp_bubble_map(self):
        """
        Displays an interactive map of all countries
        User can select year to see heat map for countries in selected year
        """
        # setting 0s to 1s since negative size does not work and 1 is sufficintly small for visulization
        self.df['max_temp'].values[self.df['max_temp'] < 0] = 1
        fig = px.scatter_geo(self.df,
                             locations="country",
                             locationmode='country names',
                             color="max_temp",
                             hover_name="country",
                             color_continuous_scale="blues",
                             size=self.df.max_temp,
                             title='Max Temperature by countries from 2008 to 2020',
                             animation_frame="year")
        fig.update(layout_coloraxis_showscale=True)
        fig.show()

    def top_n_hottest_countries(self, n, year=None):
        """
        Returns the top n hottest (country with highest average max temperature) countries for all time (over the dataset)
        If years parameter is provided then it will return the top n hottest countries for that year

        :param n: default value of 1
        :param year:
        :return:
        """
        if year is None:
            return self.df.sort_values(by=['max_temp'], ascending=False).head(n)[['year', 'country', 'max_temp']]
        return_df = self.df.loc[self.df['year'] == int(year)]
        return return_df.sort_values(by=['max_temp'], ascending=False).tail(n)[['year', 'country', 'max_temp']]

    def top_n_coldest_countries(self, n, year=None):
        """
        Returns the top n coldest (country with lowest average max temperature) countries for all time (over the dataset)
        If years parameter is provided then it will return the top n coldest countries for that year

        :param n:
        :param year:
        :return:
        """
        if year is None:
            return self.df.sort_values(by=['max_temp']).head(n)[['year', 'country', 'max_temp']]
        return_df = self.df.loc[self.df['year'] == int(year)]
        return return_df.sort_values(by=['max_temp']).head(n)[['year', 'country', 'max_temp']]


Temperature().temp_bubble_map()