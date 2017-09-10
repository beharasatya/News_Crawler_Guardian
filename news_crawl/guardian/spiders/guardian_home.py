# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from guardian.items import GuardianItem, ErrorItem
import w3lib
from scrapy.http import Request
import scrapy


class GuardianHomeSpider(CrawlSpider):

    name = 'guardian_home'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://theguardian.com/au/']

    extractor1 = LinkExtractor(restrict_xpaths='//*[@class="fc-item__container"]')
    extractor2 = LinkExtractor(restrict_xpaths='//*[@class="top-navigation__action"]')
    extractor3 = LinkExtractor(restrict_xpaths='//*[@class="local-navigation__action"]')

    rules = (
                Rule(extractor1, callback='get_links', follow=True),
                Rule(extractor2, callback='get_links', follow=True),
                Rule(extractor3, callback='get_links', follow=True),
            )

    def parse_start_url(self, response):
        list(self.get_links(response))

    def get_links(self, response):
        print(
            '------------------------------------------------------------------------------------------------------------')
        links = response.xpath("//*[@class='fc-item__container']/a/@href").extract()
        links.extend(response.xpath("//*[@class='fc-item__container']/a/@href").extract())
        links.extend(response.xpath("//*[@class='navigation__action']/a/@href").extract())
        for link in links:
            yield Request(link, callback=self.parse_news)

    def parse_news(self, response):
        print('------------------------------------------------------------------------------------------------------------')
        try:
            body = response.xpath('//div/*[@itemprop="articleBody"]/p').extract()
            body = ' '.join(body)
            body = w3lib.html.remove_tags(body, keep=())

            title = response.xpath("//*[re:match(@class, 'content__headline+')]/text()").extract_first()
            #re:match(@class, 'content__headline+')
            #@class='content__headline'
            if title:
                title = title.strip()

            author = response.xpath("//*[@itemprop='author']/a/span/text()").extract_first()

            date_pub = response.xpath("//*[@itemprop='datePublished']/text()").extract_first()
            if date_pub:
                date_pub = date_pub.strip()

            item = GuardianItem()
            item['author'] = author
            item['title'] = title
            item['article'] = body
            item['date_published'] = date_pub
            item['url'] = response.url
            yield item

        except Exception as e:
            error_item = ErrorItem()
            error_item['url'] = response.url
            error_item['error'] = str(e.args)
            yield error_item