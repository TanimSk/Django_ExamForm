import csv
import os
import json

def write_rows(filename, rows):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    rows = json.loads(rows)
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


def write_row(filename, row):
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)

def get_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for r in reader:
            data.append(r)

    return data

def remove_csv(filename):
    os.remove(filename)
