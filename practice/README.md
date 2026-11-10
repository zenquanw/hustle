# practice · 练习区

平时在 VSCode 里练的 `.py`、`.ipynb` 都放这个文件夹（也可以按日期/主题再建子文件夹）。

## 写完后怎么进 GitHub

**方式 A：提交即自动推送**（已配好，推荐）
1. 保存文件
2. `Ctrl + Shift + G` 打开源代码管理
3. 消息框写一句这次练了什么，点 ✓ 提交 → VSCode 会自动 push

**方式 B：一键脚本**
`Ctrl + Shift + B`，输入一句说明（直接回车用时间戳），自动完成 add / commit / push。

两种方式都会同步整个 `hustle` 仓库，不只是 `practice/`。

## 环境

VSCode 的 Python 解释器已指向 conda 环境 `hustle`（Python 3.11 · pandas 3.1.1 · openpyxl 3.1.5 · Jupyter）。
按 `Ctrl + Shift + P` → `Python: Select Interpreter` 可切换。

## 注意

- `__pycache__`、`.ipynb_checkpoints`、`.env` 等已被 `.gitignore` 排除，不会推上去
- 这是**公开仓库**：密码、密钥、身份证号、真实数据不要写进代码里
- `hello_pandas.py` 只是能跑通的起点，随便改或删
