from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen

site = 'https://news.google.com/news/rss'

op = urlopen(site)
read = op.read()
op.close()

soup_page  = soup(read,'xml')
news_list = soup_page.findAll('item')
for  news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("--"*50)