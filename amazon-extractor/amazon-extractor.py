'''
Created on 2012-8-26

@author: yaoyao

A specific extractor for Amazon.com.
Aimed at extractor product information and comment.
'''

import HTMLParser
import urllib2
from bs4 import BeautifulSoup
from sys import argv

# Extract product informations such as:
# Product Details, Features, and Description
# Filter tags such as script, style.
class ProductExtract():
  def __init__(self):
    self.search_pattern = ['Product Details', 'Product Features', 'Product Description']
    self.filter_pattern = ['script', 'style']
    self.dict = {}
    self.clear()
    
  def loadcontent(self, p, case):
    if 'name' in dir(p) \
      and p.name in self.filter_pattern:
      return
    if type(p).__name__ == 'NavigableString':
      p = HTMLParser.HTMLParser().unescape(p)
      p = p.strip()
      if len(p) > 0:
        self.dict[case] = self.dict[case] + ' ' + unicode(p)
    if 'contents' in dir(p):
      for c in p.contents:
        self.loadcontent(c, case)
      
  def dfs(self, p):
    if 'string' in dir(p) \
      and 'parent' in dir(p) \
      and p.string in self.search_pattern:
      if not p.string in self.dict:
        self.dict[p.string] = ''
      self.loadcontent(p.parent, p.string)
    if 'contents' in dir(p):
      for c in p.contents:
        self.dfs(c)

  def clear(self):
    self.title = ''
    self.dict = {}
    
  def extract(self, msg):
    soup = BeautifulSoup(msg)
    self.title = soup.title.string
    self.dfs(soup.body)
    
# Extract user comment for a product.
class CommentExtract():
  def __init__(self):
    return
  
# Extract productions from a search page
# or classification product page.
class SearchExtract():
  def __init__(self):
    return
  
if __name__ == "__main__":
  # Test product extract.
  if len(argv) >= 2:
    url = argv[1]
  else:
    url = "http://www.amazon.com/Samsung-UN46EH6000-46-Inch-1080p-HDTV/dp/B0071O4EKU/ref=pd_ts_zgc_e_3578042011_2?ie=UTF8&s=electronics&pf_rd_p=1367759742&pf_rd_s=right-6&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1E8N6GPA3MX4607DC1T6"
  response = urllib2.urlopen(url, timeout = 5000)
  msg = response.read()
  pe = ProductExtract()
  pe.extract(msg)
  print pe.title
  print pe.dict
