import pandas as pd
from csv_file import CsvFile

class Muslims(CsvFile):

    def __init__(self, csv_path):
        super().__init__(csv_path)


    def is_muslim(self, country):
        return len(self.get_country(country)) > 0 


    def get_country(self, country_name):
        country = {
            'Muslim': False,
            'Total Population': 0,
            'Muslim Population': 0,
            'Percentage Muslim': 0,
            'Percentage World Muslim': 0
            }

        row = self.get_first('Country', country_name)
        
        country['Total Population'] = self.to_float(row, 'Total Population', 0)
        country['Muslim Population'] = self.to_float(row, 'Muslim Population', 0)
        country['Percentage Muslim'] = self.to_float(row, 'Percentage Muslim', 0)
        country['Percentage World Muslim'] = self.to_float(row, 'Percentage World Muslim', 0)
        country['Muslim'] = True if float(country['Percentage Muslim']) > 50.0 else False

        return country


    def to_float(self, row, column_name, default_value):
        if(row is None or column_name is None):
            return default_value

        return super().to_float(row[column_name], default_value)
