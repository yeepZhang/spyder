import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from smzdm.settings import *
from smzdm.items import SmzdmItem
import requests
import re


class SmzdmSpider(scrapy.spider.Spider):
    # use for identify
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    # start urls
    start_urls = [
        "http://www.smzdm.com"
    ]
    # first function

    def __init__(self):
        self.headers = HEADER
        self.cookies = COOKIES

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}
            session = requests.session()
            session.headers = headers
            r = session.get('http://www.smzdm.com/')
            if r.status_code == 521:
                print "521521521521521521521521"
                e = 'c.push\("(.*?)"\)'
                m = re.findall(e, r.content)
                c = ''.join(m)
                session.cookies['__jsl_clearance'] = c
                self.cookies = {
                    "smzdm_user_view": "6828E4331C912B168F50803A1C59A785",
                    "smzdm_user_source": "60F20212EA682941C06BFB53E49954E2",
                    "bdshare_firstime": "1431856149939",
                    "__gads": "ID=e0f6d17f80de1fe8:T=1431856151:S=ALNI_MYYpFm0RwFPLzP48SaQkwAJTuWDrg",
                    "__jsluid": "83575169159cdbd4ce33d2f282b56355",
                    "__jsl_clearance": "1432012100.711|0|%2bLGS6QjRCKXuh%2bnjBAiTrnQjZto%3d",
                    "PHPSESSID": "q40svo85u86cri7k0u6frbds91",
                    "_gat": "1",
                    "_ga": "GA1.2.1557700789.1431856150",
                    "amvid": "23c56ca37c1e3664035bdeb41e292a5f",
                    "Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58": "1431856150,1431873256,1432012104",
                    "Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58": "1432014480",
                    "AJSTAT_ok_pages": "8",
                    "AJSTAT_ok_times": "100"
                }
                self.cookies['__jsl_clearance'] = c
            yield FormRequest(url, meta={'cookiejar': i, 'proxy': "http://115.29.202.148:8888"}, headers=self.headers, cookies=self.cookies, callback=self.parse)
    # overwrite process request
    def parse(self, response):
        hxs = Selector(response)
        sites = hxs.xpath("//div[@class='list ']")
        for site in sites:
            item = SmzdmItem()
            item['title'] = site.xpath(".//h4/a/text()").extract()[0]
            item['price'] = site.xpath(".//h4/a/span/text()").extract()[0]
            _brief = site.xpath(
                ".//div[@class='lrInfo']/strong/text()").extract()
            item['brief'] = _brief.__len__() > 0 and _brief[0] or ""
            item['description'] = site.xpath(
                ".//div[@class='lrInfo']/text()").extract()[0]
            item['up'] = site.xpath(
                ".//a[@class='good']//em/text()").extract()[0]
            item['down'] = site.xpath(
                ".//a[@class='bad']//em/text()").extract()[0]
            item['sitename'] = site.xpath(
                ".//div[@class='botPart']/a/text()").extract()[0]
            item['buylink'] = site.xpath(
                ".//div[@class='buy']/a/@href").extract()[0]
            yield item

    def prn_obj(obj):
        print ', '.join(['%s:%s' % item for item in obj.__dict__.items()])
