import scrapy


class CraigslistLocationSpider(scrapy.Spider):
    name = 'craigslist_location'

    start_urls = ['https://geo.craigslist.org/iso/us']


    def parse(self, response):
        location_links = response.css('.geo-site-list a')
        for link in location_links:
            location_name = link.css('::text').get()
            location_url = link.css('::attr(href)').get()
            result = {
                'location_name': location_name,
                'location_url': location_url,
            }
            print(result)
            yield result

