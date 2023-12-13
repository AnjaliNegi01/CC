import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def getConnection():
        try:
            connection_string=DBPropertyUtil.getConnectionString()
            conn=mysql.connector.connect(**connection_string)
            return conn
        except mysql.connector.Error as e:
            print(f"Errot connection to mysql: {e}")
            return None