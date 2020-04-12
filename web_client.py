import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
from csv_file import CsvFile

class WebClient:

    def save_as_csv(self, url, file_path):
        csv = CsvFile('./data/test.csv')
        
        html = './data/view-source_https___www.worldometers.info_coronavirus_.html'
        html = './data/table.html'

        f = open(html, "r") 
        soup = BeautifulSoup(f, 'html.parser')
        table = soup.find(id="main_table_countries_today")

        # add header
        columns = table.findAll('th')
        output_row = []
        for column in columns:
            output_row.append(csv.clean(column.text))
        
        csv.add_columns(output_row)
        #csv.delete_column('A')

        # add rows
        output_rows = []
        for table_row in table.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_rows.append(output_row)
            csv.add_row(output_row)

        csv.save('./data/abc.csv')