import urllib
import urllib2
import cookielib
from urllib2 import HTTPError
import traceback

from django.test import Client

# c = Client()
# response = c.post('/login/', {'username': 'john', 'password': 'smith'})
# response.status_code
try:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)
    req = urllib2.Request("http://django-ex-jixuduxing.1d35.starter-us-east-1.openshiftapps.com/weixin")
    req.add_data(urllib.urlencode({"username":"root","password":"ROOTXXOO"}))
    req.add_header("Referer", "www.baidu.com")
    req.add_header("Cookie", "csrftoken=HUQYHNYCbEetb96FqsCdhzfNSjAnQfW3")
    print req

    print req.get_method()
    resp = urllib2.urlopen(req)
    print resp.read()
except HTTPError,e:
    traceback.print_exc()
    print e
    print 'info:',e.info()
