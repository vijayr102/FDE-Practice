import csv

file_path = 'data/diabetic_data.csv'
def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
            break

read_csv(file_path)