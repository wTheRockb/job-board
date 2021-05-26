import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    region_url_to_name = {}
    start_urls = ['https://geo.craigslist.org/iso/us']
    custom_settings = {
        'DOWNLOAD_TIMEOUT': 10,
    }

    def parse(self, response):
        region_links = response.css('.geo-site-list a')

        for link in region_links:
            region_name = link.css('::text').get()
            region_url = link.css('::attr(href)').get()
            self.region_url_to_name[region_url] = region_name

        for (current_url, current_region_name) in self.region_url_to_name.items():
            print(current_url)
            current_query_url = current_url + "/search/jjj?query=landscaping"
            cb_kwargs = {"region_name": current_region_name}
            yield response.follow(current_query_url, self.parse_job_search, cb_kwargs=cb_kwargs)

    def parse_job_search(self, response, region_name):
        job_page_links = response.css('.result-row a::attr(href)').getall()
        cb_kwargs = {"region_name": region_name}
        yield from response.follow_all(job_page_links, self.parse_job, cb_kwargs=cb_kwargs)

    @staticmethod
    def parse_job(response, region_name):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def extract_body(query):
            return ''.join(response.css(query).getall())

        location_name = response.css('.postingtitle small::text').get()
        if location_name is not None:
            location_name = location_name.replace("(", "").replace(")", "").strip()

        yield {
            'title': extract_with_css('#titletextonly::text'),
            'description': extract_body('#postingbody::text'),
            'lattitude': response.css('#map::attr(data-latitude)').get(),
            'longitude': response.css('#map::attr(data-longitude)').get(),
            'location_name': location_name,
            'region_name': region_name,
            'url': response.url,
        }
