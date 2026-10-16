import csv

file_path = 'data/homework_invoices.csv'
def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        print("Now printing only rows with amount greater than 100000")
        invoices=[]
        count=0
        missing_fields = []
        for row in csv_reader:
            invoices.append(row)
            try:
                if(float(row['amount'])>100000):
                    count+=1
                    print(row)
            except ValueError as e:
                missing_fields.append(row)
                print(f"Error reading CSV file: {row}. Error: {e} ")
        print(f"Finished reading CSV file. Total rows: {len(invoices)}")
        print(f"Total rows with amount greater than 100000: {count}")
        print(f"Total rows with missing or invalid amount field: {len(missing_fields)}")

read_csv(file_path)

import pandas as pd

pd_df = pd.read_csv(file_path)
print(pd_df)
print(f"Total rows in the CSV file using pandas: {len(pd_df)}")
pd_df['amount']= pd.to_numeric(pd_df['amount'], errors='coerce')
missing_amount_rows = pd_df[pd_df['amount'].isna()]
print(f"Total rows with missing amount field using pandas: {len(missing_amount_rows)}")
print(f"Total rows with amount greater than 100000 using pandas: {len(pd_df[pd_df['amount']>100000])}")
print("Now printing only rows with amount greater than 100000 using pandas:")
print(pd_df[pd_df['amount']>100000])