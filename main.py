import requests
from bs4 import BeautifulSoup

target_url = "https://atilsamancioglu.com"
foundLinks = []

def make_requests(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawl(url):
    links = make_requests(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link: #none değilse demek
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if target_url in found_link and found_link not in foundLinks:
                foundLinks.append(found_link)
                print(found_link)
                #recursive
                crawl(found_link)

crawl(target_url)

#html parsing
#html parse ederken kullanılan bir kütüphanedir beautiful soup
