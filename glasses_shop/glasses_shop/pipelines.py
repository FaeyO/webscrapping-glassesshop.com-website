# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class SQLlitePipeline(object):

    def open_spider(self,spider):
        self.connection = sqlite3.connect("glasses_shop.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''CREATE TABLE glasses (glass_name TEXT,
                            glass_price TEXT, glass_link TEXT, photo_link TEXT )''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self,spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''INSERT INTO glasses (glass_name, glass_price, glass_link, photo_link) VALUES(?,?,?,?) ''',
                       (item.get('glass_name'),
                       item.get('glass_price'),
                       item.get('glass_link'),
                       item.get('photo_link')))
        self.connection.commit()
        return item
