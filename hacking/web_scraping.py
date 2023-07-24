from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

temperatura = soup.find("a", class_="link actTriggerGA")
print(temperatura.string)
##print(soup.prettify())