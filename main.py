import argparse
import happiness
import analysis
import temperature


def main():
    parser = argparse.ArgumentParser(description="Happiness, Temperature, and Analysis arguments")
    parser.add_argument('-a', '--happyplt', choices=['heatmap', 'bar'], help="Initial data exploration " +
                                                                             "for happiness data")
    parser.add_argument('-b', '--tempplt', choices=['heatmap', 'blah'], help="Initial data exploration" +
                                                                             "for temperature data")
    parser.add_argument('-c', '--csv', choices=['happy', 'temp', 'analysis'], help="Download csv of" +
                                                                                   "happiness, temperature, or analysis")
    parser.add_argument('-d', '--analysis', choices=['bubble', 'min'], help="Displays a bubble graph of" +
                                                                            "all countries based on temperature" +
                                                                            "and happiness")
    parser.add_argument('-mh', '--mosthot', type=int, dest='nhottest', help="show the n most hot countries in asc.")
    parser.add_argument('-lh', '--leasthot', type=int, dest='nleasthot',
                        help="show the n most least hot countries in asc.")
    parser.add_argument('-mp', '--mosthappy', type=int, dest='nhappiest',
                        help="show the n most happy countries in asc.")
    parser.add_argument('-lp', '--leasthappy', type=int, dest='nleasthappy',
                        help="show the n most least happy countries in asc.")
    parser.add_argument('-y', '--year',
                        choices=['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                                 '2019', '2020'],
                        help="value to let user piuck year for mh, lh, mp, lp commands")

    args = parser.parse_args()

    happy = happiness.Happiness()
    happy_df = happiness.Happiness().df
    temp = temperature.Temperature()
    temp_df = temperature.Temperature().df
    perusal = analysis.Analysis()
    # perusal_df = analysis.Analysis().df
    print(args)

    # Initial Data exploration arguments for happiness
    if args.happyplt == 'heatmap':
        happy.happiness_map()
    elif args.happyplt == 'bar':
        happy.happiness_bar()

    # Initial Data exploration arguments for temperature
    if args.tempplt == 'heatmap':
        temp.temp_map()
    elif args.tempplt == 'blah':
        print("show second graph here")

    # Download csv of happiness, temperature, and analysis data
    if args.csv == 'happy':
        happy_df.to_csv("happiness.csv", index=False)
    if args.csv == 'temperature':
        temp_df.to_csv("temperature.csv", index=False)
    # if args.csv == 'analysis':

    # Analysis displaying possible happiness and temperature correlation
    if args.analysis == 'bubble':
        perusal.mean_max_temp()

    if args.nhottest and args.nhottest > 0:
        print(temp.top_n_hottest_countries(args.nhottest, args.year))
    if args.nleasthot and args.nleasthot > 0:
        print(temp.top_n_coldest_countries(args.nleasthot, args.year))
    if args.nhappiest and args.nhappiest > 0:
        print(happy.top_n_happiest_countries(args.nhappiest, args.year))
    if args.nleasthappy and args.nleasthappy > 0:
        print(happy.top_n_saddest_countries(args.nleasthappy, args.year))
