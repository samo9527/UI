import warnings

from pymysql.connections import Connection
from model.Yaml import MyConfig


class Mysql:
    def __init__(self, switch=False, coding='utf8'):
        """
        初始化数据库数据(用于mysql)
        :param switch: False:不创建表字段，True创建表
        :param coding: 转码
        """
        self.dbHost = MyConfig('address').sql
        self.dbUser = MyConfig('account').sql
        self.dbPsw = MyConfig('password').sql
        self.dbPort = MyConfig('port').sql
        self.dbBase = MyConfig('name_db').sql
        self.dbTable = MyConfig('sql_table').sql
        self.dbTitle = MyConfig('sql_create_title').sql
        self.dbQuery = MyConfig('sql_query').sql
        self.dbInsert = MyConfig('sql_insert').sql
        self.dbDelete = MyConfig('sql_delete').sql
        self.dbUpdate = MyConfig('sql_update').sql
        self.dbCreate = MyConfig('sql_create_list').sql
        self.decoding = coding
        self.DB = self._check_sql_list()
        if switch:
            self._insert_title()

    def _connect_sql(self, switch=False):
        """
        链接数据库
        :param switch: False:单纯链接数据库，True:链接到对应的数据表中
        :return: 数据库值
        """
        if switch:
            db = Connection(
                host=self.dbHost,
                user=self.dbUser,
                password=self.dbPsw,
                database = self.dbBase,
                port=self.dbPort,
                charset=self.decoding)
        else:
            db = Connection(
                host = self.dbHost,
                user = self.dbUser,
                password = self.dbPsw,
                port = self.dbPort,
                charset = self.decoding)
        return db

    def _check_sql_list(self):
        """检查数据库是否存在case_db,先创建它在返回对应数据库值"""
        try:
            warnings.simplefilter("ignore")
            DB = self._connect_sql()
            DB.cursor().execute(self.dbCreate % self.dbBase)
            return self._check_sql_list()
        except Exception:
            DB = self._connect_sql(switch=True)
            return DB

    def _insert_title(self):
        """检查数据库表头，并创建数据库表头"""
        DB = self.DB.cursor()
        DB.execute(self.dbTable)
        DB.execute(self.dbTitle)

    def query_data(self):
        """查询数据库全部的信息"""
        save_data = []
        DB = self.DB.cursor()
        DB.execute(self.dbQuery)
        data = DB.fetchall()
        for a in data:
            save_data.append(list(a))
        return save_data

    def insert_data(self, id, level, module, name, remark, wait_time, status, url, insert_time, img=None,
                    error_reason=None, author=None, *, results_value):
        """插入数据"""
        DB = self.DB.cursor()
        if len(error_reason) < 10000:
            error_reason = error_reason[:10000]
        data = self.dbInsert % (id, level, module, name, url, remark, status, results_value, error_reason, wait_time,
                                img, author, insert_time)
        DB.execute(data)
        self.DB.commit()

    def delete_data(self):
        """清除所有数据"""
        DB = self.DB.cursor()
        DB.execute(self.dbDelete)
        self.DB.commit()

    def close_sql(self):
        """关闭数据库"""
        return self.DB.close()

    def update_sql(self, parameter, case_name):
        """更新数据库部分字段"""
        DB = self.DB.cursor()
        data = self.dbUpdate % (parameter, 'case_name={0!r}'.format(case_name))
        DB.execute(data)
        self.DB.commit()


if __name__ == '__main__':
    data = Mysql().query_data()
    print(data)