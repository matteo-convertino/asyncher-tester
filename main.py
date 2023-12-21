from client import Client
from test.base_delete_two_client_test import BaseDeleteTwoClientTest
from test.base_edit_two_client_test import BaseEditTwoClientTest
from test.base_add_two_client_test import BaseAddTwoClientTest
from test.custom_test import CustomTest
from test.duplicate_unique_before_sync_test import DuplicateUniqueBeforeSyncTest
from test.edit_data_deep_layer_test import EditDataDeepLayerTest
from test.sorting_key_deep_layer_test import SortingKeyDataDeepLayerTest


def test_menu() -> str:
    return """
     0. Exit
     1. ---- Base Two Client ----
        -> client A add 10 accounts
        -> client A sync
        -> client B sync
     2. ---- Base Edit Two Client ----
        -> client A add 2 accounts
        -> client A sync
        -> client B sync
        -> client B edit name of first data & sync
        -> client A sync
     3. ---- Base Edit Two Client ----
        -> client A add 2 accounts
        -> client A sync
        -> client B sync
        -> client B deleted first data & sync
        -> client A sync
     4. ---- Duplicate Unique Before Sync ----
        -> client A add 2 accounts
        -> client A sync
        -> client B add duplicate unique & sync
        -> client A sync
     5. ---- Edit Data Deep Layer ----
        -> client A add 2 accounts
        -> client A sync
        -> client B sync
        -> client B edit name of first sub data & sync
        -> client A sync
     6. ---- Data Deep Layer With Sorting Key ----
        -> client A add 2 accounts
        -> client A sync
        -> client B sync
        -> client B edit position of a sub data and delete another sub data (to scale position) & sync
        -> client A sync
     99. ---- Custom Test ----
    """


if __name__ == "__main__":
    client = Client()

    while True:
        print(test_menu())

        ans = input("Select the test you want to run: ")

        if ans == "1":
            BaseAddTwoClientTest().run()
        elif ans == "2":
            BaseEditTwoClientTest().run()
        elif ans == "3":
            BaseDeleteTwoClientTest().run()
        elif ans == "4":
            DuplicateUniqueBeforeSyncTest().run()
        elif ans == "5":
            EditDataDeepLayerTest().run()
        elif ans == "6":
            SortingKeyDataDeepLayerTest().run()
        elif ans == "99":
            CustomTest().run()
        elif ans == "0":
            print("\nGoodbye")
            break
        else:
            print("\nNot Valid Choice. Try again.")
