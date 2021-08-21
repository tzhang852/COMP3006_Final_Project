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
        self.temp_df = temperature.Temperature()
        self.happ_df = happiness.Happiness()

    def mean_max_temp(self):
        #plot mean max temp against average happiness for each country per year
        #bubble map
        #combine dataframe
        temp_happ_df = pd.concat([self.temp_df, self.happ_df], axis = 1)
        
        # fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
        #              hover_name="country", size="pop",
        #              projection="natural earth")
        # fig.show()
    
