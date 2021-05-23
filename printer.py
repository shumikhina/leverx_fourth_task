import abc
import json
import xml.etree.cElementTree as xml


class BasePrinter:

    @abc.abstractmethod
    def print(self, data, filename) -> None:
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
    def print_to_json(data, filename='file'):
        with open(f'{filename}.json', 'w') as file:
            json.dump(data, file)

    @staticmethod
    def print_to_xml(data, filename='file'):
        dimension = list(data[0].keys())[2]
        root = xml.Element('Rooms')
        for room in data:
            room_element = xml.SubElement(root, 'Room')
            xml.SubElement(room_element, 'Id').text = str(room['room_id'])
            xml.SubElement(room_element, 'Name').text = str(room['room_name'])
            xml.SubElement(room_element, dimension.capitalize()).text = str(room[dimension])
        file_xml = xml.ElementTree(root)
        file_xml.write(f'{filename}.xml')

    def print(self, data, filename) -> None:
        self._get_output_method()(data, filename=filename)
