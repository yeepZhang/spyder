import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from smzdm.settings import *
from smzdm.items import SmzdmItem
import requests
import re


class SmzdmSpider(scrapy.Spider):
    # use for identify
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    # start urls
    start_urls = [
        "http://www.smzdm.com/p1",
    ]
    # first function

    def __init__(self):
        self.headers = HEADER
        self.cookies = COOKIES

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url)
    # overwrite process request

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        hxs = Selector(response)
        sites = hxs.xpath("//div[@class='list ']")
        for site in sites:
            item = SmzdmItem()
            self.get_value(site, item, 'title', ".//h4/a/text()")
            self.get_value(site, item, 'price', "//h4/a/span/text()")
            self.get_value(site, item, 'brief', ".//div[@class='lrInfo']/strong/text()")
            self.get_value(site, item, 'description', ".//div[@class='lrInfo']/text()")
            self.get_value(site, item, 'up', ".//a[@class='good']//em/text()")
            self.get_value(site, item, 'down', ".//a[@class='bad']//em/text()")
            self.get_value(site, item, 'sitename', ".//div[@class='botPart']/a/text()")
            self.get_value(site, item, 'buylink', ".//div[@class='buy']/a/@href")
            yield item

    def prn_obj(obj):
        print ', '.join(['%s:%s' % item for item in obj.__dict__.items()])

    def get_value(self, site, item, key, xpath):
        _key = site.xpath(xpath).extract()
        item[key] = _key.__len__() > 0 and _key[0] or ""