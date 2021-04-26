import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load the data file for the totality of papers
data_total = pd.read_csv('data_per_country.csv',names=['Country','Total papers'])
# chech data frame from pandas
print(data_total)
# plot the bar with matplotlib
ax = data_total.plot(kind='bar',x='Country',y='Total papers',logy=True,legend=False,ylim=(1,1000),figsize=(12,6), fontsize=14)
ax.set_ylabel('Total number of papers', fontsize=14)
ax.set_xlabel('', fontsize=1)
plt.savefig('Total_papers.pdf',bbox_inches="tight")
plt.show()
# the others pie plot
other_pie = {'Dominican Republic':5, 'El Salvador':6, 'Guatemala':23, 'Honduras':9, 'Jamaica':24, 'Nicaragua':14, 'Panama':17}
df = pd.Series(other_pie, name='Other countries')
print(df)
df.plot.pie(figsize=(6,6), colormap='tab20b', autopct="%.1f%%", fontsize=14)
plt.axes().set_ylabel('')
plt.savefig('Others.pdf',bbox_inches="tight")
plt.show()

# *******************Next plot****************
# grabbing data per year of every country
data_costa_rica_year = pd.read_csv('data_per_year_costa_rica.csv',names=['year','Costa Rica'])
data_guatemala_year = pd.read_csv('data_per_year_guatemala.csv',names=['year','Guatemala'])
data_puerto_rico_year = pd.read_csv('data_per_year_puerto_rico.csv',names=['year','Puerto_Rico'])
data_cuba_year = pd.read_csv('data_per_year_cuba.csv',names=['year','Cuba'])
data_jamaica_year = pd.read_csv('data_per_year_jamaica.csv',names=['year','Jamaica'])
data_arecibo_year = pd.read_csv('data_per_year_arecibo.csv',names=['year','Arecibo'])
data_el_salvador_year = pd.read_csv('data_per_year_el_salvador.csv',names=['year','El_Salvador'])
data_honduras_year = pd.read_csv('data_per_year_honduras.csv',names=['year','Honduras'])
data_nicaragua_year = pd.read_csv('data_per_year_nicaragua.csv',names=['year','Nicaragua'])
data_dominicana_year = pd.read_csv('data_per_year_dominicana.csv',names=['year','Dominicana'])
data_panama_year = pd.read_csv('data_per_year_panama.csv',names=['year','Panama'])
# checking the total number
total_cr = data_costa_rica_year['Costa Rica'].sum()
total_cuba = data_cuba_year['Cuba'].sum()
total_puerto_rico = data_puerto_rico_year['Puerto_Rico'].sum()
total_arecibo = data_arecibo_year['Arecibo'].sum()
# others data frame
other_data = data_guatemala_year.assign(El_Salvador=data_el_salvador_year.El_Salvador, Honduras=data_honduras_year.Honduras, Nicaragua=data_nicaragua_year.Nicaragua, Panama=data_panama_year.Panama, Dominicana=data_dominicana_year.Dominicana)

other_data["others"] = other_data['El_Salvador'] + other_data['Honduras'] + other_data['Nicaragua'] + other_data['Panama'] + other_data['Dominicana']
print other_data

data_year = data_costa_rica_year.assign(Cuba=data_cuba_year.Cuba, Puerto_Rico=data_puerto_rico_year.Puerto_Rico)
data_year.rename({'Puerto_Rico': 'Puerto Rico'}, axis=1, inplace=True)
data_year['Others'] = other_data.others
#data_year['Smoothed'] = [0, (33 + 52 + 24)/3., 0, 0, (32 + 17 + 10)/3., 0, 0, (19 + 23 + 27)/3., 0, 0, (21 + 40 + 36)/3., 0, 0, (30 + 40 + 29)/3., 0, 0, (52 + 59 + 59)/3., 0, 0, (58 + 68 + 66)/3., 0, 0, (54 + 46 + 64)/3., 0, 0, (48 + 61 + 35)/3., 0, 0, (42 + 53 + 56)/3., 0, 0]
print data_year
data_year['year'] = data_year['year'].astype("string")
# time to plot the year growth
fig, ax = plt.subplots(figsize=(12,8))


