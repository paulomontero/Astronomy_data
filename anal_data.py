import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load the data file for the totality of papers
data_total = pd.read_csv('data_per_country.csv',names=['Country','Total papers'])
# chech data frame from pandas
print(data_total)
# plot the bar with matplotlib
data_total.plot(kind='bar',x='Country',y='Total papers',logy=True,legend=False,title=r'Total number of papers per country',figsize=(12,6))
plt.savefig('Total_papers.pdf',bbox_inches="tight")
plt.show()
# *******************Next plot****************
# grabbing data per year of every country
data_costa_rica_year = pd.read_csv('data_per_year_costa_rica.csv',names=['year','Costa Rica'])
data_guatemala_year = pd.read_csv('data_per_year_guatemala.csv',names=['year','Guatemala'])
data_puerto_rico_year = pd.read_csv('data_per_year_puerto_rico.csv',names=['year','Puerto Rico'])
data_cuba_year = pd.read_csv('data_per_year_cuba.csv',names=['year','Cuba'])
ax = plt.gca()
data_costa_rica_year.plot(kind='line',x='year',y='Costa Rica',ax=ax,figsize=(12,6))
data_guatemala_year.plot(kind='line',x='year',y='Guatemala',color='magenta',ax=ax,figsize=(12,6))
data_cuba_year.plot(kind='line',x='year',y='Cuba',color='green',ax=ax,figsize=(12,6))
data_puerto_rico_year.plot(kind='line',x='year',y='Puerto Rico',color='red',ax=ax,title=r'Number of papers per year per country',figsize=(12,6))
plt.savefig('Growth.pdf',bbox_inches="tight")
plt.show()
