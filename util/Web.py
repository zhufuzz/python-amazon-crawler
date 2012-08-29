'''
Created on Mar 27, 2010

@author: julius
'''
import sys
import urllib2
import time

class Web:
    '''
    simulate a browser to visit twitter
    '''
    def __init__(self, headers):
        '''
        Constructor
        '''
        self.headers = headers
    
    def getHtmlRetry(self, url, retry=0):
        if retry <= 0: retry = 5 # default retry 20 times.
        html = None
        source = None
        retry_count = 0
        while retry > 0:
            retry -= 1
            retry_count += 1

            error_msg = None
            try:
                time.sleep(0.5)
                req = urllib2.Request(url, None, self.headers)
                res = urllib2.urlopen(req)
                source = res.read()
                

            except urllib2.HTTPError, e:
                error_msg = "Error [%s, %s]" % (e, "")
            except urllib2.URLError, e:
                error_msg = "Error [%s, %s]" % (e.reason, "")
            except Exception, e:
                print '-------------------------'
                error_msg = "Error [%s, %s]" % (sys.exc_info(), "")
                import traceback
                traceback.print_exc()
                print 'trace-------------------------trace'

            if error_msg is None :
                return source
            else:
                print error_msg

        #~ end while

        if retry == 0:
            return None # meet max retry times. also None

        print "should not be here."
        return None
    
if __name__ == '__main__':
    
    cookie = '__utma=43838368.1149310522.1262412702.1269612588.1269695495.11; __utmz=43838368.1262412702.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=43838368.lang%3A%20en; __qca=P0-2060112157-1268910696397; auth_token=1269591657%7C4f45f046b0d2ce733bdbc26d57d35c6ec394e937; guest_id=1269695487536; lang=en; _twitter_sess=BAh7DjoTcGFzc3dvcmRfdG9rZW4iLTk3ZjZhOGU2OWMzODIyMTdiMjAxM2Ji%250ANjhlMTUxNTE0ZDAyNGNjMTA6FWluX25ld191c2VyX2Zsb3cwOhF0cmFuc19w%250Acm9tcHQwOg9jcmVhdGVkX2F0bCsITJ6%252FnycBOgl1c2VyaQRuvz0BIgpmbGFz%250AaElDOidBY3Rpb25Db250cm9sbGVyOjpGbGFzaDo6Rmxhc2hIYXNoewAGOgpA%250AdXNlZHsAOgdpZCIlNjM4NDQxNGQ4OWUxYTlhN2YyMGM0OTQwZmM3ODIyMjgi%250AJ3Nob3dfZGlzY292ZXJhYmlsaXR5X2Zvcl9KdWxpdXN0Y2gwOgxjc3JmX2lk%250AIiU4MjVlNGU4YTBhMzgyNDkxNGE0ZDY2NjQ1M2Q1MmMzZA%253D%253D--94466103ec87cfa7fb2bec5ab18cec293d7c9029; __utmb=43838368.4.10.1269695495; __utmc=43838368; original_referer=4bfz%2B%2BmebEkRkMWFCXm%2FCUOsvDoVeFTl'
    
    url = 'http://twitter.com/BillGates'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.8) Gecko/20100214 Ubuntu/9.10 (karmic) Firefox/3.5.8'
    headers['Cookie'] = cookie
        
    req = urllib2.Request(url, None, headers)
    res = urllib2.urlopen(req)
    content = res.read()
    print content
    print 'new test'
    test = Web(cookie)
    req = test.getHtmlRetry(url)
    print req
    
