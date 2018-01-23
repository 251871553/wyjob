# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import  hashlib

class WyjobPipeline(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='10.0.17.165', user='admin', passwd='admin', db='wyjob', port=3306,
                                        charset="utf8")
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def getmd5text(self, text):
        m = hashlib.md5()
        print(text)
        m.update(text)
        return m.hexdigest()

    def process_item(self, item, spider):
        self.cur = self.conn.cursor()
        if item['detail'] == None:
            md5_value = 0
        else:
            md5_value = self.getmd5text(item['detail'].encode('utf-8'))
        check_cmd = "select   url_md5  from  wyjob_python  where  url_md5='%s' " % md5_value
        code = self.cur.execute(check_cmd)
        if code == 0:
            mysql_cmd = "insert into wyjob_python  values (NULL,'%s','%s','%s','%s','%s','%s','%s')" % (md5_value, item['position'].strip(), item['detail'], item['corporation'], item['base'], item['sallary'],item['date'])
            self.cur.execute(mysql_cmd)
        else:
            print('duplicate')
        self.cur.close()
        self.conn.commit()
        return item

    def __del__(self):
        # disconnect  with  db
        self.conn.close()