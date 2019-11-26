import scrapy
from scrapy import Request

from shein.items import SheinItem

class TiebaSpider(scrapy.Spider):
    name = 'shein'
    allowed_domains = ["https://www.shein.com"]
    start_urls = ["https://www.shein.com/Sweaters-Cardigans-c-2216.html?ici=0_WomenHomePage_Marketing-Block-1-6_Banner_1_50001_HZ-4-3_aod-0&scici=homepage_162~~0_Banner_1_0_hotZone_7td5q3o67~~4_3~~real_2216~~ccc_shein_pc_women-homepage_default~~0~~50001&sort=3",
                  "https://www.shein.com/Sweaters-Cardigans-c-2216.html?ici=0_WomenHomePage_Marketing-Block-1-6_Banner_1_50001_HZ-4-3_aod-0&scici=homepage_162~~0_Banner_1_0_hotZone_7td5q3o67~~4_3~~real_2216~~ccc_shein_pc_women-homepage_default~~0~~50001&sort=3&page=2",
                  "https://www.shein.com/Sweaters-Cardigans-c-2216.html?ici=0_WomenHomePage_Marketing-Block-1-6_Banner_1_50001_HZ-4-3_aod-0&scici=homepage_162~~0_Banner_1_0_hotZone_7td5q3o67~~4_3~~real_2216~~ccc_shein_pc_women-homepage_default~~0~~50001&sort=3&page=3",
                  "https://www.shein.com/Sweaters-Cardigans-c-2216.html?ici=0_WomenHomePage_Marketing-Block-1-6_Banner_1_50001_HZ-4-3_aod-0&scici=homepage_162~~0_Banner_1_0_hotZone_7td5q3o67~~4_3~~real_2216~~ccc_shein_pc_women-homepage_default~~0~~50001&sort=3&page=4",
                  "https://www.shein.com/Sweaters-Cardigans-c-2216.html?ici=0_WomenHomePage_Marketing-Block-1-6_Banner_1_50001_HZ-4-3_aod-0&scici=homepage_162~~0_Banner_1_0_hotZone_7td5q3o67~~4_3~~real_2216~~ccc_shein_pc_women-homepage_default~~0~~50001&sort=3&page=5",
                  ]


    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, headers=self.default_headers, callback=self.parse)

    def parse(self, response):

        div_list = response.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[2] / div / div[4] / div[1]')

        # list_imgs = response.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[1]/a/img[2]/@data-src').extract()
        # if list_imgs:
        #     item = SheinItem()
        #     item['image_urls'] = list_imgs
        #     yield item

        for i in div_list:
            item = SheinItem()

            item['name'] = i.xpath('a/@title').extract()
            item['price'] = i.xpath('a/@data-price').extract()
            # item['image_urls'] = i.xpath('div[1]/a/img[2]/@data-src').extract()
            src = 'http:' + i.xpath('div[1]/a/img[1]/@data-src').extract()[0]
            item['image_urls'] = [src]

            # print('-----------',item['name'])
            # print('-----------',item['price'])
            # print('-----------',item['image_urls'])
            yield item

        # / html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[12] / a
        # / html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[12] / a
        # / html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[11] / a


        # next_page1 = response.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[12] / a').extract()
        # next_page2 = response.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[11] / a').extract()
        # next_page_url1 = response.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[12] / a / @href').extract()
        #
        # if next_page2:
        #     page_url = response.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[11] / a / @href').extract()
        #     next_page_url = 'https://www.shein.com' + page_url
        #     print('aaa', next_page_url)
        #     next_page = response.urljoin(next_page_url)
        #     yield scrapy.Request(next_page, callback=self.parse)
        #
        # if next_page1 and int(next_page_url1[0][-1]) < 6:
        #     page_url = response.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[12] / a / @href').extract()
        #     next_page_url = 'https://www.shein.com' + page_url
        #     print('aaa', next_page_url)
        #     next_page = response.urljoin(next_page_url)
        #     yield scrapy.Request(next_page, callback=self.parse)
