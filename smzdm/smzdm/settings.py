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

HEADER={
    "Host": "www.smzdm.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    # "Cookie": "smzdm_user_view=CF7115FB4CEC9B7499012F321D943A94; smzdm_user_source=ABBBFC77346006B56E2F340A369C2D59; __gads=ID=34f9a42d8ab14fb5:T=1431141129:S=ALNI_Mb1qII3JnS3YLvumXnd3jHyww8XYQ; __jsluid=e06542f320bbe2a51ca9d46b2d740f4d; __jsl_clearance=1431144004.065|0|Hl77q0br6dDyultqERYY3%2flcF%2f4%3d; _ga=GA1.2.1411156519.1431144006; _gat=1; amvid=bfb5713115f9d9134e1fb6399a7a8148; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1431141130,1431142911; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1431144007; AJSTAT_ok_pages=1; AJSTAT_ok_times=1; PHPSESSID=h71g7g91d1p0ktluqf7214j5m5; bdshare_firstime=1431144007780",
    "RA-Ver": "2.10.3",
    "RA-Sid": "6545CE18-20150112-150450-4f16d4-b9e68f"
    }

COOKIES={
    # 'smzdm_user_view':r'CF7115FB4CEC9B7499012F321D943A94',
    # 'smzdm_user_source':r'ABBBFC77346006B56E2F340A369C2D59',
    # '__gads':r'ID=34f9a42d8ab14fb5:T=1431141129:S=ALNI_Mb1qII3JnS3YLvumXnd3jHyww8XYQ',
    '__jsluid':r'e06542f320bbe2a51ca9d46b2d740f4d',
    '__jsl_clearance':r'1431264612.787|0|BwAkP4h%2bACjxECHqfTmEuMhzrj4%3d',
    # '_ga':r'GA1.2.1411156519.1431144006',
    # '_gat':r'1',
    # 'amvid':r'bfb5713115f9d9134e1fb6399a7a8149',
    # 'Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58':r'1431141130,1431142911',
    # 'Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58':r'1431144109',
    # 'AJSTAT_ok_pages':r'2',
    # 'AJSTAT_ok_times':r'1',
    # 'PHPSESSID':r'h71g7g91d1p0ktluqf7214j5m5',
    # 'bdshare_firstime':r'1431144007780'
}

ITEM_PIPELINES = ['smzdm.pipelines.SmzdmPipeline',]

MONGODB_SERVER = "localhost"
MONGODB_PROT = 27017
MONGODB_DB = "smzdm"
MONGODB_COLLECTION = "products"


