import time

import cfscrape
import requests
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


API_KEY = ''
URL = "https://tres-bien.com/nike-air-1-fear-of-god-sail-ar4237-100-fw19"
FIRSTNAME = "Ronald"
LASTNAME = "McCarthy"
FULLNAME = FIRSTNAME + " " + LASTNAME
EMAIL = "ronnie94offi.cial@gmail.com"
ADDRESS = "J 45, street 420"
ZIPCODE = "456523"
CITY = "awesomecity"
PHONE = "9049945383"
COUNTRY = "France"
INSTAGRAM = "ronyx_funkorama"
SHOE_SIZE = "US 11"


proxies = ['109.74.142.138:53281']

def get_site_key():
      scraper = cfscrape.create_scraper()
      response = scraper.get(URL)
      soup = bs(response.text, "html.parser")
      sitekey = soup.find("div", class_="g-recaptcha")["data-sitekey"]
      
      if sitekey is None:
            print('Unable to get sitekey, server may be down.')
            return sitekey
      
      return sitekey

def get_driver(IP_ADDRESS, PORT):
      profile = webdriver.FirefoxProfile()
      profile.set_preference("network.proxy.type", 1)
      profile.set_preference("network.proxy.http", IP_ADDRESS)
      profile.set_preference("network.proxy.type", PORT)
      profile.update_preferences()

      return webdriver.Firefox(firefox_profile=profile)


for proxy in proxies:
      IP_ADDRESS = proxy.split(":")[0]
      PORT = proxy.split(":")[1]
      SITE_KEY = get_site_key()
      print(IP_ADDRESS, PORT)
      
      driver = get_driver(IP_ADDRESS, PORT)
      driver.get(URL)
      cookies = driver.get_cookies()
      for cookie in cookies:
            driver.add_cookie(cookie)
      driver.get(URL)
      driver.maximize_window()

      driver.execute_script("window.scrollTo(0, 800)")
      
      timeout = 10
      try:
            element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="fullname"]'))
            WebDriverWait(driver, timeout).until(element_present)
      except TimeoutException:
            print ("Timed out waiting for page to load")


      fullname = driver.find_element_by_xpath('//*[@id="fullname"]')
      fullname.send_keys(FULLNAME)
      time.sleep(0.5)
     
      email = driver.find_element_by_xpath('//*[@id="raffle-email"]')
      email.send_keys(EMAIL)
      time.sleep(0.5)
      
      address = driver.find_element_by_xpath('//*[@id="address"]')
      address.send_keys(ADDRESS)
      time.sleep(0.5)
      
      zipcode = driver.find_element_by_xpath('//*[@id="zipcode"]')
      zipcode.send_keys(ZIPCODE)
      time.sleep(0.5)

      city = driver.find_element_by_xpath('//*[@id="city"]')
      city.send_keys(CITY)
      time.sleep(0.5)

      select = Select(driver.find_element_by_xpath('//*[@id="raffle-country"]'))
      select.select_by_visible_text(COUNTRY)
      time.sleep(0.5)

      phone = driver.find_element_by_xpath('//*[@id="phone"]')
      phone.send_keys(PHONE)
      time.sleep(0.5)

      select = Select(driver.find_element_by_xpath('//*[@id="Size_raffle"]'))
      select.select_by_visible_text(SHOE_SIZE)
      time.sleep(0.5)

      # this part needs to worked out - captcha solution
      frame = driver.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div[5]/div[2]/div/div[2]/form/div[2]/div/div/iframe')
      driver.switch_to.frame(frame)
      
      captcha = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]')     
      
      recaptcha_id = requests.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, SITE_KEY, URL)).text.split('|')[1]
      recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, recaptcha_id)).text
      while 'CAPCHA_NOT_READY' in recaptcha_answer:
          print('Waiting for captcha. Sleeping!')
          time.sleep(15)
          recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, recaptcha_id)).text
      recaptcha_answer = recaptcha_answer.split('|')[1]
      
      captcha.send_keys(recaptcha_answer)
 
      time.sleep(0.5)

      
