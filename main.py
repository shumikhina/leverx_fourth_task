import constants
from controller import Controller
import argparse

from loader import JSONLoader
from printer import JSONOrXMLPrinter


def get_parser():
    parser = argparse.ArgumentParser(description=constants.PARSER_DESCRIPTION)
    parser.add_argument('room_path', type=str, help=constants.ROOMS_PATH_HELP_MESSAGE)
    parser.add_argument('students_path', type=str, help=constants.STUDENTS_PATH_HELP_MESSAGE)
    parser.add_argument('output_format', choices=['1', '2'], default='1', help=constants.OUTPUT_FORMAT_HELP_MESSAGE)
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()

    rooms_loader = JSONLoader(args.room_path)
    students_loader = JSONLoader(args.students_path)
    printer = JSONOrXMLPrinter(args.output_format)
    Controller().process_files(rooms_loader, students_loader, printer)
