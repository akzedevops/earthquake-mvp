import pandas as pd
def load_earthquake_csv(path):
    df = pd.read_csv(path)
    return df

def filter_by_date(df, start_date, end_date):
    df['date'] = pd.to_datetime(df['time_iso']).dt.date
    return df[(df['date'] >= start_date) & (df['date'] <= end_date)]