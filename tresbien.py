import requests
from time import sleep

requests.packages.urllib3.disable_warnings()

# Add these values
API_KEY = ''  #  2captcha API KEY

site_key = ''  # site-key for g-recaptcha

url = 'https://tres-bien.com/adidas-yeezy-boost-350-v2-black-fu9006-fw19'  

header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://tres-bien.com/adidas-yeezy-boost-350-v2-black-fu9006-fw19",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
proxy = {IP_ADDRESS:PORT}  #proxy

proxy = {'http': 'http://' + proxy, 'https': 'https://' + proxy}

#s = requests.Session()

# here we post site key to 2captcha to get captcha ID (and we parse it here too)
captcha_id = requests.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url),
                           headers=header).text.split('|')[1]

#print(captcha_id)

# then we parse gresponse from 2captcha response
recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id),headers=header).text
print("solving ref captcha...")
while 'CAPCHA_NOT_READY' in recaptcha_answer:
    sleep(15)
    recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id),headers=header).text
recaptcha_answer = recaptcha_answer.split('|')[1]

#print(recaptcha_answer)

header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://tres-bien.com/adidas-yeezy-boost-350-v2-black-fu9006-fw19",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

payload = {
      "form_key":"1UGlG3F69LytBaMF",
      "sku":"adi-fw19-003",
      "fullname": "somename",
      "email": "ro.n.nie94official@gmail.com",
      "address": "someaddress",
      "zipcode": "somearea",
      "city": "somecity" ,
      "country": "somecountry",
      "phone": "9049945383",
      "Size_raffle":"US_11",
      "gresponse": recaptcha_answer
}

r = requests.post('https://tres-bien.com/tbscatalog/manage/rafflepost/', headers=header, verify=False, files=payload)
print(r.status_code)

