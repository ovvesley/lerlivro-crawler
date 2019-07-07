from bs4 import BeautifulSoup
import requests

class LerLivroCrawler():
    def get_books_from_page(self, url):
        page = requests.get(url)
        page_soup = BeautifulSoup(page.content,"html.parser")
        uls = page_soup.find('ul', {'class': 'products'})
        links_book = []
        for indexI in uls:
            if (indexI.name == 'li'):
                print(indexI.a)
                links_book.append(indexI.a['href'])
        print(links_book)
    def get_book(self, url):
        page = requests.get(url)
        page_soup = BeautifulSoup(page.content,"html.parser")
        div = page_soup.find('div', {'class':'links-download'})
        links_book_download = []
        for indexI in div:
            if(indexI.name == 'a'):
                if("indexI.img['alt'] != 'Ler Online'"):
                    links_book_download.append(indexI['href'])
                print(links_book_download)