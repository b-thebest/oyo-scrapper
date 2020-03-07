from bs4 import BeautifulSoup
import requests
import csv
import os

def cityScrapper(city):
    baseURL = 'https://www.oyorooms.com/hotels-in-' + city
    if not os.path.exists('data/'+ city +'.csv'):
        dataFile = open('data/' + city + '.csv', 'w')
    else:
        dataFile = open('data/' + city + '.csv', 'a')
    dataread = list(csv.reader(open('data/' + city + '.csv')))

    ##PAGE LOOP
    for i in range(1, 50):
        print('Page Number : ', i)
        mainPage = requests.get(baseURL + '?page=' + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(mainPage.text, "html.parser")

        hotelNameTags = soup.findAll('h3', {'class': 'listingHotelDescription__hotelName d-textEllipsis'})
        addressTags = soup.findAll('span', {'class', 'u-line--clamp-2'})

        if len(hotelNameTags) == 0 and len(addressTags) == 0:
            print("Data for "+ city + " successfully scraped!")
            break

        for hotel, address in zip(hotelNameTags, addressTags):
            name = hotel.text.replace('OYO ', '')
            addr = address.text
            print(name)
            print(addr)
            if [name, addr] not in dataread:
                csv.writer(dataFile).writerow([name, addr])
    dataFile.close()

if __name__ == '__main__':
    cities = ['indore', 'ujjain']
    for city in cities:
        print('City : ', city)
        cityScrapper(city)