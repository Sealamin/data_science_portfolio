import pandas as pd

import os


class DataAnalyzer:

    def __init__(self, data_folder, analysis_folder):

        self.data_folder = data_folder

        self.analysis_folder = analysis_folder

        self.data_path = os.path.join(self.data_folder, 'data.csv')


    def load_data(self):

        self.df = pd.read_csv(self.data_path)


    def analyze_column(self, column_name):

        print(self.df[column_name].describe())

        print(self.df[column_name].mode().iloc[0])


if __name__ == '__main__':

    data_folder = '../source_data'

    analysis_folder = './'

    analyzer = DataAnalyzer(data_folder, analysis_folder)

    analyzer.load_data()

    column_name = 'Počty studentů s trvalým bydlištěm v dané obci dojíždějící do vyšší odborné školy'

    analyzer.analyze_column(column_name)
