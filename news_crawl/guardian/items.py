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
    # define the fields for your item here like:
    # name = scrapy.Field()

    error = Field()
    url = Field()

'''n.find({"article" : {'$regex' : ".*Turnbull.*"}})

n.ensure_index([('article', 'text')])

n.find({"$text": {"$search": 'Turnbull'}}).count()

n.find({"$text": {"$search": "\Drew Morphett\Foxtel"}}, { "score": { "$meta": "textScore" } }).sort( [( "score", { "$meta": "textScore" } ) ])

'''