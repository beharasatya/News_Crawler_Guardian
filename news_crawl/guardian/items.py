# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class GuardianItem(Item):

    title = Field()
    author = Field()
    date_published = Field()
    article = Field()
    url = Field()


class ErrorItem(Item):

    error = Field()
    url = Field()
