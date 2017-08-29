import scrapy

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_url=[
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
    ]

    def parse_dir_contents(self, response):
        print(response)
        filename = response.url.split('/')[-2] + 'html'
        print(type(filename))
        with open(filename, 'wb') as f:
            f.write(filename.body)