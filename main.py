#data from:
# https://data.gov.uk/dataset/3e358499-eb65-4dde-9b08-9de6cac52efb/food-hygiene-ratings-website-traffic
#  2018 Food Hygiene Website Data

#packages used
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

file='food-hygiene-ratings-website-traffic-january-2018-to-december-2018.csv'

#import data
food_df = pd.read_csv(file)
#print(food_df)

#changing Date column to a proper date (rather than just a string)
food_df['Date'] = food_df['Date'].apply(lambda olddate: datetime.strptime(olddate, '%d/%m/%Y'))

#set date format to be displayed on x axis
date_format = DateFormatter("%b")


#set date to the index
food_df.set_index('Date', inplace=True, drop=True)
print(food_df)

#summary values
print('Minimum Value: ' , food_df['Visits'].min() , 'visits on' , food_df['Visits'].idxmin().strftime("%a %d %b") +'.')
print('Maximum Value: ' , food_df['Visits'].max() , 'visits on' , food_df['Visits'].idxmax().strftime("%a %d %b") +'.')
print('Mean Value: ' , round(food_df['Visits'].mean()) , 'visits.')

#plotting data

#setting figures and axes
fig, ax = plt.subplots()

 #give an x axis tick for every month
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

ax.plot(food_df.index, food_df['Visits'])

ax.xaxis.set_major_formatter(date_format) #display dates in this format
plt.xticks(rotation=90)
ax.set_xlabel('Date')
ax.set_ylabel('No. of Visits Per Day')
ax.set_title('Food Hygiene Ratings Website Visits (2018)')

#2nd plot
#ax.plot(food_df.index, food_df['Pageviews'])


plt.show()

#summary figures eg lowest day, avg etc
print('Minimum Value: ' + food_df.min())