import requests
import logging
from time import sleep

# raffle tool modules

# import sys
# sys.path.insert(0, r"/app/tools") # update address on production server

from .tools import test
from .tools import urls
from .tools import proxies
from .tools import email_ops
from .tools import site_key
from .tools import driver


# selenium modules
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, JavascriptException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def execute_entry(url,proxy,email, data):
      try:
            browser = driver.load_firefox_driver(proxy)
            browser.get(url)

            # adding cookies
            cookies = browser.get_cookies()
            for cookie in cookies:
                  browser.add_cookie(cookie)
            browser.get(url)

            browser.maximize_window()
            browser.execute_script("window.scrollTo(0, 1000)")
            sleep(5)
            print("Launching browser")

            # check if the raffle is still going on
            try:
                  print("Checking for raffle")
                  browser.execute_script("document.getElementById('notice-cookie-block').style.display = 'none';")
                  element_present = expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="fullname"]'))
                  WebDriverWait(browser, 30).until(element_present)
            except Exception as e:
                  # exit script
                  print(type(e))
                  print('printed log: '+str(e))
                  print('--Logging--')
                  logging.exception("message")
                  print("Unable to locate element")
                  message = "There seems to be an issue with your registration. Raffle is probably closed or their server is not responsive at the moment. Timed out waiting for page to load. Please try again later!"
                  email_ops.send_email(email, 'Raffle Entry Status: Error', message)
                  browser.quit()
                  return False

            # register
            print("Entering details")
            browser.find_element_by_xpath('//*[@id="fullname"]').send_keys(data['firstname'] +" " + data['lastname'])
           
            browser.find_element_by_xpath('//*[@id="raffle-email"]').send_keys(email)
            
            browser.find_element_by_xpath('//*[@id="address"]').send_keys(data['address'])
            
            browser.find_element_by_xpath('//*[@id="zipcode"]').send_keys(data['zipcode'])

            browser.find_element_by_xpath('//*[@id="city"]').send_keys(data['city'])

            Select(browser.find_element_by_xpath('//*[@id="raffle-country"]')).select_by_visible_text(data['country'])

            browser.find_element_by_xpath('//*[@id="phone"]').send_keys(data['phone'])

            Select(driver.find_element_by_xpath('//*[@id="Size_raffle"]')).select_by_visible_text(data['shoe_size'])

            # captcha solution
            try:
                  browser.execute_script("document.getElementById('g-recaptcha-response').style.display = 'block';")
                  browser.execute_script("document.getElementById('g-recaptcha-response').style.width = '150px';")
                  
                  recaptcha_id = requests.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(data['api_key'], sitekey, url)).text.split('|')[1]
                  recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(data['api_key'], recaptcha_id)).text
                  while 'CAPCHA_NOT_READY' in recaptcha_answer:
                        sleep(15)
                  recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(data['api_key'], recaptcha_id)).text
                  recaptcha_answer = recaptcha_answer.split('|')[1]
            except Exception as e:
                  # exit script
                  print(type(e))
                  print('printed log: '+str(e))
                  print('--Logging--')
                  logging.exception("message")
                  message = "There seems to be an issue with your registration. Either 2Captcha's server is unresponsive at the moment or your 2Captcha api_key is out of balance. Try again in sometime"
                  email_ops.send_email(email, 'Raffle Entry Status: Error', message)
                  browser.quit()
                  return False
            
            browser.find_element_by_id('g-recaptcha-response').send_keys(recaptcha_answer)                  
            sleep(5)

            # submit
            print("Submitting the form")
            WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="raffle-form"]/div[3]/button'))).click()
            sleep(5)
            browser.quit()
            return True
      except Exception as e:
            print(type(e))
            print('printed log: '+str(e))
            print('--Logging--')
            logging.exception("message")
            message = "There was an error reported for an user entry. Please check the site admin page for more details"
            email_ops.send_email('rafflebeezarebuzzing@gmail.com', 'Raffle Entry Status: Error', message)
            browser.quit()
            return False

def main(**data):
      try:
            test.main()
            thread_count = data['tresbien']['threads']
            url = urls.load_url('tres-bien')
            raffle_proxies = proxies.load_proxies()
          
            email_list = []
            raffle_email = data['tresbien']['email']
            print(raffle_email)
            raffle_email = raffle_email.split('@')
            if raffle_email[1] == 'gmail.com':
                  # use the + trick
                  domain_name = '@gmail.com'
                  gmail_list = email_ops.get_list(domain_name, thread_count)
                  for email_id in gmail_list:
                        email_id = raffle_email[0]+ '+' +email_id
                        email_list.append(email_id)
                  
            else:
                  #write the catch all trick
                  domain_name = '@' + raffle_email[1]
                  email_list = email_ops.get_list(domain_name, thread_count) # extract domain name from email address

            proxies_count = len(raffle_proxies) # compare with thread counts
            if int(thread_count) > int(proxies_count):
                  thread_count = proxies_count
                  message = "You are receiving this warning since you tried to create more threads than we are currently supporting. We are still happy to proceed your request with our available resources. Thanks for understanding!"
                  email_ops.send_email(data['tresbien']['email'], 'Raffle Entry Status: Warning', message)
                  
            sitekey = site_key.get_site_key(url)
            if sitekey == "":
                  message = "There seems to be an issue with your registration. Raffle is probably closed or their server is not responsive at the moment. Timed out waiting for page to load. Please try again later!"
                  email_ops.send_email(data['tresbien']['email'], 'Raffle Entry Status: Error', message)


            for i in range(int(thread_count)):
                  proxy = raffle_proxies.pop()
                  email = email_list.pop()
                  status = execute_entry(url=url,proxy=proxy,email=email, data=data['tresbien'])
                  if status is True:
                        message = 'Your raffle entry for the registered email has been successfully registered. Please check your emails for any other verifications from tres-bien.com to confirm the entry.'
                        email_ops.send_email(email, 'Raffle Entry Status: Success', message)
                  else:
                        continue
      except Exception as e:
            print(type(e))
            print('printed log: '+str(e))
            print('--Logging--')
            logging.exception("message")
            message = "There was an error reported for an user entry. Please check the site admin page for more details"
            email_ops.send_email('rafflebeezarebuzzing@gmail.com', 'Raffle Entry Status: Error', message)