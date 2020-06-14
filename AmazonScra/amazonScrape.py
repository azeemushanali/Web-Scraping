# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 04:17:10 2020

@author: Azeemushan
"""

from selenium import webdriver
import re
import pandas as pd

def scrape():
    lis = []
    count = 0
    for n in range(2,23):
        lat= f"//span[3]/div[2]/div[{n}]"
        try:
            something = driver.find_element_by_xpath(lat).text
            if(something in lis):
                count += 1
                print("allready present")
            elif ('Best seller' in something or 'Sponsored' in something):
                start = something.index('\n') + 1
                something = something[start:]
                lis.append(something)
            else:
                lis.append(something)
            BookName = something[:something.index('\nby')]
            authorName = something[something.index('\nby')+3:something.index('|')]
            bookPrice = re.findall('₹[0-9]{1,5}',something)[0]
            ScrapedData.append({
                    'Book Name' : BookName,
                    'Author Name' :authorName,
                    'Book Price(In Rs)': bookPrice[1:]})
        except Exception:
            count += 1
#            print('E')
        if count == 5:
            break
    
if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    q= "novel"
    url = "https://www.amazon.in/s?k=" + q
    driver.get(url) 
    numberofpages = 2
    ScrapedData = []
    for i in range(numberofpages):
        nexturl = 'https://www.amazon.in/s?k=novel&page=' +str(i+1)
        driver.get(nexturl)
        scrape()
    df = pd.DataFrame(ScrapedData)
    df.to_csv("Desktop//data.csv")




