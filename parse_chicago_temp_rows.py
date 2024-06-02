# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:06:42 2024

@author: gaurav
"""
import pandas as pd

import csv
from collections import defaultdict
from typing import TextIO


def aggregate_temperatures_df(reader, writer):
    # Read the CSV file
    df = pd.read_csv('test_full.csv')

    # Convert 'Date' column to datetime
    df['Measurement Timestamp'] = pd.to_datetime(df['Measurement Timestamp'], format='%m/%d/%Y %I:%M:%S %p')
    df = df.sort_values(by='Measurement Timestamp')

    # Extract the date part and store it in a new column 'Date'
    df['Date'] = df['Measurement Timestamp'].dt.date

    # Group by 'Station Name' and 'Date'
    grouped = df.groupby(['Station Name', 'Date'])

    # Aggregate the required values
    result = grouped.agg(
        Min_Temp=('Air Temperature', 'min'),
        Max_Temp=('Air Temperature', 'max'),
        First_Temp=('Air Temperature', 'first'),
        Last_Temp=('Air Temperature', 'last')
    ).reset_index()

    # Rename the columns
    result.columns = ['Station Name', 'Date', 'Min Temp', 'Max Temp', 'First Temp', 'Last Temp']
    result = result.sort_values(by='Date', ascending=False)
    # Save the result to a new CSV file
    result.to_csv('output.csv', index=False)

    print(result.to_csv(index=False))


def aggregate_temperatures(reader: TextIO, writer: TextIO):
    # Initialize a defaultdict to store aggregated temperature data
    aggregated_data = defaultdict(lambda: defaultdict(list))

    # Read the CSV file line by line
    csv_reader = csv.reader(reader)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        station_name, timestamp, temp = row
        date, time = timestamp.split(' ')
        date = '/'.join(date.split('-'))

        # Add temperature to aggregated data
        aggregated_data[station_name][date].append(float(temp))

    # Write aggregated data to the output CSV file
    csv_writer = csv.writer(writer)
    csv_writer.writerow(['Station Name', 'Date', 'Min Temp', 'Max Temp', 'First Temp', 'Last Temp'])

    for station_name, data in aggregated_data.items():
        for date, temps in data.items():
            min_temp = min(temps)
            max_temp = max(temps)
            first_temp = temps[0]
            last_temp = temps[-1]
            csv_writer.writerow([station_name, date, f'{min_temp:.1f}', f'{max_temp:.1f}', f'{first_temp:.1f}', f'{last_temp:.1f}'])

# Example usage:
with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    aggregate_temperatures(input_file, output_file)
