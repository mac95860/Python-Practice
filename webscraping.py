import pandas as pd
import requests
from bs4 import BeautifulSoup

#performs a get function and retrieves all the html from the url
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.103440000000035&lon=-94.58310999999998#.YIrEz5BKiUk')

#soup makes it easy to webscrape
soup = BeautifulSoup(page.content, 'html.parser')
# elements must be put in quotation marks
# print(soup.find_all('a'))

week = soup.find(id='seven-day-forecast-body')
# print(week)

# to access a class, you must call a class as class_
# print(week.find_all(class_ = 'tombstone-container'))
items = (week.find_all(class_ = "tombstone-container"))
# print(items[0])

# print(items[0].find(class_ = 'period-name').get_text())
# print(items[0].find(class_ = 'short-desc').get_text())
# print(items[0].find(class_ = 'temp').get_text())

period_name = [item.find(class_ = 'period-name').get_text() for item in items]
short_descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
temperatures = [item.find(class_ = 'temp').get_text() for item in items]
# print(period_name)
# print(short_descriptions)
# print(temperatures)

weather_stuff = pd.DataFrame({
    'period' : period_name,
    'short_descriptions' : short_descriptions,
    'temperatures' : temperatures
})

print(weather_stuff)

weather_stuff.to_csv('weather.csv')

