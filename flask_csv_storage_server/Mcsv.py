import csv
import pandas as pd
import os
import json

def write_file(filename, row, mode):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    row = json.loads(row)
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if mode == 'q':
            csvwriter.writerows(row)
        else:
            csvwriter.writerow(row)


def write_row(filename, row):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)

def get_csv(filename, mode):
    a = pd.read_csv(filename)
    if mode == 1:
        return [a.to_html(), a['marks'].max(), a['marks'].mean()]

    return a.to_html()

def remove_csv(filename):
    os.remove(filename)
