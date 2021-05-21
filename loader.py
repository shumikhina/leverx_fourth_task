import abc
import json


class BaseLoader:

    @abc.abstractmethod
    def load_data(self, *args, **kwargs):
        pass


class JSONLoader(BaseLoader):

    def __init__(self, path: str):
        self.path = path

    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
