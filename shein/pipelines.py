# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

from shein.items import SheinItem
images_store = get_project_settings().get('IMAGES_STORE')

class SheinPipeline(object):
    def process_item(self, item, spider):
        return item


class SheinImgDownloadPipeline(ImagesPipeline):

    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    def get_media_requests(self, item, info):

        # 获取图片地址，发起请求
        # img_url = 'http:' + item['image_url']
        # print('获取图片地址', img_url)
        # yield scrapy.Request(img_url)

        for image_url in item['image_urls']:
            # img_url = 'http:' + image_url
            print('img_url', image_url)
            # img_url = "http:"+image_url
            img_url = image_url
            self.default_headers['referer'] = img_url
            yield scrapy.Request(img_url, headers=self.default_headers, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no image")
        else:
            # print('AAAAAAAAAA',results[0][1]['path'])
            # print('AAAAAAAAAA',item['name'])
            #  图片重命名
            os.rename(images_store + '/' + results[0][1]['path'], images_store + '/' + item['name'][0] + '-' + item['price'][0] + '.jpg')
            item['image_paths'] = image_paths
        return item
