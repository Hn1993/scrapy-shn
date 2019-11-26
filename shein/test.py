import requests
from lxml import html, etree

base_urls = 'https://www.shein.com/Sweaters-Cardigans-c-2216.html?ici=0_WomenHomePage_Marketing-Block-1-6_Banner_1_50001_HZ-4-3_aod-0&scici=homepage_162~~0_Banner_1_0_hotZone_7td5q3o67~~4_3~~real_2216~~ccc_shein_pc_women-homepage_default~~0~~50001&sort=3&page=2'
response = requests.get(base_urls)
# print(response.text)

s = etree.HTML(response.text)
# next_page = s.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[2] / div / div[4] / div[1] / a / @title')
image_url = s.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[1]/a/img[2]/@data-src')
next_page = s.xpath('/html/body/div[1]/div[1]/div/div[1]/div[3]/ul/li/a/text()')

next_page = s.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[12] / a')
next_page_url = s.xpath('/ html / body / div[1] / div[1] / div / div[1] / div[3] / ul / li[12] / a / @href')
print(next_page)
print(next_page_url)
print(next_page_url[0][-1])

# if next_page:

    # next_page = s.urljoin(next_page_url)



# /html/body/div[1]/div[1]/div/div[1]/div[3]/ul/li[11]/a
# /html/body/div[1]/div[1]/div/div[1]/div[3]/ul/li[12]/a

# /html/body/div[1]/div[1]/div/div[1]/div[2]/div[4]/div[4]/div[1]/div[1]/a/img[2]
#
# /html/body/div[1]/div[1]/div/div[1]/div[2]/div[7]/div[4]/div[1]/div[1]/a/img[2]
# print(image_url)
# print(next_page)
# print(len(image_url))