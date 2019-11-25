import scrapy
from shein.items import SheinItem

class TiebaSpider(scrapy.Spider):
    name = 'shein'
    allowed_domains = ["https://www.shein.com"]
    start_urls = ["https://www.shein.com/Sweaters-Cardigans-c-2216.html?ici=0_WomenHomePage_Marketing-Block-1-6_Banner_1_50001_HZ-4-3_aod-0&scici=homepage_162~~0_Banner_1_0_hotZone_7td5q3o67~~4_3~~real_2216~~ccc_shein_pc_women-homepage_default~~0~~50001&sort=3", ]

    def parse(self, response):
        item = SheinItem()
        # / html / body / div[1] / div[1] / div / div[1] / div[2] / div[1] / div[4] / div[1] / a
        # / html / body / div[1] / div[1] / div / div[1] / div[2] / div[2] / div[4] / div[1] / a
        item['name'] = response.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[2] / div / div[4] / div[1] / a / @title').extract()

        print(item['name'])
        yield item