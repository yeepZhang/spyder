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
DOWNLOAD_DELAY = 5
# DOWNLOADER_HTTPCLIENTFACTORY = 'smzdm.spiders.HTTPClientFactory.ScrapyHTTPClientFactory'

# SPIDER_MIDDLEWARES = {
# }
# COOKIES_ENABLED = False
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'smzdm.spiders.middlewares.ProxyMiddleware': 100,
    'smzdm.spiders.middlewares.RotateUserAgentMiddleware': 400,
    'smzdm.spiders.middlewares.GenerateCookie': 500,

}
HEADER = {
    'Host':'www.smzdm.com',
    'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5',
    'Referer':'http://www.smzdm.com/',
    'X-Moz':'prefetch',
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

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
   ]
ITEM_PIPELINES = ['smzdm.pipelines.SmzdmPipeline']

MONGODB_SERVER = "localhost"
MONGODB_PROT = 27017
MONGODB_DB = "smzdm"
MONGODB_COLLECTION = "products"


