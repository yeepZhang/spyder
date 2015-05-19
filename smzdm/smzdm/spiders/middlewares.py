# Importing base64 library because we'll need it ONLY in case if the proxy
# we are going to use requires authentication
import base64
from smzdm.settings import *
from scrapy.http import Request, FormRequest

# Start your middleware class


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        # proxy_ip_port = "115.29.202.148:8888"
        # # proxy_user_pass = "awesome:dude"
        # # Set the location of the proxy
        # request.meta['proxy'] = "http://%s" % proxy_ip_port

        print("I'm in the Process_Request")

