import pandas as pd
import AppConfig
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import boto3
import argparse

class Happiness:
    def __init__(self):
        self.df = self._clean_data()

    def _load_data(self):
        """
        Forces 5 columns since some country names contain comma

        :returns dataframe built from weather dataset:
        """
        appConfig = AppConfig.AppConfig()
        # session = boto3.Session(aws_access_key_id=appConfig.accessKeyId,
        #                         aws_secret_access_key=appConfig.secretAccessKey)
        # file = session.resource('s3').Bucket(appConfig.bucket).download_file('WHR2021.csv', "data_files/")
        s3 = boto3.client('s3', aws_access_key_id=appConfig.accessKeyId,                       
                            aws_secret_access_key=appConfig.secretAccessKey,                       
                            region_name=appConfig.region)         
        s3.download_file(appConfig.bucket, 'data_files/WHR2021.csv', 'test_two.csv')
        return pd.read_csv('data_files/WHR2021.csv')

    def _clean_data(self):
        """
        Loads in data _load_data function
        Drops irrelevant columns, renames columns to more appropriate names, strips from leading spaces from strings,
        removes data for years prior to 2008 as world happiness dataset only goes back to 2008
        Takes average over year for each country (the month column is lost in this process)

        :returns cleaned dataset:
        """
        df_happiness = self._load_data()
        df_happiness = df_happiness.drop(columns=['Log GDP per capita','Social support',
                                                    'Healthy life expectancy at birth',
                                                    'Freedom to make life choices','Generosity',
                                                    'Perceptions of corruption','Positive affect',
                                                    'Negative affect'])
        print(df_happiness.columns)
        df_happiness = df_happiness.rename(columns={'Country name': 'country',
                                          'year': 'year',
                                          'Life Ladder': 'happiness'})
        #df_happiness['country'] = df_happiness['country'].str.lstrip()
        df_happiness = df_happiness[df_happiness['year']>=2008]
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
                            title='Happiness by countries from 2008 to 2020',
                            animation_frame="year")
        fig.update(layout_coloraxis_showscale=True)
        fig.show()

    def happiness_bar(self):
        """
        Displays a bar graph of happiness by countries in alphabetical order
        """
        current_year = self.df[self.df['year']==2020][:166]
        plt.rcParams['figure.figsize']=(30, 7)
        graph = sns.barplot(x = current_year['country'][:166], y = current_year['happiness'][:166])
        graph.set_xlabel(xlabel = 'Country', fontsize = 10)
        graph.set_ylabel(ylabel = 'Happiness Index', fontsize = 10)
        graph.set_title(label = 'Happiness by Country', fontsize = 20)
        plt.xticks(rotation = 90)
        plt.show()
    
def main():
    parser = argparse.ArgumentParser(description="Function for AutoMPG sorting")
    parser.add_argument('-p', '--plot', dest='plot', type = str, help = "Show Happiness by Country")
    args = parser.parse_args()

    happiness = Happiness()
    print(args)
    if args.plot:
        happiness.happiness_map()

