import sys
from pathlib import Path
import pandas as pd
from read_csv import load

DATA = Path(__file__).parent / "data"


def clean(df):
    df = df.copy()
    df["姓名"] = df["姓名"].str.strip()
    df["部门"] = df["部门"].str.strip().fillna("未分配")
    # 金额本来已是 float64，不能再对它用 .str；to_numeric 负责把异常值变成 NaN
    df["金额"] = pd.to_numeric(df["金额"], errors="coerce")
    df["日期"] = pd.to_datetime(df["日期"], errors="coerce")
    return df.drop_duplicates()


def tables(df, out=DATA):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)

    dept = df.groupby("部门")["金额"].agg(["count", "sum"])
    dept["占比"] = (dept["sum"] / dept["sum"].sum() * 100).round(1)
    dept.to_csv(out / "by_dept.csv", encoding="utf-8-sig")

    day = df.groupby(df["日期"].dt.date)["金额"].sum().reset_index()
    day.columns = ["日期", "金额"]
    day.to_csv(out / "by_day.csv", index=False, encoding="utf-8-sig")

    q = pd.DataFrame({"列": df.columns,
                      "缺失数": [df[c].isna().sum() for c in df.columns]})
    q.to_csv(out / "quality.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DATA / "sample.csv"
    df = load(path)
    if df is not None:
        tables(clean(df))
        print("已生成 3 个文件：by_dept.csv / by_day.csv / quality.csv")
