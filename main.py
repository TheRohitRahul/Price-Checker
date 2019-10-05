import math
import time
from config import DEBUG

from product_list import product_dict
from product_class import Product
from mail_handler import GMail

def build_product_list(product_dict):
  list_of_products = []
  for a_product in product_dict:
    list_of_products.append(Product(a_product, product_dict[a_product]))
  return list_of_products


 
if __name__ == "__main__":
  
    all_products = build_product_list(product_dict)
    m_client = GMail()
    while(True):
      for a_product in all_products:
        print(str(a_product))
        # Mail will only be sent once 
        if a_product.is_price_lower_than_desired() and not(a_product.stop_checking):
          subject = "Price down for {}".format(a_product.product_name)
          body = "Price for {} is {} which is lower than your desired price :  {}".format(a_product.product_name, a_product.get_valid_price()[1], a_product.user_desired_price )
          m_client.send_mail(subject, body)
          print("mail sent")
          a_product.stop_checking_product_details()
      time.sleep(60)    