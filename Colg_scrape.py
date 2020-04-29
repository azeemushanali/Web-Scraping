# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:22:44 2019

@author: Azeemushan
"""

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from firebase import firebase

FBcon = firebase.FirebaseApplication('$yourFirebaseLinkHere',None)

driver = webdriver.Chrome()

def check():
    path1 = '//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/thead/tr/th[19]'
    path2 = '//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/thead/tr/th[18]'
    if driver.find_element_by_xpath(path1).text == '%' and driver.find_element_by_xpath(path2).text == "Total":
        print("No Change in X Path")
    else:
        print("X path Changed")
        print("Ending your scraping")
        quit()



driver.get ("http://52.220.116.248/")
#driver.find_element_by_id(“ID”).send_keys(“username”)
#driver.find_element_by_id (“ID”).send_keys(“password”)
#driver.find_element_by_id(“submit”).click()

colg_id = input("Enter Colg ID-   ")
passwor = input("Enter the password-   ")
driver.find_element_by_name("email").send_keys(colg_id) 
driver.find_element_by_name("password").send_keys(passwor)
#driver.find_element_by_name("email").send_keys('') #
#driver.find_element_by_name("password").send_keys('') #

#-------------------------------------------------------------------------------------------------*/
driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[3]/div[1]").click()

driver.get("http://52.220.116.248/academic#/subject_wise_attendence/")
driver.get("http://52.220.116.248/academic#/section_wise_attendence")
print("Please wait while attendance is being loaded")
time.sleep(50)

#you can try by copying selector as well
#driver.find_element_by_css_selector('#wrapper > div.content-page > div > div > div > div > div > div.widget-content > div:nth-child(2) > table > thead > tr > th:nth-child(2)').text


def scrape(i):
    col_id = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[' + str(i) + ']/td[2]').text
    name = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[' + str(i)+']/td[5]').text
    percent = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr['+ str(i)+ ']/td[19]').text
    fraction = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr['+ str(i)+']/td[18]').text
    section = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]').text
    print(col_id,name," \t ",percent.rjust(5))
    data_to_upload = {
            'Colg_ID':col_id,
            'Name':name ,
            'Fraction':fraction,
            'Percent':percent,
            }
    result = FBcon.post(section , data_to_upload)
#    naaaaam = 'Roll No-'+str(i)
#    result = FBcon.patch(naaaaam,data_to_upload)


    
check()
print("Colg Id ".ljust(14) + "Name".center(10) + "  Attendance Percentage")
for i in range(1,65):
    try:
        
        scrape(i)
    except NoSuchElementException:
        print("Attendance Done Successfully")
        break
    except Exception as e:
        print("Error Occured",e)
        break

driver.close()
#

#data = driver.find_element_by_css_selector('#wrapper > div.content-page > div > div > div > div > div > div.widget-content > div:nth-child(2) > table > tbody')
#for table in driver.find_elements_by_xpath('//*[@id="wrapper"]/div[2]/div/div/div/div/div/div/div[2]/div[2]/table'):
#    i = 1
#    data = [item.text for item in table.find_element ("/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[{i}]/td[19]")]
#    print(data)
#    i = i+1

           
#driver.get(url)
#content = driver.page_source
#soup = BeautifulSoup(content)           
           
#           
#print(data)
