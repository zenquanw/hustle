import sqlite3
from pathlib import Path
import pandas as pd
from read_csv import load

# 用 __file__ 定位，换到任何目录运行都找得到数据
DATA = Path(__file__).parent / "data"

df = load(DATA / "sample.csv")
con = sqlite3.connect(DATA / "hustle.db")
df.to_sql("sales", con, if_exists="replace", index=False)
print(pd.read_sql("SELECT COUNT(*) AS 行数 FROM sales", con))
con.close()
