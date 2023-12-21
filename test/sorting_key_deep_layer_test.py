from client import Client
from data import Data


class SortingKeyDataDeepLayerTest:
    def __init__(self):
        self.a = Client()
        self.b = Client()

    def run(self):
        self.a.add_data(
            Data(
                name="a",
                unique="a",
                is_new=True,
                sub_data=[
                    Data(
                        name="a_a",
                        unique="a_a",
                        is_new=True,
                        position=0,
                        sub_data=[
                            Data(name="a_a_a", unique="a_a_a", is_new=True),
                            Data(name="a_a_b", unique="a_a_b", is_new=True)
                        ]
                    ),
                    Data(
                        name="a_b",
                        unique="a_b",
                        is_new=True,
                        position=1,
                        sub_data=[
                            Data(name="a_b_a", unique="a_b_a", is_new=True),
                            Data(name="a_b_b", unique="a_b_b", is_new=True)
                        ]
                    ),
                ]
            )
        )

        self.a.add_data(
            Data(
                name="b",
                unique="b",
                is_new=True,
                sub_data=[
                    Data(
                        name="b_a",
                        unique="b_a",
                        position=2,
                        is_new=True,
                        sub_data=[
                            Data(name="b_a_a", unique="b_a_a", is_new=True),
                            Data(name="b_a_b", unique="b_a_b", is_new=True),
                            Data(name="b_a_c", unique="b_a_c", is_new=True)
                        ]
                    ),
                    Data(
                        name="b_b",
                        unique="b_b",
                        is_new=True,
                        position=3,
                        sub_data=[
                            Data(name="b_b_a", unique="b_b_a", is_new=True),
                            Data(name="b_b_b", unique="b_b_b", is_new=True),
                            Data(name="b_b_c", unique="b_b_c", is_new=True)
                        ]
                    ),
                ]
            )
        )

        print("\n\n-> client A added accounts with deep layers and position\n")
        input("Press enter to continue with the next step...\n")

        self.a.sync()

        print("\n\n-> client A synchronized\n")
        input("Press enter to continue with the next step...\n")

        self.b.sync()
        self.b.data.data[1].sub_data[1].position = 0
        self.b.data.data[1].sub_data[0].position = 1
        self.b.data.data[1].sub_data[0].updated = True
        self.b.data.data[1].sub_data[1].updated = True
        self.b.data.data[0].sub_data[0].deleted = True
        self.b.sync()

        print("\n\n-> client B deleted one & synchronized\n")
        input("Press enter to continue with the next step...\n")

        self.a.sync()

        print("\n\n-> client A synchronized\n")

        print("Results: \n\n")

        print("---- Client A ----")
        self.a.print()

        print("\n\n---- Client B ----")
        self.b.print()
