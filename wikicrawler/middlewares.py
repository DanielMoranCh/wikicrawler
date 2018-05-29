from scrapy import signals


class WikipediacrawlerSpiderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # Metodo usapo por Scrapy para crear spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # middleware con las spider.
        return None

    def process_spider_output(self, response, result, spider):
        # resultado de la llamada de las Spider

        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        #metodo process_spider_input()

        pass

    def process_start_requests(self, start_requests, spider):
        #inicializa la llamas de las spider, para trabajae  con el metodo process_spider_output()

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WikipediacrawlerDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        #llamada a traves del downloader  middleware.
        # - return None: continua la busqueda
        # - or return un objeto Response
        # - or return un objeto Request
        # - or raise IgnoreRequest: process_exception() metodo instalado de downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        #llamada a traves del downloader  middleware.
        # - return None: continua la busqueda
        # - or return un objeto Response
        # - or return un objeto Request
        # - or raise IgnoreRequest: process_exception() metodo instalado de downloader middleware will be called

        return response

    def process_exception(self, request, exception, spider):
        #llamada a traves del downloader  middleware.
        # - return None: continua la busqueda
        # - or return un objeto Response
        # - or return un objeto Request
        # - or raise IgnoreRequest: process_exception() metodo instalado de downloader middleware will be called
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
