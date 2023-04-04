import requests
import pandas as pd
from bs4 import BeautifulSoup

Names = []
Description = []

url = 'https://www.airbnb.co.in/s/Hyderabad--India/homes?adults=1&place_id=ChIJx9Lr6tqZyzsRwvu6koO3k64&refinement_paths%5B%5D=%2Fhomes'
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
for i in range(1, 12):
    next_page = soup.find('a', class_='l1j9v1wn c1ytbx3a dir dir-ltr').get('href')
    # print(next_page)
    complete_next_page = "https://www.airbnb.co.in"+next_page
    # print(complete_next_page)

    url = complete_next_page
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    names = soup.find_all('div', class_='t1jojoys dir dir-ltr')
    # print(names)
    for i in names:
        n = i.text
        Names.append(n)

    desc = soup.find_all('span', class_='t6mzqp7 dir dir-ltr')
    # print(desc)
    for i in desc:
        d = i.text
        Description.append(d)


df = pd.DataFrame({"Name": Names, "Stay Description": Description})
print(df)

df.to_csv("airbnb_hyderabad.csv")