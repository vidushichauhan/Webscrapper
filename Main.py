import requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager



url="https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

#Get the HTML
r=requests.get(url)
print("WEB SCRAPPING OF FLIPKART")

content=r.content #html content
#print(content)
#parse the HTML
soup=BeautifulSoup(content,'html.parser')
#print(soup.prettify)
title=soup.title
paras=soup.find_all('p')
anchor=soup.find_all('a')
#print(" PARAGRAPH 1ST")
#print(soup.find('p'))
#print("CLASSES")
#print(soup.find('p'))
#print("CLASS LEAD")
#print(soup.find_all('p', class_="lead"))

allLinks=set()

print("MENU")
print("choose '1' to find HTML content of the website")
print("choose '2' to find title of the content")
print("choose '3' to find all the paras")
print("choose '4' to find all the anchor tags")
print("choose '5' to find first paragraph")
print("choose '6' to find text in this html code")
print("choose '7' to find all urls")
print("choose '8' to make a CSV file of all items with their prices ")

ch=input("what you want to do?")

if(ch=='1'):
    print(soup.prettify)
if(ch=='2'):
    print("The Title is: ")
    print(title)
if(ch=='3'):
    print("paras are:")
    print(paras)
if(ch=='4'):
    print("anchor tags are:")
    print(anchor)
if(ch=='5'):
    print("first para is:")
    print(soup.find('p'))#first paragraph
if(ch=='6'):
    print("text")
    print(soup.find('p').get_text())
if(ch=='7'):
    for link in anchor:
        if (link.get('href') != '#'):
            link = url + link.get('href')
            allLinks.add(link)
            print(link)
    products = []  # List to store name of the product
    prices = []  # List to store price of the product
    ratings = []  # List to store rating of the product
if(ch=='8'):
    products = []  # List to store name of the product
    prices = []  # List to store price of the product

    soup = BeautifulSoup(content, features="html.parser")
    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'})
        price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})

        products.append(name.text)
        prices.append(price.text)

    df = pd.DataFrame({'Product Name': products, 'Price': prices})
    df.to_csv('products.csv', index=False, encoding='utf-8')
    print('completed...')
    print('check in folders')




