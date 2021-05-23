import pymysql
from pymysql.constants import CLIENT

import constants


class BaseDBWorker:

    def __init__(self, host, port, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            client_flag=CLIENT.MULTI_STATEMENTS
        )

    def _execute_query(self, query, data=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, args=data)
            self.connection.commit()
            return cursor.fetchall()

    def _executemany_query(self, query, data):
        with self.connection.cursor() as cursor:
            cursor.executemany(query, data)
            self.connection.commit()
            return cursor.fetchall()

    @staticmethod
    def _process_result_to_dict(data, output_format):
        return list({name: value for name, value in zip(output_format, d)} for d in data)


class StudentsRoomsDBWorker(BaseDBWorker):

    def create_tables(self):
        self._execute_query(constants.DROP_TABLES)
        for query in constants.CREATE_TABLES_QUERIES:
            self._execute_query(query)

    def fill_tables_data(self, rooms_data, students_data):
        self._executemany_query(constants.INSERT_ROOMS, (tuple(item.values()) for item in rooms_data))
        self._executemany_query(constants.INSERT_STUDENTS, (tuple(item.values()) for item in students_data))

    def rooms_with_students(self):
        data = self._execute_query(constants.ROOMS_WITH_STUDENTS)
        return self._process_result_to_dict(data, ('room_id', 'room_name', 'students_count'))

    def top_rooms_min(self):
        data = self._execute_query(constants.TOP_ROOMS_MIN)
        return self._process_result_to_dict(data, ('room_id', 'room_name', 'min_avg_student_age'))

    def top_rooms_max_diff(self):
        data = self._execute_query(constants.TOP_ROOMS_MAX_DIFF)
        return self._process_result_to_dict(data, ('room_id', 'room_name', 'max_age_diff'))

    def rooms_with_different_sex(self):
        data = self._execute_query(constants.ROOMS_WITH_DIFFERENT_SEX)
        return self._process_result_to_dict(data, ('room_id', 'room_name', 'has_diff_sex'))
