import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
url = 'https://www.officeholidays.com/countries/india/2021'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
html_page = requests.get(url, headers=headers)
#print(html_page.content)
soup = BeautifulSoup(html_page.text, "html.parser")
#title = soup.find('title')
#title = soup.find('title').get_text()
#print(soup.title)
#title = soup.find("div", id='new-arrivals')
#title = soup.find("div", class_='twelve columns')[2].find('h2')
#holiday_list = soup.findAll('div', )
holiday_list = soup.find('table', class_='headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
')
#for Day in holiday_list.findAll('tbody'):
 #   rows = Day.findAll('tr')
  #  for row in rows:
   #     holiday_Day = row.find('tr', class_ ='region-past')
       # tbody = [tr.text for tr in holiday_list.find('tbody').findAll('tr')]

    #    print(holiday_Day)
for holiday in holiday_list:
    print(holiday)


print(holiday_list.text)


