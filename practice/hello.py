import pandas as pd
df = pd.DataFrame({
"日期": ["2026-11-10", "2026-11-11"],
"金额": [120.5, 88.0],
})
print(df.shape)
print(df.head())
df.to_csv("out.csv", index=False)