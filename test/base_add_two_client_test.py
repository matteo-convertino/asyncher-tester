from client import Client
from data import Data


class BaseAddTwoClientTest:
    def __init__(self):
        self.a = Client()
        self.b = Client()

    def run(self):
        self.a.add_data(Data(name="a", unique="a", is_new=True))
        self.a.add_data(Data(name="b", unique="b", is_new=True))
        self.a.add_data(Data(name="c", unique="c", is_new=True))
        self.a.add_data(Data(name="d", unique="d", is_new=True))
        self.a.add_data(Data(name="e", unique="e", is_new=True))
        self.a.add_data(Data(name="f", unique="f", is_new=True))
        self.a.add_data(Data(name="g", unique="g", is_new=True))
        self.a.add_data(Data(name="h", unique="h", is_new=True))
        self.a.add_data(Data(name="i", unique="i", is_new=True))

        print("\n\n-> client A added 10 accounts\n")
        input("Press enter to continue with the next step...\n")

        self.a.sync()

        print("\n\n-> client A synchronized\n")
        input("Press enter to continue with the next step...\n")

        self.b.sync()

        print("\n\n-> client B synchronized\n")

        print("Results: \n\n")

        print("---- Client A ----")
        self.a.print()

        print("\n\n---- Client B ----")
        self.b.print()
