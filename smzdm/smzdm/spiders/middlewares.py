# Importing base64 library because we'll need it ONLY in case if the proxy
# we are going to use requires authentication
import base64
from smzdm.settings import *
from scrapy.http import Request, FormRequest

# Start your middleware class


class ProxyMiddleware(object):

    def process_request(self, request, spider):

        print("Request comes here")

