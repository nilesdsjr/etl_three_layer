
#!/usr/bin/env python3
import os
from input.csv_loader import read_csv
from processing.metrics import compute_user_metrics, top_product
from output.csv_writer import write_csv

def run_pipeline(input_path: str, output_path: str):
    df = read_csv(input_path)

    summary = compute_user_metrics(df)
    purchases = df[df['event_type'] == 'purchase']
    prod_id, prod_qty = top_product(purchases)
    summary['top_product_id'] = prod_id
    summary['top_product_quantity'] = prod_qty
    write_csv(summary, output_path)

if __name__ == '__main__':

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data", "test.csv")
    result_dir = os.path.join(script_dir, "data", "result", "summary.csv")

    run_pipeline(file_path, result_dir)
