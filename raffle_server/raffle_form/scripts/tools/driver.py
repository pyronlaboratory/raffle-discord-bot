import os
import logging
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *

'''
def load_chrome_driver(proxy):
      print('Creating chrome_driver')
      options = Options()

      options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

      options.add_argument('--headless')
      options.add_argument('--disable-gpu')
      options.add_argument('--no-sandbox')
      options.add_argument('--remote-debugging-port=9223')
      options.add_argument('--proxy-server='+proxy)
      try:
        chrome_driver = webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), chrome_options=options)
        return chrome_driver
      except Exception as e:
        print(type(e))
        print('printed log: '+str(e))
        print('--Logging--')
        logging.exception("message")
'''
def load_firefox_driver(proxy):
      print('Creating firefox_driver')
      options = webdriver.FirefoxOptions()
      options.log.level = "trace"
      options.add_argument('-headless')
      options.add_argument('-disable-gpu')
      options.add_argument('-no-sandbox')
      options.add_argument('-remote-debugging-port=9224')
      
      binary = FirefoxBinary(str(os.environ.get('FIREFOX_BIN')))
      
      anonymizer = Proxy({
          'proxyType': ProxyType.MANUAL,
          'httpProxy': proxy,
          'ftpProxy': proxy,
          'sslProxy': proxy
      })
      
      try:
        firefox_driver = webdriver.Firefox(firefox_binary=binary,executable_path=str(os.environ.get('GECKODRIVER_PATH')), proxy=anonymizer, firefox_options=options)
        return firefox_driver
      except Exception as e:
        print(type(e))
        print('printed log: '+str(e))
        print('--Logging--')
        logging.exception("message")


      

      

      

      

