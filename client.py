import json

import requests
from data import Data, DataList


class Client:
    def __init__(self):
        self.data = DataList()
        self.url = 'http://localhost:8080'

    def add_data(self, value: Data):
        self.data.data.append(value)

    def get_data_by_unique(self, value: str):
        for data in self.data.data:
            if data.unique == value:
                return data
        return None

    def sync(self):
        x = requests.post(f'{self.url}/sync/', json=json.dumps(self.data.model_dump(exclude_none=True)["data"]))
        self.data = DataList(data=x.json())

    def print(self):
        self.data.data.sort(key=lambda x: x.unique)
        print(self.data.model_dump_json(indent=2, exclude_none=True))

