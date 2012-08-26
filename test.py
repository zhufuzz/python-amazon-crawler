import sys
import re
import urllib2
import urlparse
tocrawl = []
keywordregex = re.compile('<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
linkregex = re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')

crawling = "http://www.amazon.com/Samsung-UN46EH6000-46-Inch-1080p-HDTV/dp/B0071O4EKU/ref=pd_ts_zgc_e_3578042011_2?ie=UTF8&s=electronics&pf_rd_p=1367759742&pf_rd_s=right-6&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1E8N6GPA3MX4607DC1T6"
url = urlparse.urlparse(crawling)
response = urllib2.urlopen(crawling)
msg = response.read()
startPos = msg.find('<title>')
if startPos != -1:
  endPos = msg.find('</title>', startPos+7)
  if endPos != -1:
    title = msg[startPos+7:endPos]
    print title
    
  keywordlist = keywordregex.findall(msg)
  if len(keywordlist):
    keywordlist = keywordlist[0]
    keywordlist = keywordlist.split(",")
    print keywordlist
    
  links = linkregex.findall(msg)
  for link in (links.pop(0) for _ in xrange(len(links))):
    if link.startswith('/'):
      link = 'http://' + url[1] + link
    elif link.startswith('#'):
      link = 'http://' + url[1] + url[2] + link
    elif not link.startswith('http'):
      link = 'http://' + url[1] + '/' + link
    tocrawl.append(link)
  print len(tocrawl)
  print tocrawl