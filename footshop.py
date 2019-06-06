import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


proxies = ['109.74.142.138:53281']

URL = "https://releases.footshop.com/adidas-yeezy-boost-350-v2-agqn6WoBJZ9y4RSnzw9G"

SHOE_SIZE = ""

EMAIL = ""
PHONE = ""

FIRSTNAME = ""
LASTNAME = ""

COUNTRY=""
ADDRESS = ""
HOUSE_NUMBER = ""
AREA_CODE = ""
CITY = ""

CARD_NUMBER = ""
EXPIRY_MONTH = ""
EXPIRY_YEAR = ""
CVV = ""

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
      
      print(IP_ADDRESS, PORT)
      
      driver = get_driver(IP_ADDRESS, PORT)
      driver.get(URL)
      driver.maximize_window()

      driver.execute_script("window.scrollTo(0, 1040)")
      # shoesize
      timeout = 20
      try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[2]/main/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/span'))
            WebDriverWait(driver, timeout).until(element_present)
      except TimeoutException:
            print ("Timed out waiting for page to load")

      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/span').click()
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[13]').click() # edit last div[i] to dynamically populate the shoe size
      time.sleep(0.5)

      # enter raffle
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/a').click()
      time.sleep(5)

      try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div/div[2]/div/div[1]/div/input'))
            WebDriverWait(driver, timeout).until(element_present)
      except TimeoutException:
            print ("Timed out waiting for page to load")
            
      driver.execute_script("window.scrollTo(0, 1000)")
      
      # contact info
      email = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div/div[2]/div/div[1]/div/input')
      email.send_keys(EMAIL)

      phone = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/input')
      phone.send_keys(PHONE)

      time.sleep(5)
      
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div/div[2]/div/div[3]/button').click()

      try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div/input'))
            WebDriverWait(driver, timeout).until(element_present)
      except TimeoutException:
            print ("Timed out waiting for page to load")

      # name
      firstname = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div/input')
      firstname.send_keys(FIRSTNAME)

      lastname = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[3]/div/input')
      lastname.send_keys(LASTNAME)

      # bithdate
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[1]/button').click()
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[1]/div/button[5]').click() # edit button[i] to dynamically populate the day

      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[2]/button').click()
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div/button[7]').click() # edit button[i] to dynamically populate the month

      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[3]/button').click()
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[3]/div/button[12]').click() # edit button[i] to dynamically populate the year

      driver.execute_script("window.scrollTo(0, 500)")
      time.sleep(5)
      
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[5]/button').click()
      
      try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div/input'))
            WebDriverWait(driver, timeout).until(element_present)
      except TimeoutException:
            print ("Timed out waiting for page to load")

      # delivery details --
      # country
      select = Select(driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[1]/div/select"))
      select.select_by_visible_text(COUNTRY)
      """
      raise NoSuchElementException("Could not locate element with visible text: %s" % text)
      selenium.common.exceptions.NoSuchElementException: Message: Could not locate element with visible text: America
      """
      time.sleep(5)
      
      # street
      address = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[5]/div/div/div[1]/input')
      address.send_keys(ADDRESS)
      """
      raise exception_class(message, screen, stacktrace)
      selenium.common.exceptions.ElementNotInteractableException: Message: Element <input class="form-control input__2V7HN search-input__Aa-1y " type="text"> is not reachable by keyboard
      """
      # house number
      house_number = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[6]/div/input')
      house_number.send_keys(HOUSE_NUMBER)

      # postal code
      postal_code = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[8]/div/input')
      postal_code.send_keys(AREA_CODE)

      # city
      city = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[9]/div/input')
      city.send_keys(CITY)

      # consent - terms and condition
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[10]/div/div/div[1]/label').click()

      driver.execute_script("window.scrollTo(0, 1000)")
      time.sleep(5)

      # submit
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[11]/button').click()
      time.sleep(5)
      

      """
      Add page load try-exception

      """
      driver.execute_script("window.scrollTo(0, 1000)")

      # handling iframe
      frame = driver.find_element_by_xpath('//*[@id="cko-iframe-id"]')
      driver.switch_to.frame(frame)
      
      # credit card details
      credit_card_number = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[1]/input')
      credit_card_number.send_keys(CARD_NUMBER)
      """
      raise exception_class(message, screen, stacktrace)
      selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: /html/body/div/div/div/div/form/div[1]/input
      """
      time.sleep(2)
      
      card_expiry_month = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/div[1]/div/div/div[1]/input')
      card_expiry_month.send_keys(EXPIRY_MONTH)

      card_expiry_year = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/div[1]/div/div/div[2]/input')
      card_expiry_year.send_keys(EXPIRY_YEAR)

      time.sleep(2)
      
      cvv = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/div[2]/div/input')
      cvv.send_keys(CVV)

      time.sleep(2)

      #submit
      driver.switch_to.default_content()
      time.sleep(2)
      
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/div[3]/button[1]').click()

      try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/div[3]/button[1]'))
            WebDriverWait(driver, timeout).until(element_present)
      except TimeoutException:
            print ("Timed out waiting for page to load")

      driver.execute_script("window.scrollTo(0, 1000)")
      time.sleep(2)
      
      #finish
      driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div[2]/div[2]/div[3]/button[1]').click()

      
