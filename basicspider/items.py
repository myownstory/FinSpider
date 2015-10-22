# -*- coding: utf-8 -*-

import scrapy
from scrapy import Field, Item


class F10Item(Item):
    code = Field()
    name = Field()
    majorname = Field()
    majorvol = Field()
    majorpcnt = Field()
    majormao = Field()
