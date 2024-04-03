import scrapy


class GlassesSpider(scrapy.Spider):
    name = "glasses"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        products = response.xpath("//div[@class='p-title-block']/div[2]/div")
        for product in products:
            name = product.xpath("normalize-space(.//div[1]/div/a[1]/text())").get()
            price = product.xpath(".//div[2]/div/div/span/text()").get()
            link = product.xpath(".//div[1]/div/a[1]/@href").get()

            yield scrapy.Request(url=link, callback=self.parse_glasses, meta={'glass_name':name,'glass_price':price,'glass_link':link})  

    def parse_glasses(self, response):
        name = response.request.meta['glass_name']
        price = response.request.meta['glass_price']
        link = response.request.meta['glass_link']
        photos_link = response.xpath("//div[@class='head-content']/div[2]/div/div/div/div/div/img/@src").getall()

        yield{
            'glass_name':name.strip('\n'),
            'glass_price':price,
            'glass_link':link,
            'photos_link':str(photos_link)
        }

        #next_page = response.xpath("//ul[@class='pagination']/li[6]/a[@class='page-link']/@href").get()
        next_page = response.xpath("//ul[@class='pagination']/li[@class='page-item']/a[@class='page-link'][contains(text(), 'Next')]/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_glasses)           
