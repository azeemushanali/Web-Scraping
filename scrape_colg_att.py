from selenium import webdriver 
import requests
from bs4 import BeautifulSoup 
import time



driver = webdriver.Chrome()

driver.get ("http://52.220.116.248/")
#driver.find_element_by_id(“ID”).send_keys(“username”)
#driver.find_element_by_id (“ID”).send_keys(“password”)
#driver.find_element_by_id(“submit”).click()


driver.find_element_by_name("email").send_keys("$yourEmailHere")
driver.find_element_by_name("password").send_keys("$yourPasswordHere")
#driver.find_element_by_class_name("btn.btn-success btn-block").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[3]/div[1]").click()

driver.get("http://52.220.116.248/academic#/subject_wise_attendence/")
driver.get("http://52.220.116.248/academic#/section_wise_attendence")
time.sleep(50)

xyz = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]')
#print(xyz)
print(xyz.text)
print("Block 1 done by Xpath")
sel = driver.find_element_by_css_selector("#wrapper > div.content-page > div > div > div > div > div > div.widget-content > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2)")
#print(sel)
print(sel.text)
print("Block 2 done by CSS Selectors")
byclass = driver.find_element_by_class_name("table.table-striped")
#print(byclass)
print(byclass.text)
print("Block 3 done by Class name")
sty  = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]')
#print(sty)
print(sty.text)
print("Block 4 done by Full Xpath")

print("Colg Id\tName\tAttendance Percentage")
for i in range(1,59):
    col_id = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[' + str(i) + ']/td[2]').text
    name = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[' + str(i)+']/td[5]').text
    percent = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr['+str(i)+']/td[19]').text
    print(col_id,name,"\t",percent)

#driver.get(url)
#content = driver.page_source
#soup = BeautifulSoup(content)           
           
#           
#print(data)
