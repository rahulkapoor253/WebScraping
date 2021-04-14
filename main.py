# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import csv

res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

print(res.status_code)

soup = BeautifulSoup(res.content, 'html.parser')
# to scrape title, body, head we use soup.title, soup.head, soup.body

all_products = []

products = soup.select("div.thumbnail")
for product in products:
    name = product.select("h4 > a")[0].text.strip()
    price = product.select("h4.price")[0].text.strip()
    description = product.select("p.description")[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select("img")[0].get("src")

    all_products.append({
        "product_name": name,
        "price": price,
        "description": description,
        "reviews": reviews,
        "image": image
    })

columns = all_products[0].keys()
with open("my_data.csv", "w", newline="") as file:
    dict_writer = csv.DictWriter(file, columns)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)