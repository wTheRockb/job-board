import json
import scrapy

craigslist_regions = {}
with open('craigslist_region.json') as f:
        craigslist_regions = json.load(f)
        craigslist_regions = craigslist_regions[0]

def map_job_url_to_region(location_dict, job_url):
    shortened_url = job_url.split(".org/")[0] + ".org"
    return location_dict[shortened_url]

def get_start_urls():
    craigslist_regions = []
    with open('craigslist_region.json') as f:
        craigslist_regions = json.load(f)
        craigslist_regions = craigslist_regions[0].keys()
    return list(map(lambda x: x + "/search/jjj?query=landscaping", craigslist_regions))


class JobsSpider(scrapy.Spider):
    name = 'jobs'

    start_urls = get_start_urls()
    

    def parse(self, response):
        job_page_links = response.css('.result-row a::attr(href)').getall()
        yield from response.follow_all(job_page_links, self.parse_job)

    def parse_job(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def extract_body(query):
            return ''.join(response.css(query).getall())

        location_name = response.css('.postingtitle small::text').get()
        if location_name != None:
            location_name = location_name.replace("(", "").replace(")", "").strip()

        ## TODO get any pictures also?
        yield {
            'title': extract_with_css('#titletextonly::text'),
            'description': extract_body('#postingbody::text'),
            'lattitude': response.css('#map::attr(data-latitude)').get(),
            'longitude': response.css('#map::attr(data-longitude)').get(),
            'location_name': location_name,
            'region_name': map_job_url_to_region(craigslist_regions, response.url),
            'url': response.url,
        }




