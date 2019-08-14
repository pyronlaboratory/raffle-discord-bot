import tldextract
import json


def update_dictionary(domain, link):
      with open(r"/app/raffle_form/scripts/tools/config/urls.json", "r") as json_input: # update address on production server
            url_dictionary = json.load(json_input)
            url_dictionary[domain] = link
            json_input.close()
      with open(r"/app/raffle_form/scripts/tools/config/urls.json", "w") as json_output: # update address on production server
            json.dump(url_dictionary, json_output)
            json_output.close()

          
def is_update_required(domain, link):
      with open(r"/app/raffle_form/scripts/tools/config/urls.json") as json_file: # update address on production server
            url_dictionary = json.load(json_file)
            link_dictionary = url_dictionary[domain]
            if link == link_dictionary:
                  json_file.close()
                  return False
            else:
                  json_file.close()
                  return True

      
def load_url(domain_passed):
      links = open(r"/app/links.txt","r") # update address on production server
      if links.mode == "r":
            for link in links:
                  if len(link) > 1:
                        link = link.strip()
                        extract = tldextract.extract(link)
                        domain =  extract.domain
                        if domain_passed == domain: # domain found in the links.txt
                              update = is_update_required(domain, link)
                              if update is False:
                                    return link
                              else:
                                    update_dictionary(domain, link)
                                    return link
      with open(r"/app/raffle_form/scripts/tools/config/urls.json") as json_file:
            url_dictionary = json.load(json_file)
            if len(url_dictionary[domain_passed]) > 1:
                  return url_dictionary[domain_passed]
            json_file.close()
