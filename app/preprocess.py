import pandas as pd
import csv

def csv_to_txt(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    return rows

def xlsx_to_csv(xlsx_path):
    xlsx = pd.read_excel(xlsx_path)
    xlsx.to_csv(xlsx_path.replace(".xlsx",".csv"))


if __name__ == "__main__":
    xlsx_to_csv("app/data/xmall_data_v2.5.xlsx")