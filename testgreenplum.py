#_*_ coding:utf-8 _*_
#!/usr/bin/env python

import pg


def operate_postgre_tbl_product():
    try:
        #pgdb_conn = pg.connect(dbname = 'tpc', host = '192.168.103.31', user = 'gpadmin', passwd = '')
        pgdb_conn = pg.connect("host=192.168.103.31 port=5432 dbname=tpc user=gpadmin")

    except Exception as e:
         print(e.args[0])
         return


    sql_desc = "select * from call_center limit 5;"
    for row in pgdb_conn.query(sql_desc).dictresult():
        print(row)

    pgdb_conn.close()


if __name__ == '__main__':
    operate_postgre_tbl_product()