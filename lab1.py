
import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('AQI_Data.csv')

# Display the first few rows of the dataframe
print(df.head())

# Display the first 8 rows of the dataframe
print("\nDisplay the first 8 rows:")
print(df.head(8))

# Display the last 5 rows of the dataframe
print("\nDisplay the last 5 rows:")
print(df.tail(5))

# Show the dtype and number of non-null values for each column
print("\nShow the dtype and number of non-null values for each column:")
print(df.info())

# Use numpy to compute the mean AQI, max PM2.5, and min PM10 values for each city
print("\nUse numpy to compute the mean AQI, max PM2.5, and min PM10 values for each city:")
result = df.groupby('City').agg(
    mean_aqi=('AQI', 'mean'),
    max_pm25=('PM2.5', 'max'),
    min_pm10=('PM10', 'min')
).reset_index()

# Display the result
print(result)

# If you want to see the mean AQI of each city specifically
print("\nThe mean AQI of each city is:")
print(result[['City', 'mean_aqi']])

#the maximum value of PM2.5 in each city
print("\nThe maximum value of PM2.5 in each city is:")
print(result[['City', 'max_pm25']])

# Sort the result by mean AQI in descending order
sorted_result = result.sort_values(by='mean_aqi', ascending=False)

# Display the sorted result
print("\nSorted result by mean AQI in descending order:")
print(sorted_result)






