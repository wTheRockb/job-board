import scrapy


class CraigslistRegionSpider(scrapy.Spider):
    name = 'craigslist_region'

    start_urls = ['https://geo.craigslist.org/iso/us']

    def parse(self, response):
        region_links = response.css('.geo-site-list a')
        results = {}
        for link in region_links:
            region_name = link.css('::text').get()
            region_url = link.css('::attr(href)').get()
            results[region_url] = region_name
        return results
