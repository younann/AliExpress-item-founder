from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
myKey=input("Enter what you searching for...")
price=input("Enter your Max price for this item")
browser=webdriver.Chrome()
browser.get('https://www.aliexpress.com/')
searchfiled=browser.find_element_by_xpath('//*[@id="search-key"]')
searchfiled.send_keys(myKey)
searchfiled.send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[1]/span[2]/input').send_keys('0.5')
maxprice=browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[1]/span[3]/input')
maxprice.send_keys(price)
maxprice.send_keys(Keys.ENTER)
time.sleep(5)
freeShipping=browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[3]/span[2]/label/span[2]/span')
freeShipping.click()
time.sleep(3)
bestMatch=browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/span/span[2]')
bestMatch.click()
time.sleep(2)

item=browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li[1]/div/div[2]/div/div[1]/a')
link=item.get_attribute('href')
print(link)

time.sleep(20)
browser.close()

