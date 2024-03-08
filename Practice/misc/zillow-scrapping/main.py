from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


google_form = "https://docs.google.com/forms/d/e/1FAIpQLScF_hcDT26YW5zO1l07rxG0eC6-wsmfAoYtloYX_GfduSpm4A/viewform?usp=sf_link"
zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"

# fetch the HTML content
response = requests.get(zillow_clone_url)

# check if request is successful
if response.status_code == 200:
    
    #parse the HTML with bs4
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
else:
    print('Failed to fetch the webpage:', response.status_code)


# create list of links
rental_links = soup.find_all(class_ = "StyledPropertyCardDataWrapper")

hrefs = [link.a["href"] for link in rental_links if link.a]

# create list of prices
card_prices = soup.find_all(class_="StyledPropertyCardDataWrapper")
price = [price.span.text[0:6] for price in card_prices]

# create list of addresses
card_address = soup.find_all(class_="StyledPropertyCardDataWrapper")
addresses = [
    address.find("address").text.strip().split(",", 1)[1]
    for address in card_address
    if address.find("address")
]

#use selenium to fill in the form 
