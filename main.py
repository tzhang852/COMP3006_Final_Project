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
import happiness
import analysis
import temperature

def main():
    parser = argparse.ArgumentParser(description="Happiness, Temperature, and Analysis arguments")
    parser.add_argument('-a', '--happy', choices=['heatmap', 'bar'], help="Initial data exploration " +
                                                                        "for happiness data")
    parser.add_argument('-b', '--temp', choices=['heatmap', 'blah'], help="Initial data exploration"+
                                                                        "for temperature data")
    parser.add_argument('-c', '--csv', choices=['happy', 'temp', 'analysis'], help="Download csv of"+
                                                                        "happiness, temperature, or analysis")
    parser.add_argument('-d', '--analysis', choices=['bubble', 'min'], help="Displays a bubble graph of"+
                                                                        "all countries based on temperature"+
                                                                        "and happiness")
    args = parser.parse_args()

    happy = happiness.Happiness()
    happy_df = happiness.Happiness().df
    temp = temperature.Temperature()
    temp_df = temperature.Temperature().df
    perusal = analysis.Analysis()
    #perusal_df = analysis.Analysis().df
    print(args)

    #Initial Data exploration arguments for happiness
    if args.happy == 'heatmap':
        happy.happiness_map()
    elif args.happy == 'bar':
        happy.happiness_bar()
    
    #Initial Data exploration arguments for temperature
    if args.temp == 'heatmap':
        temp.temp_map()
    elif args.temp == 'blah':
        print("show second graph here")

    #Download csv of happiness, temperature, and analysis data
    if args.csv == 'happy':
        happy_df.to_csv("happiness.csv", index = False)
    if args.csv == 'temperature':
        temp_df.to_csv("temperature.csv", index = False)
    #if args.csv == 'analysis':

    #Analysis displaying possible happiness and temperature correlation
    if args.analysis == 'bubble':
        perusal.mean_max_temp()

if __name__ == "__main__":
    main()
