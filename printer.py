import abc
import json
import xml.etree.cElementTree as xml


class BasePrinter:

    @abc.abstractmethod
    def print(self, data) -> None:
        pass


class JSONOrXMLPrinter(BasePrinter):

    def __init__(self, output_format):
        self.output_format = output_format

    def _get_output_method(self):
        methods_map = {
            '1': self.print_to_json,
            '2': self.print_to_xml
        }
        return methods_map[self.output_format]

    @staticmethod
    def print_to_json(data):
        with open('file.json', 'w') as file:
            json.dump(data, file)

    @staticmethod
    def print_to_xml(data):
        # root = xml.Element('Rooms')
        # for room in data.values():
        #     room_element = xml.SubElement(root, 'Room')
        #     xml.SubElement(room_element, 'Id').text = str(room['id'])
        #     xml.SubElement(room_element, 'Name').text = str(room['name'])
        #     students = xml.SubElement(room_element, 'Students')
        #     for student in room['students']:
        #         student_element = xml.SubElement(students, 'Student')
        #         xml.SubElement(student_element, 'Id').text = str(student['id'])
        #         xml.SubElement(student_element, 'Name').text = student['name']
        #         xml.SubElement(student_element, 'Room').text = str(student['room'])
        # file_xml = xml.ElementTree(root)
        file_xml.write('file.xml')

    def print(self, data) -> None:
        self._get_output_method()(data)
