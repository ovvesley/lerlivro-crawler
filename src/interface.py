from ler_livro_crawler import Crawler
##quantidade de pagina
ler_livro = Crawler()
ler_livro.set_pages(3,5)
ler_livro.start()
print(len(ler_livro.array_book))

