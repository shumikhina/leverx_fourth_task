from loader import BaseLoader
from printer import BasePrinter
from db_worker import StudentsRoomsDBWorker


class Controller:

    @classmethod
    def process_files(cls, rooms_loader: BaseLoader, students_loader: BaseLoader,
                      db: StudentsRoomsDBWorker, printer: BasePrinter):
        rooms_data = rooms_loader.load_data()
        students_data = students_loader.load_data()
        db.create_tables()
        db.fill_tables_data(rooms_data, students_data)
        rooms_with_students = db.rooms_with_students()
        top_rooms_min = db.top_rooms_min()
        top_rooms_max_diff = db.top_rooms_max_diff()
        rooms_with_different_sex = db.rooms_with_different_sex()
        printer.print(rooms_with_students, 'first_query')
        printer.print(top_rooms_min, 'second_query')
        printer.print(top_rooms_max_diff, 'third_query')
        printer.print(rooms_with_different_sex, 'fourth_query')
