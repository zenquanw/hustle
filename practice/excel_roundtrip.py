"""练习：pandas 写 Excel + openpyxl 读回（全程在内存里，不生成文件）。

在 VSCode 里右键 ->「在终端中运行 Python 文件」。
"""
import io

import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "score": [88, 95, 73],
})

buffer = io.BytesIO()
df.to_excel(buffer, engine="openpyxl", index=False)
buffer.seek(0)

back = pd.read_excel(buffer, engine="openpyxl")
print("openpyxl version:", __import__("openpyxl").__version__)
print(back)
print("total:", int(back["score"].sum()))
