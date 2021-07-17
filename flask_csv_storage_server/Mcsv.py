import csv
import pandas as pd
import os
import json

def write_rows(filename, rows):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    rows = json.loads(rows)
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


def write_row(filename, row):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)

def get_csv(filename):
    a = pd.read_csv(filename)
    a.rename( columns={'Unnamed: 0':'new column name'}, inplace=True )
    return a.to_html()

def remove_csv(filename):
    os.remove(filename)
