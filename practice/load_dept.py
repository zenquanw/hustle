import sqlite3
from pathlib import Path
import pandas as pd

# 用 __file__ 定位，换到任何目录运行都找得到数据
DATA = Path(__file__).parent / "data"

con = sqlite3.connect(DATA / "hustle.db")
dept = pd.read_csv(DATA / "dept.csv")
dept.to_sql("dept", con, if_exists="replace", index=False)
print(pd.read_sql("SELECT * FROM dept", con))
con.close()
