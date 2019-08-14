import random
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


def execute_entry(url,proxy,email,data):
      try:
            browser = driver.load_firefox_driver(proxy)
            browser.get(url)
            browser.maximize_window()

            browser.execute_script("window.scrollTo(0, 1040)")
            sleep(5)
            print("Launching browser")

            # check if the raffle is still going on
            try:
                  print("Checking for raffle")
                  element_present = expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="mce-EMAIL"]'))
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
            browser.find_elements_by_xpath('//*[@id="mce-EMAIL"]')[1].send_keys(email)
            sleep(2)

            browser.find_element_by_xpath('//*[@id="mce-FNAME"]').send_keys(data['firstname'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="mce-LNAME"]').send_keys(data['lastname'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="mce-STREET"]').send_keys(data['address'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="mce-ZIP"]').send_keys(data['zipcode'])
            sleep(2)
            
            browser.execute_script("window.scrollTo(0, 500)")
            
            browser.find_element_by_xpath('//*[@id="mce-CITY"]').send_keys(data['city'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="mce-STATE"]').send_keys(data['state'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="mce-COUNTRY"]').send_keys(data['country'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="mce-SIZES"]').send_keys(data['shoe_size'])
            sleep(2)
            
            # submit
            WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="mc-embedded-subscribe"]'))).click()
            sleep(20)
            
            # switch window
            window_after = browser.window_handles[1]
            browser.switch_to_window(window_after)
           
            # subscribe
            try:
                  element_present = expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="MERGE1"]'))
                  WebDriverWait(browser, 20).until(element_present)
            except Exception as e:
                  # exit script
                  print(type(e))
                  print('printed log: '+str(e))
                  print('--Logging--')
                  logging.exception("message")
                  message = "There seems to be an issue with your registration. Raffle is probably closed or their server is not responsive at the moment. Timed out waiting for page to load. Please try again later!"
                  email_ops.send_email(email, 'Raffle Entry Status: Error', message)
                  browser.quit()
                  return False

            browser.find_element_by_xpath('//*[@id="MERGE1"]').send_keys(data['firstname'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="MERGE2"]').send_keys(data['lastname'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="MERGE6"]').send_keys(data['city'])
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="MERGE0"]').send_keys(email)
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="MERGE4"]').send_keys(random.randint(100000,999999)) #random_id
            sleep(2)
            
            browser.find_element_by_xpath('//*[@id="MERGE9"]').send_keys(data['shoe_size'])
            sleep(2)
            
            # submit
            WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/div[3]/input'))).click()
            sleep(20)

            # captcha solution     
            try:
                  browser.execute_script("document.getElementById('g-recaptcha-response').style.display = 'block';")
                  browser.execute_script("document.getElementById('g-recaptcha-response').style.width = '150px';")
                  site_key = browser.find_element_by_xpath('/html/body/div[1]/div/form/div/div').get_attribute("data-sitekey")
                  recaptcha_id = requests.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(data['api_key'], site_key, 'https://afew-store.us5.list-manage.com/subscribe/post')).text.split('|')[1]
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

            # submit
            print("Submitting the form")
            WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/form/input[4]'))).click()
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
            print(data['afewstore']['threads'])
            thread_count = data['afewstore']['threads']
            url = urls.load_url('afew-store')
            print(url)
            raffle_proxies = proxies.load_proxies()

            email_list = []
            raffle_email = data['afewstore']['email']
            raffle_email = raffle_email.split('@')  # extract domain name from email address
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
                  email_list = email_ops.get_list(domain_name, thread_count)
            print(email_list)

            proxies_count = len(raffle_proxies) # compare with thread counts
            if int(thread_count) > int(proxies_count):
                  thread_count = proxies_count
                  message = "You are receiving this warning since you tried to create more threads than we are currently supporting. We are still happy to proceed your request with our available resources. Thanks for understanding!"
                  email_ops.send_email(data['tresbien']['email'], 'Raffle Entry Status: Warning', message)   

            for i in range(int(thread_count)):
                  print("Entering loop:"+ str(i))
                  proxy = raffle_proxies.pop()
                  email = email_list.pop()
                  status = execute_entry(url=url,proxy=proxy,email=email, data=data['afewstore'])
                  if status is True:
                        message = 'Your raffle entry for the registered email has been successfully registered. Please check your emails for any other verifications from afew-store.com to confirm the entry.'
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