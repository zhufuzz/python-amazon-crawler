'''
Created on 2012-8-26

@author: yaoyao

A amazon specific URL selector.
Manage URL already extracted, extract regularly and URL queue.
'''

import HTMLParser
import urllib2
from bs4 import BeautifulSoup
from sys import argv

# Extract productions from a search page
# or classification product page.
class DepartmentExtract():
  def __init__(self):
    self.search_pattern = ['computer parts & components', 'books']
    self.view_more = ['see more']
    self.department_url = []
    return
  
  def dfs(self, p):
    if 'name' in dir(p) and p.name == 'a' and p.string and \
    HTMLParser.HTMLParser().unescape(p.string).lower() in self.search_pattern:
      url = 'http://www.amazon.com' + p['href']
      if not url in self.department_url:
        self.department_url.append(url)
    if 'contents' in dir(p):
      for c in p.contents:
        self.dfs(c)

  def extract(self, msg):
    soup = BeautifulSoup(msg)
    self.dfs(soup)
    
class ProductListExtract():
  def __init__(self):
    self.production_list = {}
    self.next_page = ''
    
  def dfs_result(self, p):
    if 'name' in dir(p) and p.name == 'a' and \
      'attrs' in dir(p) and 'href' in p.attrs:
      if not 'product-reviews' in p['href']:
        self.production_list[p['href']] = 1
    if 'contents' in dir(p):
      for c in p.contents:
        self.dfs_result(c)
    
  def dfs(self, p):
    if 'name' in dir(p) and p.name == 'a' and \
      p.string and 'next' in p.string.lower():
      self.next_page = p['href']
    if 'name' in dir(p) and p.name == 'div' and \
      'attrs' in dir(p) and 'id' in p.attrs and \
      'result_' in p['id']:
      self.dfs_result(p)
    if 'contents' in dir(p):
      for c in p.contents:
        self.dfs(c)
    
  def extract(self, msg):
    soup = BeautifulSoup(msg)
    self.dfs(soup)

if __name__ == "__main__":
  # Test production list extract.
  url = "http://www.amazon.com/Film-Cameras-Photo/b/ref=amb_link_358884302_66?ie=UTF8&node=499106&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=gp-left-4&pf_rd_r=0H1BK6RNC43VDNHP9KYN&pf_rd_t=101&pf_rd_p=1350383062&pf_rd_i=502394"
  response = urllib2.urlopen(url, timeout = 5000)
  msg = response.read()
  ple = ProductListExtract()
  ple.extract(msg)
  print ple.next_page
  print len(ple.production_list)
  for url in ple.production_list:
    print url
  
  # Test classification page.
  url = "http://www.amazon.com/gp/site-directory/ref=sa_menu_fullstore"
  response = urllib2.urlopen(url, timeout = 5000)
  msg = response.read()
  de = DepartmentExtract()
  de.extract(msg)
  print de.department_url