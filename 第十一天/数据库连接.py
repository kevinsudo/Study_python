import pymysql
db=pymysql.connect("localhost","root","123123","mysql")
#执行sql语句
cursor=db.cursor()
sql="select * from "
