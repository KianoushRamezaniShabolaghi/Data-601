#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:09:31 2022

@author: bj45613
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sat Oct 22 11:00:21 2022

@author: bj45613
Kianoush Ramezani Shabolaghi
Contact: bj45613@umbc.edu
+1 443 527 8882


# About this code:
    
#  I wrote this code and runned this file by Spyder IDE which I think maybe has some 
# notations that differs from other IDE's or Jupyrt, if the file doesnt work please 
# let me know, because I tested it and it works properly on my Spyder.
# The reason that I used Spyder is because My Jupyter notebook cannot read the whole .csv file 
# which I was not able to solve

# The Questions are determined by 'Question' at the beggining of line in the comments 
# Though I tried to explore more than answering the specified Questions


# please put the 'uber-raw-data-janjune-15.csv' file in the working directory

# when you run this code a folder for figures (Pics) and a folder 
# for .csv files (CSV) are created and some data are shown by them.

# Except these folders you can check three new dataframes created (dfdates, dfweeks, and dfmonths)
# each of them summurizes and categorized the outputs

# I also printed out some useful notes in the console which will help to undrestand 
# The code's each step

# Some useful notes are in the code body to explain what we want to do in each section


# some information about data analyzed:
# the data are for 6 month from January to June Excalty 181 days)

