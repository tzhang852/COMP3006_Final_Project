import pandas as pd
import AppConfig
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import boto3
import argparse
import happiness
import temperature


class Analysis:
    def __init__(self):
        self.temp_df = temperature.Temperature().df
        self.happy_df = happiness.Happiness().df
        self.temp_happy_df = self._clean_data()

    def _clean_data(self):
        """
        normalizes country names so that their names are in the exact same format so merge works
        Merges the two data frames into a single dataframe
        :returns cleaned and normalized dataset:
        """
        temp_happy_df = (self.happy_df.merge(self.temp_df, on=['country', 'year'], how='inner'))
        # normalize
        temp_happy_df['happiness'] = temp_happy_df['happiness'] / max(temp_happy_df['happiness'])
        #temp_happy_df.to_csv("testing3.csv")
        return temp_happy_df

    def mean_max_temp(self):
        """
        Plots mean max temp against average happiness for each country per year
        using bubble heat map
        heat color goes off of temperature
        bubble size goes off happiness
        """
        fig = px.scatter_geo(self.temp_happy_df, locations="country", locationmode='country names',
                             color="max_temp", hover_name='country', size="happiness", size_max=30,
                             animation_frame='year', projection="natural earth")
        fig.show()
        
    def scatter(self):
        """
        Comments go here
        """
        x_1 = self.temp_happy_df["max_temp"]
        y_2 = self.temp_happy_df["happiness"]
        m, b = np.polyfit(x_1, y_2, 1)
        plt.scatter(x_1, y_2, marker='o')
        plt.plot(x_1, m*x_1 + b, color='red')
        plt.savefig("maxtemp.png")
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Analysis")
    parser.add_argument('-p', '--plot', choices=['maxtemp'], help="Display bubble map by country" +
                                                                  " using mean maximum temperature and happiness")
    # parser.add_argument('-t', '--temperature', choices=range(2008,2020), help="Display bubble map by country" +
    #                                                               " using mean maximum temperature and happiness")
    # parser.add_argument('-a', '--happiness', choices=['maxhappiness','minsadness'], help="Display bubble map by country"+
    #                                                                " using mean maximum temperature and happiness")
    #parser.add_argument('-p', '--plot', choices=['maxtemp'], help="Display bubble map by country" +
                                                                  #" using mean maximum temperature and happiness")
    
    # parser.add_argument('-')
    args = parser.parse_args()

    perusal = Analysis()
    print(args)
    if args.plot == 'maxtemp':
        perusal.scatter()


if __name__ == "__main__":
    main()
