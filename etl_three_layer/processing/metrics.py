import pandas as pd

def compute_user_metrics(df: pd.DataFrame) -> pd.DataFrame:
    purchases = df[df['event_type'] == 'purchase']
    total_purchases = purchases.groupby('user_id').size().rename('total_purchases')
    total_spent = purchases.groupby('user_id')['price'].sum().rename('total_spent')

    views = df[df['event_type'] == 'view']
    total_views = views.groupby('user_id').size().rename('total_views')

    summary = pd.concat([total_purchases, total_spent, total_views], axis=1).fillna(0)
    summary['conversion_rate'] = summary.apply(
        lambda r: (r['total_purchases'] / r['total_views']) if r['total_views'] else 0, axis=1)
    return summary.reset_index()

def top_product(purchases: pd.DataFrame):
    if purchases.empty:
        return None, 0
    product_counts = purchases.groupby('product_id').size()
    return product_counts.idxmax(), product_counts.max()
