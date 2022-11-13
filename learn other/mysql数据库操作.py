"""
1、连接数据库
2、执行sql语句
3、获取执行的结果
4、关闭数据库连接
"""

import pymysql


# 1、建立连接
conn = pymysql.connect(
    host="api.lemonban.com",
    port=3306,
    user="future",
    password="123456",
    database="futureloan",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor  # 返回字典
)

# 2、创建游标
cur = conn.cursor()

# 3、执行sql语句
sql = 'select * from member LIMIT 10'
count = cur.execute(sql)  # 返回的是，sql语句执行结果的行数

# 4、获取sql语句执行后的数据结果
one = cur.fetchone()  # 获取结果中的第一条
print("第一条数据：", one)

# 5、获取所有的结果
All_Result = cur.fetchall()  # 获取所有的数据
print("所有数据：", All_Result)
# 6、关闭游标，关闭数据库链接
cur.close()
conn.close()

