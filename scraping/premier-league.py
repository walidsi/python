
# Scraping English Premier League standings from Wikipedia using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/2020%E2%80%9321_Premier_League'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
league_tables = soup.findAll('table', class_='wikitable')
rows = league_tables[3].findAll('tr')

#rows
df_list = []
keys = []
dict_row = {}

for index, row in enumerate(rows):
    elements = row.findAll('th')
    #print(elements)
    
    if index == 0:
        for ele in elements:
            keys.append(ele.text[:-1])
        print(keys)
        #dict_row = {key: None for key in keys}   
        #print(dict_row)
    else:
        elements = row.findAll(['td', 'th'])
        #dict_row = {}
        for index2, element in enumerate(elements):
            dict_row[keys[index2]] = element.text[:-1]
        #print(dict_row)
        df_list.append(dict_row.copy()) #must copy() because append() inserts a reference, otherwise need to initialize with every row

df = pd.DataFrame(df_list)
df.to_csv("EPL_Standings.csv", index=False)
 