from bs4 import BeautifulSoup
import requests
url = "http://lelivros.love/page/2"

def get_books_from_page(url):
    page = requests.get(url)
    page_soup = BeautifulSoup(page.content,"html.parser")
    uls = page_soup.find('ul', {'class': 'products'})
    links_book = []
    for indexI in uls:
        if (indexI.name == 'li'):
            print(indexI.a)
            links_book.append(indexI.a['href'])
    print(links_book)

get_books_from_page(url)

