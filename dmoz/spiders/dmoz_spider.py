import scrapy

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    #可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。

    start_url=[
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
    ]
    '''
    先爬起始网站的站内链接，再爬这些链接内的数据
    '''
    def parse(self, response):
        '''parse寻找符合要求的链接，urljoin返回绝对路径，用scrapy.Request再将每个内链传给下面提取数据的方法parse_dir_contents'''

        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url=response.urljoin(response.url,href.extract())
            yield scrapy.Request(url,callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

    '''
    提取站内数据，再查找能跟进的页面，并使用同一回调函数,【【【常用来爬取分页网站】】】
    '''
    def parse_articles_follow_next_page(self,response):
        for article in response.xpath('//article')
            item = ArticleItem()
            ……
            yield item

        next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_articles_follow_next_page)
