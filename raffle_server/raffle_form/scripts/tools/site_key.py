import cfscrape
import requests
from bs4 import BeautifulSoup as bs

def get_site_key(url):
      scraper = cfscrape.create_scraper()
      response = scraper.get(url)
      soup = bs(response.text, "html.parser")
      sitekey = ""
      try:
            sitekey = soup.find("div", class_="g-recaptcha")["data-sitekey"]
      except:
            pass
      
      return sitekey
