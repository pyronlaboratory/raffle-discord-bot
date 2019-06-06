import time
import cfscrape
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup as bs


#write definition to load premium proxies
proxies = ['109.74.142.138:53281']

#import parameters from rafflefair.herokuapp.com
ENTRIES = ''
API_KEY = ''
URL = ""
FIRSTNAME = ""
LASTNAME = ""
EMAIL = "" # create either a catchall domain using this email/ use the dot trick - keep all the details in an array
PHONE = ""
INSTAGRAM = ""
SHOE_SIZE = "11US - 45" #use this format

#check if the user is in the premium list, and proceed accordingly

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


for entry in range(1,ENTRIES):

      proxy = proxies[entry-1]
      IP_ADDRESS = proxy.split(":")[0]
      PORT = proxy.split(":")[1]

      SITE_KEY = get_site_key()
      
      print(IP_ADDRESS, PORT)
      
      driver = get_driver(IP_ADDRESS, PORT)
      driver.get(URL)
      driver.maximize_window()

      timeout = 10
      try:
            element_present = expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="wpcf7-f2262-p2259-o1"]/form/p[8]/label/span/div/span/input'))
            WebDriverWait(driver, timeout).until(element_present)
      except TimeoutException:
            print ("Timed out waiting for page to load")

      
      firstname = driver.find_element_by_name("your-firstname")
      firstname.send_keys(FIRSTNAME)
      time.sleep(0.5)
      
      lastname = driver.find_element_by_name("your-name")
      lastname.send_keys(LASTNAME)
      time.sleep(0.5)
      
      email = driver.find_element_by_name("your-email")
      email.send_keys(EMAIL)
      time.sleep(0.5)
      
      phone = driver.find_element_by_name("your-tel")
      phone.send_keys(PHONE)
      time.sleep(0.5)
      
      instagram = driver.find_element_by_name("your-instagram")
      instagram.send_keys(INSTAGRAM)
      time.sleep(0.5)
      
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(0.5)
      
      size = driver.find_element_by_name("size")
      size.send_keys(SHOE_SIZE)
      time.sleep(0.5)
      
      accept_terms = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/article/div[5]/div/div/form/p[8]/label/span/div/span')
      accept_terms.click()
      time.sleep(0.5)
      
      captcha = driver.find_element_by_id('recaptcha-anchor')      

      recaptcha_id = session.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, SITE_KEY, URL)).text.split('|')[1]
      recaptcha_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, recaptcha_id)).text
      while 'CAPCHA_NOT_READY' in recaptcha_answer:
          print('Waiting for captcha. Sleeping!')
          sleep(15)
          recaptcha_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, recaptcha_id)).text
      recaptcha_answer = recaptcha_answer.split('|')[1]
      
      captcha.send_keys(recaptcha_answer)
  
      time.sleep(0.5)

      submit = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/article/div[5]/div/div/form/p[10]/input')
      submit.click()

      # log registeration details and email the file

      


      



      
