import requests
from bs4 import BeautifulSoup
import csv

def get_data(url):
    #url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=Ikaruga&_sacat=0"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def parse(soup):
    productslist = []
    results = soup.find_all("div", {"class": "s-item__info clearfix"})
    for item in results:
        product = {
            "title": item.find("div", {"class": "s-item__title"}).text
        }
        #print(len(results))
        productslist.append(product)
        print(product)
        fields = ["title"]
        filename = "eBay.csv"
        with open('/home/adam/repos/web-scraping-sandbox/eBayListing.txt', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(productslist)
        #file.write(product)
        #file.close
    return
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=Ikaruga&_sacat=0"
soup = get_data(url)
parse(soup)

#file = open('/home/adam/repos/web-scraping-sandbox/eBayListing.txt', 'w')
#file.write(soup.prettify())
#file.close

#print (doc.prettify())


