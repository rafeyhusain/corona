import pandas as pd
import matplotlib.pyplot as plt
from summary import Summary
from web_client import WebClient

def main():
    #webclient = WebClient()
    #webclient.save_as_csv('https://www.worldometers.info/coronavirus/', './data/corona.csv')

    summary = Summary('./data/corona.csv', './data/muslims.csv')
    summary.show()


if __name__ == '__main__':
    main()