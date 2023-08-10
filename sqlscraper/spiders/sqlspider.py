import scrapy
from sqlscraper.items import SqlscraperItem
from sqlscraper.itemloaders import SqlItemLoader
class SqlspiderSpider(scrapy.Spider):
    name = "sqlspider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    def parse(self, response):
        products = response.css('product-item')
        for product in products:
            sql_item = SqlItemLoader(item=SqlscraperItem(), selector=product)
            sql_item.add_css('name', "a.product-item-meta__title::text")
            sql_item.add_css('price', 'span.price', re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            sql_item.add_css('url', 'div.product-item-meta a::attr(href)')
            yield sql_item.load_item() 
        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)
