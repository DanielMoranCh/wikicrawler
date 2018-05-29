# configuraciones de Scrapy para el proyecto wikicrawler

#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wikicrawler'

SPIDER_MODULES = ['wikicrawler.spiders']
NEWSPIDER_MODULE = 'wikicrawler.spiders'


ROBOTSTXT_OBEY = True
