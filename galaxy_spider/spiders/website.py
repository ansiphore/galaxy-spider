import scrapy


class WebsiteSpider(scrapy.Spider):
    name = 'website'
    allowed_domains = ['ansible.galaxy.com']
    start_urls = ['http://ansible.galaxy.com/']

    def parse(self, response):
        pass
