from bs4 import BeautifulSoup
import requests
import json

class Crawler():
    def __init__(self, url):
        pass
    def get_books_from_page(url, self):
        page = requests.get(url)
        page_soup = BeautifulSoup(page.content,"html.parser")
        uls = page_soup.find('ul', {'class': 'products'})
        links_book = []
        for indexI in uls:
            if (indexI.name == 'li'):           
                link = indexI.a['href']
                title = indexI.a.h3.text
                x = {
                    "Titulo": title,
                    "Link": link,
                    'Download': [],
                    }
                y = json.dumps(x)
                links_book.append(y)
        print(links_book)
        return links_book        
    def get_book(url, self):
        page = requests.get(url)
        page_soup = BeautifulSoup(page.content,"html.parser")
        div = page_soup.find('div', {'class':'links-download'})
        links_book_download = []
        for indexI in div:
            if(indexI.name == 'a'):
                if("indexI.img['alt'] != 'Ler Online'"):
                    links_book_download.append(indexI['href'])
                print(links_book_download)