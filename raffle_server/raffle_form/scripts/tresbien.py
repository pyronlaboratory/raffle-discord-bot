from time import sleep
import requests

# raffle tool modules
import sys
sys.path.insert(0, r"C:\Users\AYUSH\Desktop\Ronnie\python\discord-raffle-bot\raffle_scripts_v2.0\tools") # update address on production server

import test
import urls
import proxies
import generate_email
import site_key
import driver

# selenium modules
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def execute_entry(site_key,proxy):
      browser = driver.load_driver(proxy)
      browser.get(url)
      cookies = browser.get_cookies()
      for cookie in cookies:
            browser.add_cookie(cookie)
      browser.get(url)
      browser.maximize_window()

      browser.execute_script("window.scrollTo(0, 1000)")
      sleep(5)
      browser.execute_script("document.getElementById('notice-cookie-block').style.display = 'none';")

      # check if the raffle is still going on
      timeout = 10
      try:
            element_present = expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="fullname"]'))
            WebDriverWait(browser, timeout).until(element_present)
      except TimeoutException:
            # write exit script
            print ("Raffle is probably closed or their is not responsive at the moment. Timed out waiting for page to load. Please try again later!")

   
      browser.find_element_by_xpath('//*[@id="fullname"]').send_keys(data['tresbien']['firstname'] +" " + data['tresbien']['lastname'])
     
      browser.find_element_by_xpath('//*[@id="raffle-email"]').send_keys(email)
      
      browser.find_element_by_xpath('//*[@id="address"]').send_keys(data['tresbien']['address'])
      
      browser.find_element_by_xpath('//*[@id="zipcode"]').send_keys(data['tresbien']['zipcode'])

      browser.find_element_by_xpath('//*[@id="city"]').send_keys(data['tresbien']['city'])

      Select(browser.find_element_by_xpath('//*[@id="raffle-country"]')).select_by_visible_text(data['tresbien']['country'])

      browser.find_element_by_xpath('//*[@id="phone"]').send_keys(data['tresbien']['phone'])

      Select(driver.find_element_by_xpath('//*[@id="Size_raffle"]')).select_by_visible_text(data['tresbien']['shoe_size'])

      # captcha solution
      browser.execute_script("document.getElementById('g-recaptcha-response').style.display = 'block';")
      browser.execute_script("document.getElementById('g-recaptcha-response').style.width = '150px';")
      try:
            recaptcha_id = requests.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(data['tresbien']['api_key'], site_key, url)).text.split('|')[1]
            recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(data['tresbien']['api_key'], recaptcha_id)).text
            while 'CAPCHA_NOT_READY' in recaptcha_answer:
                  print('Waiting for captcha..')
                  sleep(15)
            recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, recaptcha_id)).text
            recaptcha_answer = recaptcha_answer.split('|')[1]
      except:
            # write exit script
            print('recaptcha api is not responsive. Try again in sometime')
      
      
      browser.find_element_by_id('g-recaptcha-response').send_keys(recaptcha_answer)                  
      sleep(5)

      #submit
      WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="raffle-form"]/div[3]/button'))).click()


def main(**data):
      print("working")
      '''
      test.main()
      url = urls.load_url('tres-bien')
      proxies = proxies.load_proxies()
      proxies_count = len(proxies) # compare with thread counts
      if thread_count > proxies_count:
            pass
            # write exit script
      email_list = generate_email.get_list("@rycao.me", thread_count) # extract domain name from email address
      site_key = site_key.get_site_key(url)

      thread_count = data['tresbien']['threads']
      for i in range(thread_count):
            proxy = proxies.pop()
            email = email_list.pop()
            execute_entry(proxy,email, data['tresbien'])

            # email the details to user      
      '''
