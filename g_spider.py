# -*- coding:utf-8 -*-
import scrapy

class Gitspider(scrapy.Spider):
    name = 'github_repositories'

    @property
    def start_urls(self):
        '''
        返回一个可迭代对象
        '''
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        #用css或者xpath处理返回对象的文本信息，获得name和updatetime
        for info in response.css('div#user-repositories-list'):
            yield{
                    
                "name":info.xpath('.//a[contains(@itemprop,"name codeRepository")]/text()').extract(), 


                "update_time":info.css('relative-time::attr(datetime)').extract()
                    
            }

