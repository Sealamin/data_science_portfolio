import pandas as pd

import matplotlib.pyplot as plt

import os


class DataAnalyzer:

    def __init__(self, data_folder, analysis_folder):

        self.data_folder = data_folder

        self.analysis_folder = analysis_folder

        self.data_path = os.path.join(self.data_folder, 'data.csv')


    def load_data(self):

        self.df = pd.read_csv(self.data_path)


    def analyze_regions(self):

        regions_count = self.df['Zřizovatel'].value_counts()

        return regions_count


    def plot_regions(self, regions_count):

        plt.figure(figsize=(8,4))

        plt.bar(regions_count.index, regions_count.values)

        plt.xlabel('Typ zřizovatele SŠ')

        plt.ylabel('Počet zřizovatelů')

        plt.title('Počty zřizovatelů SŠ dle typu pro Královehradecký kraj')

        plt.show()


if __name__ == '__main__':

    data_folder = 'ource_data'

    analysis_folder = 'analysis'

    analyzer = DataAnalyzer(data_folder, analysis_folder)

    analyzer.load_data()

    regions_count = analyzer.analyze_regions()

    analyzer.plot_regions(regions_count)
