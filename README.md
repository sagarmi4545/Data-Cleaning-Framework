# Data Cleaning Framework using Pandas

## Introduction
This Python framework provides a convenient way to clean and preprocess your data using the powerful pandas library. Data cleaning is an essential step in the data analysis process to ensure data integrity and quality. This framework offers various functionalities to handle missing values, remove duplicates, standardize formats, remove outliers, apply transformations, and save the cleaned data.

## Features
- **Data Description**: Get a simple description of the dataset, including the number of rows, columns, null values, and data types.
- **Missing Data Handling**: Clean missing values using methods such as mean, median, mode, or drop.
- **Duplicate Removal**: Remove duplicate records from the dataset.
- **Format Standardization**: Standardize formats of selected columns (e.g., convert text to lowercase).
- **Outlier Removal**: Remove outliers from a specific column using the z-score method.
- **Data Transformations**: Apply custom transformations to selected columns (e.g., square transformation).
- **Data Saving**: Save the cleaned data to a new CSV file.

## Usage
1. Instantiate the `DataCleaner` class by providing the file path of your dataset.
2. Use the available methods to clean and preprocess your data:
    - `describe()`: Display a simple description of the dataset, including null values and data types.
    - `clean_missing_data(method)`: Handle missing values using mean, median, mode, or drop methods.
    - `remove_duplicates()`: Remove duplicate records from the dataset.
    - `standardize_formats()`: Standardize formats of selected columns.
    - `remove_outliers(column_name, z_score_threshold)`: Remove outliers from a specific column.
    - `apply_transformations()`: Apply custom transformations to selected columns.
    - `save_cleaned_data(output_path)`: Save the cleaned data to a new CSV file.
3. Customize the cleaning operations and parameters according to your specific requirements.

## Example
```python
from data_cleaner import DataCleaner

# Instantiate the DataCleaner class
cleaner = DataCleaner("data.csv")

# Get data description
cleaner.describe()

# Handle missing values using the mean method
cleaner.clean_missing_data(method='mean')

# Remove duplicate records
cleaner.remove_duplicates()

# Standardize formats of selected columns
cleaner.standardize_formats()

# Remove outliers from a specific column
cleaner.remove_outliers(column_name='column_name', z_score_threshold=3)

# Apply custom transformations to selected columns
cleaner.apply_transformations()

# Save the cleaned data to a new CSV file
cleaner.save_cleaned_data("cleaned_data.csv")


## Requirements

* pandas
* numpy

## Contribution

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
