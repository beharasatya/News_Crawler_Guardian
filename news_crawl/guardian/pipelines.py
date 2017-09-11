# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from guardian.items import GuardianItem
from scrapy import log


class GuardianMongoPipeline(object):

    def __init__(self):
        self.connection = pymongo.MongoClient(
            settings['COMPOSE_URI']
        )
        self.db = self.connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]
        self.err_collection = self.db[settings['MONGODB_ERRORS']]
        self.stat_collection = self.db[settings['MONGODB_STATS']]

        # Clear the news articles and the errors from the previous run
        self.collection.remove()
        self.err_collection.remove()

    def close_spider(self, spider):
        stats = spider.crawler.stats.get_stats()  # stats is a dictionary
        # write stats to the database here
        self.stat_collection.insert(stats)
        self.connection.close()

    def process_item(self, item, spider):
        if isinstance(item, GuardianItem):
            self.collection.insert(dict(item))
            log.msg("News added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        else:
            self.err_collection.insert(dict(item))
        return item
