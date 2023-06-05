# Data analysis

Error Detection and Analysis

## Description

This Python project aims to detect errors in a dataset and provide an analysis report for clean data. The project is designed to be manually driven, meaning that it requires manual intervention to identify and resolve errors. Right now it
only works on a certain structure of the dataset.

## Features

- Error Detection: The project includes functionality to identify errors in the dataset. It employs various error detection algorithms and techniques to identify inconsistencies, outliers, missing values, or any other type of error.

- Manual Intervention: Once errors are detected, the project prompts the user to manually review and resolve them. It provides clear instructions on how to identify and correct the errors.

- Analysis Report: The project also includes a file that generates an analysis report for clean data. This report provides insights, statistical summaries, visualizations, and other relevant information about the dataset.

## Usage

1. Clone the project repository
2. Execute the error detection script:
   ```
   python detect-data-entry-errors.py
   ```
   This script will analyze the dataset and identify potential errors. It will prompt you to review and resolve the detected errors manually.
3. Once the errors are resolved, execute the analysis report script:
   ```
   python data_analysis_report.py
   ```
   This script will generate an analysis report for the clean data. The report will be saved to a specified output file.
