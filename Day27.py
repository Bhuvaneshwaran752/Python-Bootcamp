import requests, csv, pandas as pd
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=hp+laptop+8gb+ram&crid=P9IFJ5D1KA2Q&sprefix=hp+la%2Caps%2C475&ref=nb_sb_ss_ts-doa-p_10_5"
response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, "html.parser")
print(soup.prettify)

laptops = []
price = []

laptops = soup.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
print(laptops.text)

for a in soup.findAll('a', href=True, attrs={'class':'sg-row'}):
    name = a.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
    prices = a.find('span', attrs={'class': 'a-price-whole'})
    laptops.append(name.text)
    prices.append(price.text)

df =pd.DataFrame({"Lap name": laptops, "Price": prices})
df.head()
df.to_csv("smaple.csv")

