# COMP 3006 Final Project (SU '21)
**Group Members**
- Ian Mckellar
- Tiffany Zhang

**Research Question**
- Using the Wiki Weather Dataset and World Happiness Index dataset, see if there is a correlation between the maximum temperature for a country and happiness.
- Hypothesis: The hotter a country is, the lower their Happiness Index

**Datasets**
- Dataset 1: Average World Temperature (1991-2020) [https://climateknowledgeportal.worldbank.org/download-data] this is a dataset containing the max temperature for each country each month, we are only utilizing the data from 2008 to 2020 as the other dataset only has data back to 2008
- Dataset 2: World Happiness Index (2008-2020) [https://worldhappiness.report/ed/2021/#appendices-and-data] this is a dataset that basically measures how happy each country is each year.  More information can be found here [https://worldhappiness.report/]

**How to run the program**
- To run type: python3 main.py
- List of command and a brief description
```
commands    description    

- -a    --happyplt      Initial data exploration for happiness data                                     
choices: heatmap, bar 
- -b    --tempplt       Initial data exploration for temperature data                                   
choices: heatmap, bubblemap
- -c    --csv           Download csv of happiness, temperature, or analysis                             
choices: happy, temp, analysis
- -d    --analysis      Displays a bubble graph of all countries based on temperature and happiness     
choices: bubble, min
- -mh   --mosthot       show the n most hot countries in asc.
- -lh   --leasthot      show the n most least hot countries in asc.
- -mp   --mosthappy     show the n most happy countries in asc.
- -lp   --leasthappy    show the n most least happy countries in asc.
- -y    --year          value to let user pick year for mh, lh, mp, lp commands                         
choices: any year between 2008 and 2020

Example:
python3 main.py -a heatmap -c analysis -mh 5 -y 2008
```

**Conclusion**
- With our brief analysis on countries and their average maximum temperature for the year we found no clear correlation that hotter countries are more unhappy nor did we find the inverse (that they more happy).  Further analysis could be done to prove this by taking into account other metrics in the world happiness report or by looking at the data regionally rather than by country.
