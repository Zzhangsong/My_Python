"""
1、数据库链接  conn cur
2、获取一条数据
3、获取条数
4、获取所有数据
5、关闭数据库链接
"""
import pymysql
from day4.Common.handle_config import conf


class HandleDB:

    def __init__(self):
        self.conn = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        # 创建游标
        self.cur = self.conn.cursor()

    def get_one_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_count(self, sql):
        return self.cur.execute(sql)

    def updata(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def get_close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    sql = 'select * from member LIMIT 3'
    db = HandleDB()
    data = db.get_one_data(sql)
    print("一条数据", data)

