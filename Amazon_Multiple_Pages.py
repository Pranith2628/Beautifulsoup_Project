import requests
from bs4 import BeautifulSoup
import pandas as pd

Names = []
Prices = []
Description = []

for i in range(1, 11):
    url = 'https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find('div', class_='_1YokD2 _3Mn1Gg')
    names = box.find_all('div', class_='_4rR01T')
    # print(names)
    for i in names:
        n = i.text
        Names.append(n)
    print(len(Names))

    prices = box.find_all('div', class_='_30jeq3 _1_WHN1')
    # print(prices)
    for i in prices:
        p = i.text
        Prices.append(p)
    print(len(Prices))

    desc = box.find_all('ul', class_='_1xgFaf')
    # print(desc)
    for i in desc:
        d = i.text
        Description.append(d)
    print(len(Description))


df = pd.DataFrame({'product names': Names, ' product price': Prices, 'product description': Description})
print(df)

df.to_csv("Amazon_multiple_pages.csv")