'''




import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import time
# This line calculates the execution time of code
# Grab Currrent Time Before Running the Code
start = time.time()
import os
# os.mkdir('./Pics')
import os
import shutil
import sys


# creating Pics and CSV folders
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

# checking if we have any duplicated row and remove them
# keep first duplicate row
result_df = df.drop_duplicates()
print(result_df.shape)
print(df.shape)
print("\nThe total number of duplicated rows which are deleted are equal to: " + str(df.shape[0] - result_df.shape[0]))


###############################
#%%
# Some general information about data:
print('Data Types are: \n')
print(df.dtypes)

print('\nData shape is: \n')
print(df.shape)

print('Data has ' + str(df.shape[0])+ ' Columns and ' + str(df.shape[1]) + ' Rows'  )

#%%
##############################
# splitting the Pickup_date to two columns: Pickup_Day and Pickup_Hour
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
print(df.columns)

#%%
# Question: Summarize data (df.groupby) by Dispatching_base_num and locationID. 
newdf = df.groupby(['Dispatching_base_num','locationID']) 
print(newdf.head())


#%%
##############################
# reset the indexes after the above processes
df = df.reset_index()

##############################
print("Different locationID's and their frequency: ")
print(df['locationID'].value_counts())


# Question:Which locationID has the highest count?
print("The locationID with the maximmum frequency is: ")
print(df['locationID'].value_counts().idxmax())

# Question: How many dispatching_bases are there?
print("Different Dispatching_base_num's and their frequency: ")
print(df['Dispatching_base_num'].value_counts())
print('\nHow many dispatching_bases are there:')
print(df['Dispatching_base_num'].value_counts().size)

# Question: Which Dispatching_base_num  appeared maximum time?
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
# Adding a new column (day_of_week) which shows the day of the week (Monday, Tuesday ...)
df['day_of_week'] = df['Pickup_Day'].astype('datetime64').dt.day_name()
print('\nthe new columns titles: ')
print(df.columns)


print("\nQuestion: Which three dates have the highest traffic? Which days (Mon, Tue?) were these (find this programmatically")
print(df['Pickup_Day'].value_counts().nlargest(3))



# Question: Which three dates have the highest traffic? Which days (Mon, Tue?) 
# were these (find this programmatically). 
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
# Question: Summarize data per day (eliminate time) and plot the number of pickups per day. If days are too many, summarize per week.
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


# Sorting dataframe of dfdates based on dates
print('Sorting dataframe of dfdates based on dates: ')
dfdates = dfdates.sort_values(by='Days', ascending=True)
dfdates = dfdates.reset_index()
print('\nThe new dfdates dataframe contains days, their traffic and week number')
print(dfdates.head())


# plot days versus their traffic

print('\nBecause there are too many Days we use weeks instead: ')
import datetime
# dfdates['Week'] = dfdates['Days'].dt.isocalendar().week

# converting the 2015-01-01 into separate day, month and year numbers
dfdates['year'] = pd.DatetimeIndex(dfdates['Days']).year
dfdates['month'] = pd.DatetimeIndex(dfdates['Days']).month
dfdates['day'] = pd.DatetimeIndex(dfdates['Days']).day




import numpy as np
dfdates["week"] = np.nan  # create a NaN column named week
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
print('\n The new dfweeks dataframe is: ')
print(dfweeks)
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
# Question: Summarize data per day (eliminate time) and plot the number of pickups per day. If days are too many, summarize per week.
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
# Failed attempts:
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
# Failed attempts:
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
# Failed attempts:
# import matplotlib
# cmap = matplotlib.cm.get_cmap('Spectral_r')
# color_dict = pd.Series({k:cmap(np.random.rand()) for k in dfweeks.index.unique()})
# color_dict.name = 'color_dict'
# dfweeks = pd.merge(dfweeks, color_dict, how='left', left_on=dfweeks.index, right_index=True)
# dfweeks.plot.scatter(x=dfweeks.index,\
#                      y='traffic', c='color_dict');
# plt.show()

#%%
# Summarize data per day (eliminate time) and plot the number of pickups per day.
# If days are too many, summarize per week. 

# Method 2: Converting Days to weeks programmatically:

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
# Question: Is there an Affiliated_base_num which has some interesting statistics
# (most people visit it on a certain day of the week?)')

print('\nQuestion: # Is there an Affiliated_base_num which has some interesting statistics \
(most people visit it on a certain day of the week?)')


y = df["Affiliated_base_num"].astype("category").value_counts()
print('\nAffiliated_base_num and their frequency are: ')
print(y)

print('\n The Affiliated_base_num with the highest number of frequency is: ')
print(df["Affiliated_base_num"].astype("category").value_counts()[0])

# Question: most people visit it on a certain day of the week?
print('\n Most people visit at these days respectively: ')
list1 = df['day_of_week'].value_counts().nlargest(7)
print(list1)



print('\n   Plot of weeek days and their pickup rate: ')

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
# Question: Plotting days and their traffic
print('\n The days and their traffic: ')

# x = df['Pickup_Day'].value_counts().index.tolist()[:3]
# y = df["Pickup_Day"].astype("category").value_counts()[:3]
# markersize = 400
# plt.scatter(x, y, c ="green", s=markersize)
# plt.xlabel("Dates")
# plt.ylabel("Pickup per day")
# plt.title("Days with highest traffic")
# plt.savefig('./Pics/Days_with_highest_traffic.png')
# plt.show()





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
# Question: # Question: Plotting months and their traffic
# This cell will calcualte the months and their traffic and plot them

# converting months number to their names (January, Febreuary, ...)
print('Converting months number to their names (January, Febreuary, ...')
import calendar
dfdates['month_name'] = dfdates.month.apply(lambda x: calendar.month_abbr[x])





print('\n The Months and their traffic: ')
dfmonth = dfdates.groupby(['month_name']).sum()
dfmonth = dfmonth.sort_values(by='month_name', ascending=True)
print('Pi chart: ')
list_3 = dfmonth.index.tolist()[:6]
print(list_3)
list_4 = dfmonth.traffic
plt.pie(list_4, labels = list_3, shadow = True)
plt.pie(list_4)
# plt.xlabel("Months")
# plt.ylabel("traffic")
plt.title("Months and their traffic")
plt.savefig('./Pics/Months_and_their_traffic.png')
plt.show()





#%%
# Summarizig Data in .CSV files
# this cell produces some .csv files in the CSV folder which contain 
# some information about the Data



# this is a numpy array:
# df["day_of_week"].unique()


df1 = df.groupby("day_of_week").head()
print(df1)
# df2 = df1.head(1000)
df1.to_csv('./CSV/grouped_by_day_of_week.csv')





# unique days of the week in the data
print('\n Unique days of the week in the data stored \
      in the Unique_days.csv file')
import csv
f = open('./CSV/Unique_days.csv', 'w')
writer = csv.writer(f)
writer.writerow(np.transpose(df["day_of_week"].unique()))
f.close()




print('\n Unique Dispatching_base_num and their frequency stored \
      in the Unique_Dispatching_base_num.csv file')
import csv
f = open('./CSV/Unique_Dispatching_base_num_frequency.csv', 'w')
writer = csv.writer(f)
writer.writerow(np.transpose(df["Dispatching_base_num"].unique()))
writer.writerow(df['Dispatching_base_num'].value_counts())
f.close()



print('\n Unique Pickup_Day and their frequency stored \
      in the Pickup_Day_frequency.csv file (Sorted based on Days)')
import csv
f = open('./CSV/Pickup_Day_frequency_sorted.csv', 'w')
writer = csv.writer(f)

writer.writerow(dfdates.Days)
writer.writerow(dfdates.traffic)
f.close()




print('\n  Weeks and their frequency stored \
      in the weeks_frequency.csv file (Sorted based on Days)')
import csv
f = open('./CSV/weeks_frequency.csv', 'w')
writer = csv.writer(f)
writer.writerow(dfweeks.index)
writer.writerow(dfweeks.traffic)
f.close()




print('\n Months and their frequency stored \
      in the month.csv file')
import csv
f = open('./CSV/month_frequency.csv', 'w')
writer = csv.writer(f)
writer.writerow(dfmonth.index)
writer.writerow(dfmonth['traffic'])
f.close()






#%%
# Grab Currrent Time After Running the Code
end = time.time()
#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ 'The total run time is: ' + str(int(total_time)) + ' seconds')




#%%




