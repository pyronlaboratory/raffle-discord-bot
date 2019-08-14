import logging
from time import sleep

# raffle tool modules

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
                  element_present = expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="comp_firstname"]'))
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
            browser.find_element_by_xpath('//*[@id="comp_firstname"]').send_keys(data['firstname'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_lastname"]').send_keys(data['lastname'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_email"]').send_keys(email)
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_paypalemail"]').send_keys(data['paypal_email'])
            sleep(5)
            
            Select(browser.find_element_by_xpath('//*[@id="comp_countrycode"]')).select_by_visible_text(data['phone_prefix'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_mobile_end"]').send_keys(data['phone'])
            sleep(5)
            
            Select(browser.find_element_by_xpath('//*[@id="shoesize"]')).select_by_visible_text(data['shoe_size'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_address1"]').send_keys(data['street1'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_address2"]').send_keys(data['street2'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_address3"]').send_keys(data['city'])
            sleep(5)
            
            Select(browser.find_element_by_xpath('//*[@id="comp_address4"]')).select_by_visible_text(data['county'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="comp_postcode"]').send_keys(data['zipcode'])
            sleep(5)
            
            browser.find_element_by_xpath('//*[@id="validation"]/table/tbody/tr[3]/td/table/tbody/tr/td/table[2]/tbody/tr/td[2]/table/tbody/tr[7]/td/table/tbody/tr/td[1]/label[1]').click()
            sleep(5)
            
            # submit
            print("Submitting the form")
            WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))).click()
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
            thread_count = data['jdsports']['threads']
            url = urls.load_url('jdsports')
            raffle_proxies = proxies.load_proxies()

            email_list = []
            raffle_email = data['jdsports']['email']
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


            proxies_count = len(raffle_proxies) # compare with thread counts
            if int(thread_count) > int(proxies_count):
                  thread_count = proxies_count
                  message = "You are receiving this warning since you tried to create more threads than we are currently supporting. We are still happy to proceed your request with our available resources. Thanks for understanding!"
                  email_ops.send_email(data['jdsports']['email'], 'Raffle Entry Status: Warning', message)   

            for i in range(int(thread_count)):
                  sleep(5)
                  proxy = raffle_proxies.pop()
                  email = email_list.pop()
                  status = execute_entry(url=url,proxy=proxy,email=email, data=data['jdsports'])
                  if status is True:
                        message = 'Your raffle entry for the registered email has been successfully registered. Please check your emails for any other verifications from jdsports.co.uk to confirm the entry.'
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