import pandas as pd
import AppConfig
import plotly.express as px
import boto3


class Temperature:
    def __init__(self):
        self.df = self._clean_data()

    def _load_data(self):
        """
        Forces 5 columns since some country names contain comma

        :returns dataframe built from weather dataset:
        """
        appConfig = AppConfig.AppConfig()
        # session = boto3.Session(aws_access_key_id=appConfig.accessKeyId,
        #                         aws_secret_access_key=appConfig.secretAccessKey,
        #                         region_name=appConfig.region)
        # file = session.resource('s3').Bucket(appConfig.bucket).download_file('tasmax.csv', "data_files/")

        s3 = boto3.client('s3', aws_access_key_id=appConfig.accessKeyId,
                      aws_secret_access_key=appConfig.secretAccessKey,
                      region_name=appConfig.region)
        s3.download_file(appConfig.bucket, 'data_files/tasmax.csv', 'test_two.csv')
        print(file)
        return pd.read_csv('data_files/tasmax.csv', usecols=range(5))

    def _clean_data(self):
        """
        Loads in data _load_data function
        Drops irrelevant columns, renames columns to more appropriate names, strips from leading spaces from strings,
        removes data for years prior to 2008 as world happiness dataset only goes back to 2008
        Takes average over year for each country (the month column is lost in this process)

        :returns cleaned dataset:
        """
        df_temp = self._load_data()
        df_temp = df_temp.drop(columns=[' ISO3'])
        df_temp = df_temp.rename(columns={' Year': 'year',
                                          ' Statistics': 'month',
                                          'tasmax': 'max_temp',
                                          ' Country': 'country'})
        df_temp['country'] = df_temp['country'].str.lstrip()
        df_temp = df_temp[df_temp['year'] >= 2008]
        df_temp = df_temp.groupby(['year', 'country']).mean().reset_index()
        return df_temp.reset_index()

    def temp_map(self):
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


temperature = Temperature()
print(temperature.df)
temperature.temp_map()
