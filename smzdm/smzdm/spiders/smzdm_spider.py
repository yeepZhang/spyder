import scrapy
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector
from smzdm.settings import *
from smzdm.items import SmzdmItem
class SmzdmSpider(scrapy.spider.Spider):
  #use for identify
  name = "smzdm"
  allowed_domains = ["smzdm.com"]
  #start urls
  start_urls = [
    "http://www.smzdm.com"
  ]
  def __init__(self):
      self.headers =HEADER
      self.cookies =COOKIES

  def start_requests(self):
      for i, url in enumerate(self.start_urls):
          yield FormRequest(url, meta = {'cookiejar': i}, headers = self.headers, cookies =self.cookies, callback = self.parse)

  #first function
  def parse(self, response):
    # filename = response.url.split("/")[-2]
    # with open(filename, 'wb') as f:
    #   f.write(response.body)
    hxs = Selector(response)
    sites = hxs.xpath("//div[@class='list ']")
    for site in sites:
      item = SmzdmItem()
      item['title'] = site.xpath(".//h4/a/text()").extract()[0]
      item['price'] = site.xpath(".//h4/a/span/text()").extract()[0]
      _brief = site.xpath(".//div[@class='lrInfo']/strong/text()").extract()
      item['brief'] = _brief.__len__() > 0 and _brief[0] or ""
      item['description'] = site.xpath(".//div[@class='lrInfo']/text()").extract()[0]
      item['up'] = site.xpath(".//a[@class='good']//em/text()").extract()[0]
      item['down'] = site.xpath(".//a[@class='bad']//em/text()").extract()[0]
      item['sitename'] = site.xpath(".//div[@class='botPart']/a/text()").extract()[0]
      item['buylink'] = site.xpath(".//div[@class='buy']/a/@href").extract()[0]
      yield item

