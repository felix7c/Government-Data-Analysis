#data from:
# https://data.gov.uk/dataset/3e358499-eb65-4dde-9b08-9de6cac52efb/food-hygiene-ratings-website-traffic
#  2018 Food Hygiene Website Data

import pandas as pd
import matplotlib.pyplot as plt

file='food-hygiene-ratings-website-traffic-january-2018-to-december-2018.csv'

#import data
food_df = pd.read_csv(file)
print(food_df)

#plotting data
plt.style.use("ggplot") #ggplot style

#setting figures and axes
fig, ax = plt.subplots()

ax.plot(food_df['Date'], food_df['Visits'])

ax.set_xlabel('Date')
ax.set_ylabel('No. of Visits Per Day')
ax.set_title('No of Page Visits Per Day')


plt.show()