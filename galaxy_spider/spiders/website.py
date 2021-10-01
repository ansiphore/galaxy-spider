import scrapy
import sqlite3


class WebsiteSpider(scrapy.Spider):
    name = 'website'
    allowed_domains = ['galaxy.ansible.com']

    field_labels = {}

    field_types = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        conn = sqlite3.connect('result.db', isolation_level=None)
        c = conn.cursor()

        self.conn = conn

    def start_requests(self):
        for i in range(300):
            yield scrapy.Request(
                'https://galaxy.ansible.com/search?deprecated=false&keywords=&order_by=-relevance&page_size=100&page=' +
                str(i + 1), self.parse)

    def parse(self, response):
        if len(response.body) == 0:
            return

        role_links = response.css('.collection-item > .collection-container a')

        for link in role_links:
            yield response.follow(link, self.parse_role)

    def parse_role(self, response):
        pass
