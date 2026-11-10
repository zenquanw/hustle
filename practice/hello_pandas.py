"""练习起点：确认 hustle 环境可用，顺便造一张小表。

在 VSCode 里打开本文件，右键 ->「在终端中运行 Python 文件」即可。
"""
import pandas as pd

df = pd.DataFrame({
    "step": ["read", "clean", "summary"],
    "done": [True, True, False],
})

print("pandas version:", pd.__version__)
print(df)
print("rows:", len(df), "| columns:", list(df.columns))
