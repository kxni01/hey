import csv
import json
class CSVToJsonConverter:
    def __init__(self, csvfile, jsonfile):
        self.csvfile = csvfile
        self.jsonfile = jsonfile
    def convert(self):
        data = []
        with open(self.csvfile, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        with open(self.jsonfile, 'w') as file:
            json.dump(data, file, indent=4)
        return f"{self.jsonfile}"
converter = CSVToJsonConverter('dummy.csv', 'output.json')
result = converter.convert()
print(result)
