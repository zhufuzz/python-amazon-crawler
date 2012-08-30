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

if __name__ == "__main__":
  # Test classification page.
  url = "http://www.amazon.com/gp/site-directory/ref=sa_menu_fullstore"
  response = urllib2.urlopen(url, timeout = 5000)
  msg = response.read()
  de = DepartmentExtract()
  de.extract(msg)
  print de.department_url