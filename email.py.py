import requests
from selenium import webdriver
import time

driver = webdriver.Chrome("C://Users/user/AppData/Local/Programs/chromedriver.exe")
driver.set_page_load_timeout(90)
#driver.get("http://www.google.com/gmail/")             

sender = 'Neel'
gmail_user = 'SamWiki1999@gmail.com'
gmail_pswd = 'SamWiki123456'
msg = 'This is a test message for internship purpose only.'

def login_gmail():
    is_logged_in = False
    gmail_login = "http://www.google.com/gmail/"

    try:
        driver.get(gmail_login)
        driver.maximize_window()
        time.sleep(1)
        html = driver.page_source.strip()

        email_id = driver.find_element_by_name("identifier")
        email_id.clear()
        email_id.send_keys("SamWiki1999@gmail.com")
        email_button = driver.find_element_by_id("identifierNext")
        email_button.click()
        time.sleep(1)

        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys("SamWiki123456")
        password_button = driver.find_element_by_id("passwordNext")
        password_button.click()
        time.sleep(1)

        html = driver.page_source.strip()
        is_logged_in = True

    except Exception as ex:
        print(str(ex))
        is_logged_in = false
    finally:
        return is_logged_in
                
login_gmail()

def access_gmail():
    try:
        '''
        #driver.get('http://gmail.com')
        time.sleep(1)
        m = driver.find_elements_by_css_selector('.UI table > tbody > tr')

        for a in m:
            if sender.lower() in a.text:
                a.click()
                break

        # take rest'''
        #time.sleep(1)
        compose = driver.find_element_by_css_selector("div[class='T-I J-J5-Ji T-I-KE L3']")
        time.sleep(1)
        if compose:
            compose.click()
            time.sleep(1)
            driver.find_element_by_class_name('vO').send_keys('SamWiki1999@gmail.com')
            driver.find_element_by_class_name('aoT').send_keys('Test Mail')

            editable = driver.find_element_by_css_selector('.editable')
            if editable:
                editable.click()
                editable.send_keys(msg)

            

            send = driver.find_elements_by_xpath('//div[@role="button"]')
            for s in send:
                if s.text.strip() == 'Send':
                    s.click()

    except Exception as ex:
        print(str(ex))
    finally:
        return True
access_gmail()
