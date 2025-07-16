
import pandas as pd
import os

def write_csv(df: pd.DataFrame, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(df)
    df.to_csv(path, index=False)
    print(f"Summary written to {path}")
