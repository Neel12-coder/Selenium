import requests
from selenium import webdriver
import time

driver = webdriver.Chrome("C://Users/user/AppData/Local/Programs/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.w3.org/")
links = driver.find_elements_by_xpath('.//a')
print("All links are....")

for link in links:
    r = requests.head(link.get_attribute("href"))
    print(link.get_attribute('href'), r.status_code)




