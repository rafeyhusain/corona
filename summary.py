import pandas as pd
from csv_file import CsvFile
from muslims import Muslims

class Summary(CsvFile):

    def __init__(self, corona_path, muslims_path):
        super().__init__(corona_path)
        self.add_columns([
            'Muslim',
            'Total Population',
            'Muslim Population',
            'Percentage Muslim',
            'Percentage World Muslim'])
            
        self.save('./data/summary.csv')

        self.muslims = Muslims(muslims_path)


    def show(self):
        for index, row in self.df.iterrows():

            country = self.muslims.get_country(row['Country'])

            if (country is not None):
                self.df.at[index, 'Muslim'] = country['Muslim']  
                self.df.at[index, 'Total Population'] = country['Total Population'] 
                self.df.at[index, 'Muslim Population'] = country['Muslim Population']
                self.df.at[index, 'Percentage Muslim'] = country['Percentage Muslim']
                self.df.at[index, 'Percentage World Muslim'] = country['Percentage World Muslim']

        # TODO: Why it is not saving
        # self.save()
        self.df = self.df.replace('\,', '', regex=True)
        self.df.columns = self.df.columns.str.replace(' ', '')

        self.df.to_csv('./data/summary.csv', sep=',', encoding='utf-8')
        # print(self.df)
    
