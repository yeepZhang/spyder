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
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'smzdm.spiders.middlewares.ProxyMiddleware': 100,

}
HEADER={
    "Host": "www.smzdm.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "RA-Ver": "2.10.3",
    "RA-Sid": "6545CE18-20150112-150450-4f16d4-b9e68f"
    }

COOKIES={
    '__jsluid':r'83575169159cdbd4ce33d2f282b56355',
    '__jsl_clearance':r'1432012100.711|0|%2bLGS6QjRCKXuh%2bnjBAiTrnQjZto%3d'
}
ITEM_PIPELINES = ['smzdm.pipelines.SmzdmPipeline',]

MONGODB_SERVER = "localhost"
MONGODB_PROT = 27017
MONGODB_DB = "smzdm"
MONGODB_COLLECTION = "products"


