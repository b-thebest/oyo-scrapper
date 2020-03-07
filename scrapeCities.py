from bs4 import BeautifulSoup
import requests
import csv

cityPage = requests.get("https://www.oyorooms.com/allcities/", headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(cityPage.text, "html.parser")
cityFile = open('cities.csv', 'w')

name_tages = soup.findAll('div', {'class': 'c-19rr7ql'})
for city in name_tages[1:]:
    print(city.text)
    csv.writer(cityFile).writerow([city.text])
