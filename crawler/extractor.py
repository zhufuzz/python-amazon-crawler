'''
Created on 2012-8-26

@author: yaoyao

A general page source extractor.
Extract page source and the links in page source.
'''

import re
import urllib2
import urlparse

# Parse the URL and return (1, url_parse, page source).
# return (0, URL, exception message) for exception.
def pageextractor(url):
  try:
    url_parse = urlparse.urlparse(url)
    response = urllib2.urlopen(url, timeout = 5000)
    msg = response.read()
    return 1, url_parse, msg
  except Exception as e:
    return 0, url, Exception(e).message
    
# Parse the page source and return (1, a list of URLs).
# return (0, exception message) for exceptions.
linkregex = re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')
def urlextractor(url_parse, msg):
  try:
    links = linkregex.findall(msg)
    url_list = []
    for link in links:
      if link.startswith('/'):
        link = 'http://' + url_parse[1] + link
      elif link.startswith('#'):
        # Currently, we don't do extract for # tag.
        #link = 'http://' + url_parse[1] + url_parse[2] + link
        continue
      elif not link.startswith('http'):
        link = 'http://' + url_parse[1] + '/' + link
      url_list.append(link)
    return 1, url_list;
  except Exception as e:
    return 0, url_parse[1] + '\t' + Exception(e).message

if __name__ =="__main__":
  msg = pageextractor("http://www.amazon.com/Samsung-UN46EH6000-46-Inch-1080p-HDTV/dp/B0071O4EKU/ref=pd_ts_zgc_e_3578042011_2?ie=UTF8&s=electronics&pf_rd_p=1367759742&pf_rd_s=right-6&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1E8N6GPA3MX4607DC1T6")
  print msg[0], msg[1], len(msg[2])
  msg = urlextractor(msg[1], msg[2])
  print msg
  print len(msg[1])
  msg = pageextractor("http://no/such/website")
  print msg