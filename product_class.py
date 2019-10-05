import time
import math

from amazon_parser import Amazon_parser

class Product(object):
  def __init__(self, product_name, single_dict):
    self.product_name = product_name
    self.currency = single_dict["currency"]
    self.user_desired_price = single_dict['desired_price']
    self.product_url = single_dict['url']
    self.site = single_dict['site']
    self.latest_price = -1
    self.is_deal = False
    self.price_last_updated = 0
    self.update_duration = 20
    # Once we have got the product at the desired price then we will stop checking it
    # Otherwise the mailbox will be filled with the messages of price lowering
    self.stop_checking = False

    if self.site == "amazon":
      self.parser = Amazon_parser(self.product_url, product_name)

  def __str__(self):
    self.update_price()
    string_to_return = ""
    price_valid , actual_price = self.get_valid_price()
    string_to_return = string_to_return + "\nProduct Name : {}".format(self.product_name)
    if price_valid:
      string_to_return = string_to_return + "\nProduct_Price : {}".format(actual_price)
      string_to_return = string_to_return + "\nDeal : {}".format(self.is_deal_there())
      string_to_return = string_to_return + "\nProduct price is lower than desired : {}".format(self.is_price_lower_than_desired())
    else:
      string_to_return = string_to_return + "\nUnable to fetch latest price check log for more information"
    
    return string_to_return

  def get_price(self):
    try :
      self.is_deal, self.latest_price = self.parser.get_price()
    except Exception as e:
      print ("exception occured, see logs for more information")
      return False
    return True

  def stop_checking_product_details(self):
    self.stop_checking = True

  def update_price(self):
    if (time.time() > self.price_last_updated + self.update_duration) and not(self.stop_checking) :
      print("updating price")
      if self.get_price() != None:
        self.price_last_updated = time.time()
        return True
      else:
        return False
    else:
      print ("not updating price update duration is not met")

  def is_deal_there(self):
    if self.update_price() and self.get_valid_price()[0]:
      return self.is_deal
    else:
      return None

  def get_valid_price(self):
    if self.latest_price == -1:
      return False, math.inf
    return True, self.latest_price

  def is_price_lower_than_desired(self):
    if self.user_desired_price > self.get_valid_price()[1]:
      return True
    else:
      return False