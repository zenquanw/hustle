import sys
import pandas as pd

from read_csv import load        # 复用昨天的函数

def summarize(df):
    df = df.assign(部门=df['部门'].str.strip())
    print(df.groupby('部门')['金额'].agg(['count', 'sum']))
    df.groupby('部门', as_index=False)['金额'].sum().to_csv(
        'practice/data/summary.csv', index=False, encoding='utf-8-sig')
    print('已写出 summary.csv')

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else 'practice/data/sample.csv'
    df = load(path)
    if df is not None:
        print(df.shape, df.isna().sum().to_dict())
        summarize(df)
