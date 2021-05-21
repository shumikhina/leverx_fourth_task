from loader import BaseLoader
from joiner import Joiner
from printer import BasePrinter


class Controller:

    joiner_class = Joiner

    @classmethod
    def process_files(cls, rooms_loader: BaseLoader, students_loader: BaseLoader, printer: BasePrinter):
        rooms_data = rooms_loader.load_data()
        students_data = students_loader.load_data()
        result_data = cls.joiner_class.join_rooms_with_students(rooms_data, students_data)
        printer.print(result_data)