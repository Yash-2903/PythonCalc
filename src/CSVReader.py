import csv
from pprint import pprint


# def ClassFactory(class_name, dictionary):
# return type(class_name, (object,), dictionary)

# Read csv file and convert data into list format
class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

# def return_data_as_objects(self, class_name):
# objects = []
# pprint(self.data)
# for row in self.data:
# objects.append(ClassFactory(class_name, row))
# return objects
