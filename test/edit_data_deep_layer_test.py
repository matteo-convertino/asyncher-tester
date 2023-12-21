from client import Client
from data import Data


class EditDataDeepLayerTest:
    def __init__(self):
        self.a = Client()
        self.b = Client()

    def run(self):
        self.a.add_data(
            Data(
                name="b",
                unique="b",
                is_new=True,
                sub_data=[
                    Data(name="b_a", unique="b_a", is_new=True, sub_data=[
                        Data(name="b_a_a", unique="b_a_a", is_new=True)
                    ]),
                ]
            )
        )

        print("\n\n-> client A added 1 account with two deep layer\n")
        input("Press enter to continue with the next step...\n")

        self.a.sync()

        print("\n\n-> client A synchronized\n")
        input("Press enter to continue with the next step...\n")

        self.b.sync()
        self.b.data.data[0].sub_data[0].sub_data[0].sub_data = [Data(name="b_a_a_a", unique="b_a_a_a", is_new=True)]

        self.b.sync()

        print("\n\n-> client B add another deep layer & synchronized\n")
        input("Press enter to continue with the next step...\n")

        self.a.sync()
        self.a.data.data[0].sub_data[0].sub_data[0].sub_data[0].name = "NAME EDITED"
        self.a.data.data[0].sub_data[0].sub_data[0].sub_data[0].updated = True

        self.a.sync()
        self.b.sync()

        print("\n\n-> client A synchronized & edit last one deep layer\n")

        print("Results: \n\n")

        print("---- Client A ----")
        self.a.print()

        print("\n\n---- Client B ----")
        self.b.print()
