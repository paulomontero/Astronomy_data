import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load the data file for the totality of papers
data_total = pd.read_csv('data_per_country.csv',names=['Country','Total papers'])
# chech data frame from pandas
print(data_total)
# plot the bar with matplotlib
data_total.plot(kind='bar',x='Country',y='Total papers')
plt.savefig('Total_papers.pdf',bbox_inches="tight")
plt.show()

