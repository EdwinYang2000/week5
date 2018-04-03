# -*- coding:utf-8 -*-

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import MovieItem

class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):
    name = 'awesome-movie'

    download_delay = 2
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']
    rules = (Rule(LinkExtractor(restrict_xpaths='//div[@class="recommendations-bd"]/dl/dd/a'),
            callback='prase_page',follow=True),)

    def prase_movie_item(self, response):
        item = MovieItem()
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
        item['url'] = response.url
        item['score'] = response.xpath('//strong[@property="v:average"]/text()').extract()
        item['summary'] = ''.join(response.xpath('//span[@property="v:summary"]/text()').extract())
        return item

    def prase_start_url(self,response):
        yield self.parse_movie_item(response)


    def prase_page(self,response):
        yield self.prase_movie_item(response)


