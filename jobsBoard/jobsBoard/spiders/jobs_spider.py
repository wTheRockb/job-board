import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'

    start_urls = ['https://orangecounty.craigslist.org/search/jjj?query=landscaping']

    def parse(self, response):
        job_page_links = response.css('.result-row a::attr(href)').getall()
        yield from response.follow_all(job_page_links, self.parse_job)

        # pagination_links = response.css('li.next a')
        # yield from response.follow_all(pagination_links, self.parse)

    def parse_job(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def extract_body(query):
            return ''.join(response.css(query).getall())

        yield {
            'title': extract_with_css('#titletextonly::text'),
            'description': extract_body('#postingbody::text'),
            'location': response.url
        }