#ax = plt.gca()

#data_year.plot(x='year', y='Smoothed', kind='line', ax=ax)
data_year.plot.bar(x='year',y=['Costa Rica','Cuba','Puerto Rico', 'Others'], colormap='Paired', stacked=True,  ax=ax, fontsize=14)


#def splitSerToArr(ser):
#    return [ser.index, ser.as_matrix()]

# I am going to try to a bin to see what the trends are for the years
i = 0
#x_array = np.zeros(10)
#for i in range(0, 10):
#    x_array[i] = 1991 + i*3
#x_array = np.array([1991,1994,1997,2000,2003,2006,2009,2012,2015,2018])
x_array = ["1990","1991","1992","1993","1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002","2003","2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]

#y_array = np.array([np.nan, (33 + 52 + 24)/3., np.nan, np.nan, (32 + 17 + 10)/3., np.nan, np.nan, (19 + 23 + 27)/3., np.nan, np.nan, (21 + 40 + 36)/3., np.nan, np.nan, (30 + 40 + 29)/3., np.nan, np.nan, (52 + 59 + 59)/3., np.nan, np.nan, (58 + 68 + 66)/3., np.nan, np.nan, (54 + 46 + 64)/3., np.nan, np.nan, (48 + 61 + 35)/3., np.nan, np.nan, (42 + 53 + 56)/3., np.nan, np.nan])
y_array = np.array([33, 52, 24, 32, 17, 10, 19, 23, 27, 21, 40, 36, 30, 40, 29, 52, 59, 59, 58, 68, 66, 54, 46, 64, 48, 61, 35, 42, 53, 56, 37])
print('The years for binning: ',x_array)
print('The values: ',y_array)
print('Lengths: ', len(x_array), len(y_array))

for i in range(0,len(x_array)):
    if (i == 0 or i == len(x_array) - 1):
        y_array[i] = y_array[i]
    else:
        y_array[i] = (y_array[i-1] + y_array[i] + y_array[i+1]) / 3.

#s1 = pd.Series(y_array, index=x_array)
#ax.plot(*splitSerToArr(s1.dropna()), linestyle='-', marker='o',label=r'pau')

ax.plot(x_array,y_array,'-',lw=3,label=r'3-year moving average')
ax.set_ylabel('Number of papers per year per country', fontsize=14)
ax.set_xlabel(' ', fontsize=1)
ax.legend(loc="best", fontsize=14)
plt.savefig('Contribution_per_year.pdf',bbox_inches="tight")
plt.show()

print('The publication rate:', y_array)


print('The totals for the growth guys are: '+str(total_cr)+' for CR, '+str(total_cuba)+' for Cuba, '+str(total_arecibo)+' for arecibo, and '+str(total_puerto_rico)+' for PR')


data_puerto_rico_year.rename({'Puerto_Rico': 'Puerto Rico'}, axis=1, inplace=True)

ax = plt.gca()
#data_costa_rica_year.plot(kind='area',x='year',y='Costa Rica',ax=ax,figsize=(12,6))
#data_guatemala_year.plot(kind='line',x='year',y='Guatemala',color='magenta',ax=ax,figsize=(12,6))
#data_cuba_year.plot(kind='area',x='year',y='Cuba',color='yellow',ax=ax,figsize=(12,6), alpha=0.6)
#data_jamaica_year.plot(kind='line',x='year',y='Jamaica',color='black',ax=ax,figsize=(12,6))
data_arecibo_year.plot(kind='area',x='year',y='Arecibo',color='cyan',ax=ax, alpha=0.4, fontsize=14)
data_puerto_rico_year.plot(kind='area',x='year',y='Puerto Rico',color='red',ax=ax, ylim=(0,60),figsize=(12,6),alpha=0.2, fontsize=14)
ax.legend(loc="best", fontsize=14)
#ax.set_title('Contribution of the Arecibo Observatory',fontsize=14)
ax.set_xlabel('year', fontsize=14)
ax.set_ylabel('Number of papers per year', fontsize=14)
plt.savefig('Arecibo.pdf',bbox_inches="tight")
plt.show()

