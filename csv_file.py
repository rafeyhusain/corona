import pandas as pd

class CsvFile:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path, encoding='utf-8')


    def set_column(self, country, column, value):
        row = self.get_country(country)
        row[column] = value 


    def add_column(self, column_name, default_value = None):
        index = len(self.df.columns)
        self.df.insert(index, column_name, default_value)


    def add_columns(self, column_names):
        self.df = pd.concat([self.df, pd.DataFrame(columns=column_names)])

    def delete_column(self, column_name):
        self.df.drop(column_name, axis=1, inplace=True)

    def save(self, file_name = None):
        self.df.to_csv(file_name, sep=',', encoding='utf-8')

    def get_first(self, column_name, value):
        result = self.df.loc[self.df[column_name] == value]

        if (len(result) > 0):
            return result.iloc[0]
        else:
            return None

    def add_row(self, row):
        row_df = pd.DataFrame([row])
        self.df = pd.concat([row_df, self.df], ignore_index=True)
        #self.df.drop(self.df.columns[[0]], axis=1, inplace=True)


    def to_float(self, s, default_value):
        try:
            s = str(s)
            s = s.replace(",", "")
            s = s.replace("<", "")
            s = s.replace("\xa0", "")
            s = s.replace("\n", "")
            if ("-" in s):
                s = s.split('-')[1 if len(s) > 1 else 0].strip()
            
            if ("?" in s):
                s = s.split('?')[1 if len(s) > 1 else 0].strip()
        except:
            s = default_value

        return float(s)