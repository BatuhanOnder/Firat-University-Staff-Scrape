import requests

from bs4 import BeautifulSoup
from lxml.cssselect import CSSSelector
import os
class Scrape:


    def __init__(self, base_url):
        self.base_url = base_url

    def connect(self,page):
        url = self.base_url + page
        response = requests.get(url)
        return response

    def scrape(self):
        r = requests.get('http://bilgisayar.mf.firat.edu.tr/tr/academic-staffs')
        soup = BeautifulSoup(r.content, 'lxml')
        kisiler = soup.find_all("div",{"class" :"profile-outer"})
        for kisi in kisiler:
            linkler = kisi.select(".user-links > a")
            for link in linkler:
                personal_url = link.get("href")
                if  ("https://staff.firat.edu.tr/person.jsp?param=") in personal_url:
                    path = os.getcwd() + "\kisi-adresleri"
                    if  not os.path.exists(path):
                        os.mkdir(path)
                    with open(path+"\kisiler.txt","a") as file:
                        file.write(personal_url+"\n")


if __name__ == "__main__":
    scrape  = Scrape("http://bilgisayar.mf.firat.edu.tr/tr/")
    scrape.scrape()