import requests
import bs4
from config import DEBUG, HEADERS

class Amazon_parser(object):
  def __init__(self, url, product_name = "unknown_product"):
    self.url = url
    self.product_name = product_name
    self.current_session = requests.session()

  def get_price(self):
    r = self.current_session.get(self.url, headers = HEADERS)
    if DEBUG:
      with open(self.product_name + ".txt", "w") as f:
        f.write(r.content.decode("utf-8"))

    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    deal= False
    price = soup.find('span', id ='priceblock_ourprice') 
    if price == None:
      deal = True
      price = soup.find('span', id ='priceblock_dealprice') 
    for a_price in price:
      formatted_price = a_price
    currency = formatted_price[0]
    formatted_price = formatted_price.replace(currency, "")
    formatted_price = formatted_price.replace(",", "")
    formatted_price = float(formatted_price)
    return deal, formatted_price