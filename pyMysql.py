# coding=utf-8

import datetime

import pymysql as MySQLdb

host = '127.0.0.1'
user = 'root'
passwd = 'root'
port = 3306
db = 'baiwan'


class OperationMySQL(object):
    def __init__(self):
        """连接数据库"""
        try:
            self.conn = MySQLdb.connect(host=host,
                                        port=port,
                                        user=user,
                                        passwd=passwd,
                                        db=db,
                                        charset='utf8', )
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Connect MySQL Database Fail: ' + e)

    def _close_connect(self):
        """关闭连接"""
        self.cur.close()
        self.conn.close()

    def insert_data(self, data):
        """插入数据"""
        sql = 'insert into blog_rank (rank,score,create_time) values ({0},{1},{2})'.format(data['rank'], data['score'],
                                                                                           datetime.datetime.now().timestamp())
        res = self.cur.execute(sql)
        self.conn.commit()
        self._close_connect()

    def select_data(self, sql=None):
        """根据sql查询数据"""
        if sql is None:
            sql = 'SELECT name,id FROM auth_permission'
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self._close_connect()
        headers = ('name', 'id')
        results = [dict(zip(headers, row)) for row in result]
        print(results)
        return results


if __name__ == '__main__':
    OperationMySQL().select_data()

