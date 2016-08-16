
SPIDER_MODULES = ['scraper.spiders']

LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {'scraper.pipelines.MongoDBPipeline': 300}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "healthdata"
MONGODB_COLLECTION = "va"
