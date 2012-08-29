'''
Created on 2012-8-26

@author: yaoyao

A specific extractor for Amazon.com.
Aimed at extractor product information and comment.
'''

from sys import argv
import cralwer

  
if __name__ == "__main__":
  if len(argv) >= 2:
    url = argv[1]
  else:
    url = "http://www.amazon.com/Samsung-UN46EH6000-46-Inch-1080p-HDTV/dp/B0071O4EKU/ref=pd_ts_zgc_e_3578042011_2?ie=UTF8&s=electronics&pf_rd_p=1367759742&pf_rd_s=right-6&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1E8N6GPA3MX4607DC1T6"
    