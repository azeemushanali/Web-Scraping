# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:44:03 2020

@author: Azeemushan
"""

from selenium import webdriver
from calendar import monthrange
import pandas as pd

def makeURL():
    news_urls = []
    for month in range(1,13):
        days = monthrange(2010,month)[1]
        for day in range(1,days+1):
            base_url = f"https://www.thehindu.com/archive/web/2010/{month}/{day}/"
            news_urls.append(base_url)
    return news_urls

newsURL = makeURL()
newsURL=newsURL[:2] #'''For 2 days ''
def DayNewsLink(list_URL):
    news=[]
    links= []
    global driver
    driver = webdriver.Chrome()
    for url in newsURL:
        driver.get(url)
        for i in driver.find_elements_by_xpath('//div[2]/div/div/div/ul/li'):
            news.append(i.text)
            links.append(driver.find_element_by_link_text(i.text).get_attribute("href"))
        
        print(f"Done for url {url}")
    data = {'News': news[2:],'Links': links[2:]}
    df = pd.DataFrame.from_dict(data)
    return df

df_NewsLinks = DayNewsLink(newsURL)


def ScrapeALL(DataFrame):
    '''It is actually scraping all the 50 articles of the dAY TO MAKE IT FAST '''
    news_urls = DataFrame.values[:50,1:] 
    news_titles = DataFrame.values[:50,:1]
    news_final = {}
    #now for news
    i = 0 #start 
    for news in news_urls:
        i += 1
        url = news[0]
        driver.get(url)
        news_body = driver.find_element_by_xpath("//*[contains(@id, 'content-body')]").text
        try:
            news_author = driver.find_element_by_xpath("//a[contains(@class, 'auth-nm')]").text
        except:
            news_author = "NA"
        key = news_author
        news_final.setdefault(key, [])
        news_final[key].append(news_body)
        print(f"Scraping done {i}/50")
    return news_final

news_dictionary = ScrapeALL(df_NewsLinks)
        
def searchNews(auth_name,news_dict):
    if auth_name in news_dict:
        print(f"News Found for Author {auth_name}")
        print(news_dict[auth_name])
    else:
        print("Please chech the name again.I am afraid it is not there")

author = input("Enter the name of the Author to be searched - Case Senstive --> ")
searchNews(author,news_dictionary)



#from selenium import webdriver
#
#driver = webdriver.Chrome()
#driver.get("https://www.thehindu.com/opinion/op-ed/The-ANC-is-failing-poor-Africans/article16835229.ece")
#r = driver.find_element_by_xpath("//*[contains(@id, 'content-body')]")
#r.text
