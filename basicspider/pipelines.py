# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.out', 'wb')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        if item['code'].startswith('60'):
            line = '1|'+item['code']+'|'\
                   +item['majorname'] +','+item['majorvol']+','+item['majorpcnt']+','+item['majormao']+'|0.000\n'
        else:
            line = '0|'+item['code']+'|'\
                   +item['majorname'] +','+item['majorvol']+','+item['majorpcnt']+','+item['majormao']+'|0.000\n'
        self.file.write(line)
        return item

class BasicPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(host='127.0.0.1', port=27017)
        db = connection.DoubanMovie
        self.collect = db.MovieTop250

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing %s of blogpost from %s" % (data, item['url']))
        if valid:
            new_moive = [{
                "title": item['title'],
                "star": item['star'],
                "quote": item['quote'],
                "movieInfo": item['movieInfo'].strip()
            }]
            self.collect.insert(new_moive)
        return item
