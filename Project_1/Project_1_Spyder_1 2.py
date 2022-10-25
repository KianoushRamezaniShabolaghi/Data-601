#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:00:21 2022

@author: bj45613
"""

# This code:
# when you run this code a folder for figures (Pics) and a folder 
# for .csv files (CSV) is created 












import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
import datetime
# some infprmation about data analyzed:
# the data are for 6 month from January to June Excalty 181 days)
# This line calculates the execution time of code
import time
# Grab Currrent Time Before Running the Code
start = time.time()
import os
# os.mkdir('./Pics')
import os
import shutil
import sys

dir = 'Pics'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
dir = 'CSV'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)


#%%
##################################
# print the size of the file
from pathlib import Path
 
# open file
Path(r'uber-raw-data-janjune-15.csv').stat()
 
# getting file size
file=Path(r'uber-raw-data-janjune-15.csv').stat().st_size
print("Size of file is :", file, "bytes")


################################
# read The .csv file and prints its first 5 lines

df = pd.read_csv("uber-raw-data-janjune-15.csv")
print(df.head()) 




# delete thoese rows with NaN data
print(df.shape)
Initial_rows = df.shape[0]


df.dropna(axis=0, inplace=True)
print(df.shape)
Final_rows = df.shape[0]
print("\nThere were " + str(Initial_rows - Final_rows) + " rows that had NaN data")



print("Hello World")

# checking if we have any duplicated row
# keep first duplicate row
result_df = df.drop_duplicates()
print(result_df.shape)
print(df.shape)
print("\nThe total number of duplicated rows which are deleted are equal to: " + str(df.shape[0] - result_df.shape[0]))





#%%
##############################

print(df['Dispatching_base_num'].head())

##############################
# splitting from this website:
#.   https://www.skytowner.com/explore/splitting_strings_based_on_space_in_pandas_dataframe
# or https://www.geeksforgeeks.org/split-a-text-column-into-two-columns-in-pandas-dataframe/




# the Pickup_date is spliited into two new columns: Pickup_Day and Pickup_Hour
# now the dataframe has two new columns
df[['Pickup_Day','Pickup_Hour']] = df.iloc[:, 1].str.split(' ', expand=True)
# df[['Pickup_date','Pickup_one']] = df.Dispatching_base_num.str.split(expand=True)
df.head(5)
##############################


# print the name of the columns
df.columns

#%%
##############################
# dof = df.groupby(['Dispatching_base_num','locationID']).size().reset_index(name='count’)
# print(dof)
# Reset indexes after removing rows with NaN value
# print(df.index)
df = df.reset_index()
# print(df.index)

##############################
print("Different locationID's and their frequency: ")
print(df['locationID'].value_counts())

print("The locationID with the maximmum frequency is: ")
print(df['locationID'].value_counts().idxmax())


print("Different Dispatching_base_num's and their frequency: ")
print(df['Dispatching_base_num'].value_counts())
print("The Dispatching_base_num with the maximmum frequency is: ")
print(df['Dispatching_base_num'].value_counts().idxmax())
print("Different Affiliated_base_num's and their frequency: ")
print(df['Affiliated_base_num'].value_counts())

##############################
# another method for most repeated value in a column :
print("\nthe Dispatching_base_num with the highest count is: ")
print(df.Dispatching_base_num.mode())
print("\nthe locationID with the highest count is: ")
print(df.locationID.mode())
print("\nthe Pickup_Day with the highest count is: ")
print(df.Pickup_Day.mode())

#%%
##############################
# adding a new column (day_of_week) which shows the day of the week (Monday, Tuesday ...)
df['day_of_week'] = df['Pickup_Day'].astype('datetime64').dt.day_name()
print('\nthe new columns titles: ')
print(df.columns)


print("\nQuestion: Which three dates have the highest traffic? Which days (Mon, Tue?) were these (find this programmatically")
print(df['Pickup_Day'].value_counts().nlargest(3))



# we create a list that contains the three days which have the highest traffic
list = df['Pickup_Day'].value_counts()[:4].index.tolist()
# The following code shows the week days whith the highest traffic
print("\nThe Days of the week with highest traffic: ")
for i in range(3): 
    df2 = df.loc[df['Pickup_Day'] == list[i], 'day_of_week'].iloc[0]
    print(df2)


# the codes is taken from this website:
#     https://sparkbyexamples.com/pandas/pandas-extract-column-value-based-on-another-column/
#%%
##############################
print("\nQuestions is:  Summarize data per day (eliminate time) and plot the number of pickups per day. If days are too many, summarize per week. ")
print(df.head())
# Thereafter we create a dataframe (dfdates) which contains dates and their frequency
dfdates = pd.DataFrame()    # it is necessary to firstly define an empty dataframe

# this is each day
dfdates['Days']= df['Pickup_Day'].value_counts()[:181].index


# this is the frequency of each Day
dfdates['traffic'] = df['Pickup_Day'].value_counts()[:181].tolist()
print(dfdates.head())
print(dfdates.shape)
print(dfdates.columns)


# del dfdates['Frequency']
# Sorting dataframe of dfdates based on dates
print('Sorting dataframe of dfdates based on dates: ')
dfdates = dfdates.sort_values(by='Days', ascending=True)
dfdates = dfdates.reset_index()
print('\nThe new dfdates dataframe contains days, their traffic and week number')
print(dfdates.head())


# plot days versus their traffic
# import matplotlib.pyplot as plt
# print('Plot Days versus their Traffic')
# plt.scatter(dfdates['Days'], dfdates['traffic'], c ="blue")
# plt.show()

print('\nBecause there are too many Days we use weeks instead: ')
import datetime
# dfdates['Week'] = dfdates['Days'].dt.isocalendar().week

# converting the 2015-01-01 into separate day, month and year numbers
dfdates['year'] = pd.DatetimeIndex(dfdates['Days']).year
dfdates['month'] = pd.DatetimeIndex(dfdates['Days']).month
dfdates['day'] = pd.DatetimeIndex(dfdates['Days']).day




import numpy as np
dfdates["week"] = np.nan  # create a NaN column named week
# print(dfdates.head(20))
for i in range(len(dfdates['Days'])):
    dfdates['week'][i]= datetime.date(dfdates['year'][i], 
                                  dfdates['month'][i], dfdates['day'][i]).isocalendar()[1]
# this last 1 is for week if put 0 it prints year and if 2 then month
                                                                                       


print('\nPlot Days versus their Traffic')
dfweeks = pd.DataFrame() 
# producing an array of sums per week
array = dfdates.groupby(['week']).sum()   
# converting that array into a framework
dfweeks=pd.DataFrame(array)
print(dfweeks)
print(dfweeks['traffic'])
print(dfweeks.index)
print('\nPlot days versus their Traffic')
plt.scatter(dfdates.index, dfdates['traffic'], c ="blue")
plt.xlabel('Day')
plt.ylabel('Traffic')
plt.savefig('./Pics/Traffic_of_each_day.png')
plt.show()

print('\nBecause the days of week 1 and week 27 (last week) are not complete their values deviate from the rest values')

correcteddfweeks = dfweeks.iloc[1: 26, :]   # removes rows 0 and 27
print(correcteddfweeks)
print('\nPlot weeks versus their Traffic')
#%%
##############################

print('\nBecause there are too many Days we use weeks instead')
print('          Plot weeks versus their Traffic')
# every time you run generates a new color 
col = (np.random.random(), np.random.random(), np.random.random())
plt.scatter(correcteddfweeks.index, correcteddfweeks['traffic'], c =col)
plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.legend(fontsize=12) 
plt.xlabel('week')
plt.ylabel('traffic')
plt.title('              weeks versus their Traffic')
# from mlxtend.plotting import category_scatter
plt.savefig('./Pics/weeks_versus_their_Traffic.png')
plt.show()



print('                \nPlot weeks versus their Traffic')
# Different colors for differnt points
plt.scatter(correcteddfweeks.index, correcteddfweeks['traffic'], c=np.random.rand(len(correcteddfweeks.index),3))
plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.xlabel('week')
plt.ylabel('traffic')
plt.title('weeks_versus_their_Traffic') 
# from mlxtend.plotting import category_scatter
plt.savefig('./Pics/weeks_versus_their_Traffic.png')
plt.show()



#%%
##########################
# # Uncomment the following (it will work individually not with the rest of code)
# print('                Plot different days of weeks versus their Traffic')
# import matplotlib.pyplot as plt
# dfcolors = pd.DataFrame() 
# cmap = matplotlib.cm.get_cmap('Spectral_r')

# print('we will generate a dictionary for colors')
# dfcolors = pd.Series({k:cmap(np.random.rand()) for k in dfdates['traffic']})
# dfcolors.columns = 'color_dict'
# dfdates.plot.scatter(x='week',\
#                      y='traffic', c=dfcolors);

# plt.xlabel('week days')
# plt.ylabel('traffic')
# plt.title('week days versus their Traffic') 
# plt.show()

#%%
# print('                Plot different days of weeks versus their Traffic')
# import matplotlib
# cmap = matplotlib.cm.get_cmap('Spectral_r')
# print('we will generate a dictionary for colors')
# color_dict = pd.Series({k:cmap(np.random.rand()) for k in dfdates['week'].unique()})
# color_dict.name = 'color_dict'
# dfdates = pd.merge(dfdates, color_dict, how='left', left_on='week', right_index=True)
# dfdates.plot.scatter(x='week',\
#                      y='traffic', c='color_dict');

# plt.xlabel('week days')
# plt.ylabel('traffic')
# plt.title('week days versus their Traffic') 
# plt.show()



#%%
##############################
# import matplotlib
# cmap = matplotlib.cm.get_cmap('Spectral_r')
# color_dict = pd.Series({k:cmap(np.random.rand()) for k in dfweeks.index.unique()})
# color_dict.name = 'color_dict'
# dfweeks = pd.merge(dfweeks, color_dict, how='left', left_on=dfweeks.index, right_index=True)
# dfweeks.plot.scatter(x=dfweeks.index,\
#                      y='traffic', c='color_dict');
# plt.show()


# Website:
#    https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column

print('\nMethod 2: converting Days to weeks programmatically: ')

# Finding the number of days in each month
print('\n        Finding the number of days in each month')
print(dfdates['month'].unique())
dfdates.loc[dfdates.groupby(['month'])['day'].idxmax()]


# a program to obtain date number of each month
dfdates["week_number"] = np.nan 
week_number = 0

for i in range(181):
    if dfdates.index[i] % 7 == 0:
        week_number += 1
        dfdates["week_number"][i]=week_number
    else:
        dfdates["week_number"][i]=week_number



#%%
###############################
print('\nQuestion: # Is there an Affiliated_base_num which has some interesting statistics \
(most people visit it on a certain day of the week?)')


y = df["Affiliated_base_num"].astype("category").value_counts()
print('\nAffiliated_base_num and their frequency are: ')
print(y)

print('\n             The Affiliated_base_num with the highest number of frequency is: ')
print(df["Affiliated_base_num"].astype("category").value_counts()[0])


print('\n             Most people visit at these days: ')
list1 = df['day_of_week'].value_counts().nlargest(7)
print(list1)



print('\n              Plot of weeek days and their pickup rate: ')

list2 = df['day_of_week'].value_counts().index.tolist()[:7]
print(list2)


  
fig= plt.figure(figsize = (20, 10))
 
# creating the bar plot
plt.bar(list2, list1,  color=['black', 'red', 'green', 'blue', 'cyan', 'maroon', 'yellow'],
        width = 0.4)


fig, ax = plt.subplots()
bars = ax.barh(list2, list1)

ax.bar_label(bars)



plt.xlabel("Days of the week")
plt.ylabel("Pickup per day")
plt.title("Days' traffic")
plt.savefig('./Pics/Days_traffic.png')
plt.show()


# Pi chart
print('Pi chart: ')
plt.pie(list1)
myexplode = [0.2, 0, 0, 0, 0, 0, 0]
plt.pie(list1, labels = list2, explode = myexplode, shadow = True)
plt.title("Days' traffic")
plt.savefig('./Pics/Days_traffic_pi_chart.png')
plt.show() 
#%%
print('\n The days and their traffic: ')

x = df['Pickup_Day'].value_counts().index.tolist()[:3]
y = df["Pickup_Day"].astype("category").value_counts()[:3]
markersize = 400
plt.scatter(x, y, c ="green", s=markersize)
plt.xlabel("Dates")
plt.ylabel("Pickup per day")
plt.title("Days with highest traffic")
plt.savefig('./Pics/Days_with_highest_traffic.png')
plt.show()





x = df['Pickup_Day'].value_counts().index.tolist()[:3]
y = df["Pickup_Day"].astype("category").value_counts()[:3]
markersize = [i/200 for i in y]
plt.scatter(x, y, c ="red", s=markersize)
plt.xlabel("Dates")
plt.ylabel("Pickup per day")
plt.title("Days with highest traffic")
plt.savefig('./Pics/Days_with_highest_traffic_red.png')
plt.show()

#%%
aa = df['Dispatching_base_num'].unique()
print(aa)
df.shape
# df.groupby('Dispatching_base_num').to_csv('34.csv')



week_grouped = df.groupby('Dispatching_base_num')
# week_grouped.to_csv('66.csv')
week_grouped.sum().reset_index().to_csv('./CSV/55.csv'






















#%%
# Grab Currrent Time After Running the Code
end = time.time()
#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ str(total_time))




