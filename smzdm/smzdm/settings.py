# -*- coding: utf-8 -*-

# Scrapy settings for smzdm project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'smzdm'

SPIDER_MODULES = ['smzdm.spiders']
NEWSPIDER_MODULE = 'smzdm.spiders'
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'
DOWNLOAD_DELAY = 1
# DOWNLOADER_HTTPCLIENTFACTORY = 'smzdm.spiders.HTTPClientFactory.ScrapyHTTPClientFactory'

# DOWNLOADER_MIDDLEWARES = {
#         'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
#         'smzdm.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
#     }
# SPIDER_MIDDLEWARES = {
# }
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'smzdm.spiders.middlewares.ProxyMiddleware': 100,

}
HEADER = {
    'Host':'www.smzdm.com',
    'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5',
    'Referer':'http://www.smzdm.com/',
    'X-Moz':'prefetch',
    # 'Cookie':'smzdm_user_view=D04B3B9F888FF9914BFF14C211E72CDF; smzdm_user_source=B8D75F68C77E71DB025CE90E97B78825; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1431347558,1431837605,1432019844,1432090884; AJSTAT_ok_times=5; bdshare_firstime=1431347557980; __gads=ID=03c0a840645fa406:T=1431347558:S=ALNI_Mb6SNihVUmjzcOKplzzzRMh1kpB9Q; _ga=GA1.2.1757472345.1431837605; __jsluid=c02c1ca291ef064f53a485866b8496ea; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1432100049; PHPSESSID=5nhqql3r5hm67nu6c55qphmbk0; amvid=168f872f0a75eb2b32af5b51166ba3ce; __jsl_clearance=1432106829.897|0|0OWmEwuEjkVaVnkGNcMU4WFvyhc%3d'
}

COOKIES={
    'smzdm_user_view':'D04B3B9F888FF9914BFF14C211E72CDF',
    'smzdm_user_source':'B8D75F68C77E71DB025CE90E97B78825',
    'Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58':'1431347558,1431837605,1432019844,1432090884',
    'AJSTAT_ok_times':'6',
    'bdshare_firstime':'1431347557980',
    '__gads':'ID=03c0a840645fa406:T=1431347558:S=ALNI_Mb6SNihVUmjzcOKplzzzRMh1kpB9Q',
    '_ga':'GA1.2.1757472345.1431837605',
    '__jsluid':'c02c1ca291ef064f53a485866b8496ea',
    'Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58':'1432107897',
    'PHPSESSID':'5nhqql3r5hm67nu6c55qphmbk0',
    'amvid':'e28bad91896de6f7e5d8b219385d6916'
}
ITEM_PIPELINES = ['smzdm.pipelines.SmzdmPipeline']

MONGODB_SERVER = "localhost"
MONGODB_PROT = 27017
MONGODB_DB = "smzdm"
MONGODB_COLLECTION = "products"


