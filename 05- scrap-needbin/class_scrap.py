import requests
from bs4 import BeautifulSoup
import pprint
import json

class Scrap ():
    
    def __init__ (self, links, price):
        self.price = price
        self.links = links
        self.h = []

    def sorted_with_price (self, h):
        sorted (self.h, key = lambda k:k ['price']) #sort on the basis of price
        for i in range(0, len(self.h)):
            self.h[i]['id'] = i #add id to the list 
        return self.h

    def scrape_needbin (self, links, price):
        
        for idx, item in enumerate(self.links):
            title = item.getText().strip()
            lnk = links[idx].select("a")
            lk = lnk[0].get ('href', None)
            prc = float(self.price[idx].getText().replace(u"৳\xa0", u""))
            self.h.append({"title": title, "links": lk, "price":prc})
        return self.sorted_with_price(self.h)

    
    def make_json (self):
        out_file = open("test2.json", "w") 
        json.dump(self.scrape_needbin (self.links, self.price), out_file, indent = 4, sort_keys = False)


def main ():
    res = requests.get('https://needbin.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    price = soup.select ('.woocommerce-Price-amount')
    links = soup.select('.featured-title')
    p1 = Scrap (links, price)
    p1.make_json()

if __name__ == '__main__':
    main ()