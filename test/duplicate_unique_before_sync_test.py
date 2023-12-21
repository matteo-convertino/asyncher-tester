from client import Client
from data import Data


class DuplicateUniqueBeforeSyncTest:
    def __init__(self):
        self.a = Client()
        self.b = Client()

    def run(self):
        self.a.add_data(Data(name="a", unique="a", is_new=True))
        self.a.add_data(Data(name="b", unique="b", is_new=True))

        print("\n\n-> client A added 2 accounts\n")
        input("Press enter to continue with the next step...\n")

        self.a.sync()

        print("\n\n-> client A synchronized\n")
        input("Press enter to continue with the next step...\n")

        self.b.add_data(Data(name="duplicate unique", unique="a", is_new=True))
        self.b.sync()

        print("\n\n-> client B add duplicate unique & sync\n")
        input("Press enter to continue with the next step...\n")

        self.a.sync()

        print("\n\n-> client A synchronized\n")

        print("Results: \n\n")

        print("---- Client A ----")
        self.a.print()

        print("\n\n---- Client B ----")
        self.b.print()
