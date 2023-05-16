import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)  # Load data from a CSV file

    def describe(self):
        total_rows = self.data.shape[0]
        null_values = self.data.isnull().sum()
        describe = pd.DataFrame([[index, i, round((i/total_rows)*100, 2), typ] for index, i, typ in zip(null_values.index, null_values, self.data.dtypes)], columns =["Field", "Null Values", "Percentage", "Datatype"])
        describe.set_index('Field', inplace=True)
        print("The file has {} rows and {} columns. Simple description of the file is:\n")
        print(describe)

    def clean_missing_data(self, method='mean'):
        if method == 'mean':
            self.data.fillna(self.data.mean(), inplace=True)
        elif method == 'median':
            self.data.fillna(self.data.median(), inplace=True)
        elif method == 'mode':
            self.data.fillna(self.data.mode().iloc[0], inplace=True)
        elif method == 'drop':
            self.data.dropna(inplace=True)
        else:
            raise ValueError('Invalid method: {}. Allowed one of [mean, median, mode, drop] methods'.format(method))

    def remove_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def standardize_formats(self):
        self.data['column_name'] = self.data['column_name'].str.lower()  # Example: convert to lowercase

    def remove_outliers(self, column_name, z_score_threshold=3):
        z_scores = np.abs((self.data[column_name] - self.data[column_name].mean()) / self.data[column_name].std())
        self.data = self.data[z_scores < z_score_threshold]

    def apply_transformations(self):
        self.data['column_name'] = self.data['column_name'].apply(lambda x: x**2)  # Example: square transformation

    def save_cleaned_data(self, output_path):
        self.data.to_csv(output_path, index=False)

# Example Usage
cleaner = DataCleaner("data.csv")  # Replace "data.csv" with your file path
cleaner.handle_missing_values(strategy='mean')
cleaner.remove_duplicates()
cleaner.standardize_formats()
cleaner.remove_outliers(column_name='column_name', z_score_threshold=3)
cleaner.apply_transformations()
cleaner.save_cleaned_data("cleaned_data.csv")  # Replace "cleaned_data.csv" with your desired output file path
