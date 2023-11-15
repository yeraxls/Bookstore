import pathlib
import json
class ManageDb:
    __address_file = "{0}/src/db/dbBooks.json".format(pathlib.Path().absolute())

    def read_books(self):
        with open(self.__address_file, "r") as data:
            return json.loads(data.read())