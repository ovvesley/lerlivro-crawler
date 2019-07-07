from bs4 import BeautifulSoup
import requests
import json

class Crawler():
    __link_list = []
    array_book = []
    def __init__(self):
        print('Bem vindo ao Crawler LER LIVRO')
        
    def set_pages(self, start=2, end=622):
        self.__link_list = [('http://lelivros.love/page/'+ str(indexI) +'/') for indexI in range(start, end)]

    def start(self):        
       for link in self.__link_list:
            value = self.__get_books_from_page(link)
            for book_json in value:
                book = json.loads(book_json)
                book['Download'] = self.__get_book(book['Link'])
                #book_js = json.dump(book)
                self.array_book.append(book)               

    def __get_books_from_page(self, url):
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
        return links_book        
    def __get_book(self, url):
        page = requests.get(url)
        page_soup = BeautifulSoup(page.content,"html.parser")
        div = page_soup.find('div', {'class':'links-download'})
        links_book_download = []
        for indexI in div:
            if(indexI.name == 'a'):
                if(indexI.img['alt'] != 'Ler Online'):
                    links_book_download.append(indexI['href'])
        return links_book_download

    def download_book():
        pass