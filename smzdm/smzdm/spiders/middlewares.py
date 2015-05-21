# -*-coding:utf-8-*-

from scrapy import log
import random
import requests
import re
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy.http import Request, FormRequest
from smzdm.settings import *

# ip proxy
class ProxyMiddleware(object):

    def process_request(self, request, spider):
        print("TODO with the IP proxy")


# user-agent rotate
class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent
        self.headers = HEADER
        self.user_agent_list = USER_AGENTS

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            self.headers.setdefault('User-Agent', ua)
        for key in self.headers:
            request.headers.setdefault(key, self.headers[key])
        print("RotateUserAgentMiddleware")


# cookie generation
class GenerateCookie():
    def __init__(self):
        self.headers = HEADER
        self.cookies = COOKIES
    def process_request(self, request, spider):
        r = requests.get('http://www.smzdm.com/', headers=self.headers, cookies=self.cookies)
        if r.status_code == 521:
            print "this is 521"
            e = 'c.push\("(.*?)"\)'
            m = re.findall(e, r.content)
            c = ''.join(m)
            print c
            self.cookies['__jsl_clearance'] = c
        for key in self.cookies:
            request.cookies[key] = self.cookies[key]