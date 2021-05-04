import requests
from bs4 import BeautifulSoup

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
print(items)