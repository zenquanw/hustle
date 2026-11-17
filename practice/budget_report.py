"""把 dept（预算）和 sales（实际）拼成一张对账表，写成 budget_vs_actual.csv。

SQL 原文和逐句注释在 budget.sql 的「二、A」段，这里保持一致。
运行前先跑一次 load_dept.py 建好 dept 表。
"""
import sqlite3
from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data"

SQL = """
SELECT d.部门,
       d.预算,
       COUNT(s.姓名)                              AS 笔数,
       COALESCE(SUM(s.金额),0)                    AS 实际,
       d.预算 - COALESCE(SUM(s.金额),0)           AS 差额,
       ROUND(COALESCE(SUM(s.金额),0) * 100.0 / d.预算, 1) AS 执行率
FROM dept d LEFT JOIN sales s ON d.部门 = TRIM(s.部门)
GROUP BY d.部门, d.预算
ORDER BY d.预算 DESC
"""


def main():
    con = sqlite3.connect(DATA / "hustle.db")
    df = pd.read_sql(SQL, con)
    total = con.execute("SELECT COALESCE(SUM(金额),0) FROM sales").fetchone()[0]
    con.close()

    df = df.rename(columns={"执行率": "执行率(%)"})
    out = DATA / "budget_vs_actual.csv"
    df.to_csv(out, index=False, encoding="utf-8-sig")  # 带 BOM，Excel 打开中文不乱码

    print(df.to_string(index=False))
    print(f"\n合计（预算表内）：预算 {df['预算'].sum()} / 实际 {df['实际'].sum()} "
          f"/ 差额 {df['差额'].sum()} / 执行率 "
          f"{round(df['实际'].sum() / df['预算'].sum() * 100, 1)}%")
    print(f"全表实际是 {total}，差的 {total - df['实际'].sum()} "
          "是 2 笔没有部门预算的流水（未分配）")
    print(f"已写出：{out}")


if __name__ == "__main__":
    main()
