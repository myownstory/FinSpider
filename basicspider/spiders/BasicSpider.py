# __author__ = 'yueguo'
# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from basicspider.items import F10Item
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MyTest(scrapy.Spider):
    name="f10"
    # start_urls = ['http://f10.eastmoney.com/f10_v2/BusinessAnalysis.aspx?code='+l.strip() for l in open('allcodes','r').readlines()]
    # start_urls = ['http://f10.eastmoney.com/f10_v2/BusinessAnalysis.aspx?code=sz000002']

    def __init__(self):
        with open('allcodes', 'r') as f:
            self.start_urls = ['http://f10.eastmoney.com/f10_v2/BusinessAnalysis.aspx?code='+l.strip() for l in f.readlines()]

    def parse(self, response):
        item = F10Item()
        selector = Selector(response)
        # rowcount = selector.xpath('//td[@class="tips-fieldnameL"]/@rowspan')[0].extract()
        # print "hello",int(rowcount)

        firstMajor = selector.xpath('//td[@class="tips-fieldnameL"]')[0]

        majorname = firstMajor.xpath('following-sibling::node()/text()')[0].extract()
        majorvol = firstMajor.xpath('following-sibling::node()/text()')[1].extract()
        majorpcnt = firstMajor.xpath('following-sibling::node()/text()')[6].extract()
        majormao = firstMajor.xpath('following-sibling::node()/text()')[7].extract()
        # print majorname,majorvol,majorpcnt

        item['name'] = selector.xpath('//p[@class="key"]//a/text()')[0].extract().strip()

        item['code'] = selector.xpath('//p[@class="key"]//a/text()')[1].extract().strip()

        item['majorname'] = majorname.strip()

        item['majorpcnt'] = majorpcnt.strip()
        item['majorvol'] = majorvol.strip()
        item['majormao'] = majormao.strip()
        # for i in range(int(rowcount)):
        #     print i
        # table1 = selector.xpath('/html/body/div[1]/div[13]/div[2]/table[1]')
        # tr2 = table1.xpath('//tr[2]')[0]
        # td2 = tr2.xpath('td[2]/text()').extract()
        # td8 = tr2.xpath('td[8]/text()').extract()

        # item['percent'] = td8
        # item['major'] = td2
        # item['code'] = '000002'
        # item['name'] = u'万科'
        # labels = selector.xpath('//div[@class="section"]/div[@class="content"]//td[@class="tips-fieldnameL"]')
        # count = labels[0].xpath('@rowspan').extract()[0]
        # print int(count)
        # for label in labels:
        #     print "hello",label.xpath('@rowspan').extract()
        #     title = label.xpath('text()').extract()
        #     print "hekki",title
        #     # item['percent'] = selector.xpath('//body/div[1]/div[13]/div[2]/table[1]/tbody/tr[2]/td[4]/text()')[0].extract()
        #     # item['major'] = selector.xpath('//body/div[1]/div[13]/div[2]/table[1]/tbody/tr[2]/td[2]/text()')[0].extract()
        #     # item['code'] = '000002'
        #     # item['name'] = u'万科'
        print item
        yield item

