

import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        dtype={
            "user_id": str,
            "event_type": str,
            "product_id": str
        },
        parse_dates=["timestamp"],
        keep_default_na=False,
        skiprows=1,
        header=0,
        skipinitialspace=True 
    )
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)
    return df
