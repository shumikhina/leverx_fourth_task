import pymysql
import constants
#connection = create_connection("127.0.0.1", "root", "1553")


class Database:
    def __init__(self, host, port, user, password):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
        )
        self.cursor = self.connection.cursor()


def create_table_rooms():
    return constants.create_table_rooms


def create_table_students():
    return constants.create_table_students




  



