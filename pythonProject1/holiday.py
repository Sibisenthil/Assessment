import requests
from bs4 import BeautifulSoup
import csv

def Extraxct_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

    r= requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(r, 'lxml')
    table = soup.find("table",{"class":"country-table"})
    #table = soup.table
    thead = table.find("thead").find_all("th")
    table_head = [ th.text for th in thead]
    table_body = table.find("tbody").find_all("tr")
    with open("list of holidayss.csv", "w", newline="") as csv_file:
        csv.write = csv.writer(csv_file)
        csv.write.writerow(table_head)
        for tr in table_body:
            table_data = [ td.text for td in tr.find_all("td")]
            csv.write.writerow(table_data)
    #print(table_body)
Extraxct_data(url="https://www.officeholidays.com/countries/india/2021")
