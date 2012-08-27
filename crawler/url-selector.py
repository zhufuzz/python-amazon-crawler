'''
Created on 2012-8-26

@author: yaoyao

A general URL selector.
'''

from collections import deque
from datetime import datetime
from threading import Thread, Lock

class URLSelector(object):
  # TODO(yaoyao): modify URL selector so that store all the information
  # in a database instead of memory.
  # In queue, each element is a pair (time, URL)
  def __init__(self, lock):
    self.log_filename = "..\log.txt"
    self.writer = open(self.log_filename, 'a')
    self.finish_dict = {}
    self.url_queue = deque()
    self.mutex = lock
  
  # Ask URL selector to pick up a URL from queue.
  def pickurl(self):
    self.mutex.acquire()
    url_pair = self.url_queue.popleft()
    url = url_pair[1]
    self.finish_dict[url] = 1
    self.log("pick", url)
    self.mutex.release()
    return url
  
  # Ack URL selector to put URL in queue.
  def inserturl(self, url):
    self.mutex.acquire()
    time = str(datetime.now())
    if not url in self.finish_dict:
      self.url_queue.append((time, url))
      self.log("insert", url)
    self.mutex.release()
    return
  
  # Ack URL selector that controller has finished extracting URL.
  def finishurl(self, url):
    self.mutex.acquire()
    self.finish_dict[url] = 2
    self.log("finish", url)
    self.mutex.release()
    return
  
  def log(self, msg, url):
    self.writer.write(msg + ":\t" + url + "\n")
    self.writer.flush()

if __name__ == "__main__":
  lock = Lock()
  url_selector = URLSelector(lock)
  url_selector.inserturl("a")
  print url_selector.pickurl()