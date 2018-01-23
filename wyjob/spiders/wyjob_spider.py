import scrapy
from wyjob.items import WyjobItem


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'}

class QuotesSpider(scrapy.Spider):
    name = "wyjob"

    def start_requests(self):
        urls = [
            'http://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
       # 'http://search.51job.com/list/020000,000000,0000,00,9,99,python,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,headers=headers)

    def parse(self, response):
        item=WyjobItem()
        for  data  in  response.xpath('//div[@class="el"]'):
             item['position']=data.xpath('./p/span/a/text()').extract_first()
             item['detail'] = data.xpath('./p/span/a/@href').extract_first()
             item['corporation'] = data.xpath('./span[@class="t2"]/a/text()').extract_first()
             item['base']= data.xpath('./span[@class="t3"]/text()').extract_first()
             item['sallary'] = data.xpath('./span[@class="t4"]/text()').extract_first()
             item['date'] = data.xpath('./span[@class="t5"]/text()').extract_first()


             yield item

        #next_page = response.xpath('//div[ @ id = "resultList"] /div[55]/div/div/div/ul/li[8]/a/@href').extract_first()
        next_page = response.xpath('//div[@class="p_in"]/ul/li/a/@href').extract()[-1]
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))
       # if next_page:
       #          url = response.urljoin(next_page[0].extract())
       #          yield scrapy.Request(url, self.parse)
                 #    page = response.url.split("/")[-2]
     #   filename = '51job-%s.html' % page
    #    with open(filename, 'wb') as f:
     #       f.write(response.body)
      #  self.log('Saved file %s' % filename)