# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import mysql.connector
import psycopg2
import pymongo

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class SqlscraperPipeline:
    def process_item(self, item, spider):
        return item

class PriceToUSDPipeline:

    gbpToUsdRate = 1.3

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ## check is price present
        if adapter.get('price'):

            #converting the price to a float
            floatPrice = float(adapter['price'])

            #converting the price from gbp to usd using our hard coded exchange rate
            adapter['price'] = floatPrice * self.gbpToUsdRate

            return item

        else:
            # drop item if no price
            raise DropItem(f"Missing price in {item}")
        

class DuplicatesPipeline:
    def __init__(self):
        self.names_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['name'] in self.names_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.names_seen.add(adapter['name'])
            return item
        


class SQLPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'eric',
            password = 'eric',
            database = 'datamining'
        )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_in_db(item)
        #we need to return the item below as Scrapy expects us to!
        return item

    def store_in_db(self, item):
        self.curr.execute(""" insert into table_name(name,price,url) values (%s,%s,%s)""", (
            item["name"],
            item["price"],
            item["url"]
        ))
        self.conn.commit()

class PostgresPipeline(object):

    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.conn = psycopg2.connect(
            host = 'localhost',
            user = 'eric',
            password = 'eric',
            database = 'datamining'
        )

        self.curr = self.conn.cursor()


    def process_item(self, item, spider):
        self.store_in_db(item)
        #we need to return the item below as scrapy expects us to!
        return item

    def store_in_db(self, item):
        self.curr.execute(""" insert into table_name(name,price,url) values (%s,%s,%s)""", (
            item["name"],
            item["price"],
            item["url"]
        ))
        self.conn.commit()



class MongoDBPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGODB_URI"),
            mongo_db=crawler.settings.get("MONGODB_DATABASE")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(dict(item))
        return item