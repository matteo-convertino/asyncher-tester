import itertools
import json

import requests

from client import Client
from data import Data

import uuid


class CustomTest:
    def __init__(self):
        self.a = Client()
        self.b = Client()
        self.c = Client()
        self.position = 0

    def __random_data(self, n, stop=False):
        data = []

        for i in range(n):
            random_string = uuid.uuid4().hex

            sub_data = [] if stop else self.__random_data(100, True)

            data.append(Data(name=random_string, unique=random_string, sub_data=sub_data, position=self.position, is_new=True))
            self.position += 1

        return data

    def run(self):
        for d in self.__random_data(10000, True):
            self.a.add_data(d)

        self.a.sync()

        print("\n\n-> client A added accounts & sync\n")
        input("Press enter to continue with the next step...\n")

        self.b.sync()

        self.b.data.data[0].name = "EDITED"
        self.b.data.data[0].position = 20
        self.b.data.data[0].updated = True

        self.b.sync()

        print("Results: \n\n")

        print("---- Client A ----")
        self.a.print()

        print("\n\n\n\n", len(self.a.data.data))
        print("\n\n\n\n", len(self.b.data.data))
