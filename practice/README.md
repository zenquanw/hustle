# practice · 练习区

平时在 VSCode 里练的 `.py`、`.ipynb` 都放这个文件夹（也可以按日期/主题再建子文件夹）。

## 每日脚本

在仓库根目录 `hustle/` 下打开终端，直接跑：

```bash
python practice/read_csv.py    # 读 sample_gbk.csv，打印表结构 / 统计 / 筛选结果
python practice/clean.py       # 清洗数据，生成 by_dept.csv、by_day.csv、quality.csv
python practice/load_db.py     # 把 sample.csv 灌进 SQLite，建 sales 表
```

- 输出都落在 `practice/data/`；`query.sql` 是 `sales` 表的五个查询。
- 三个脚本都用 `__file__` 定位数据，换到别的目录运行也不会找不到文件。
- `clean.py` 可以接一个别的 csv 路径：`python practice/clean.py practice/data/sample_gbk.csv`。
- `quality.csv` 的「原始缺失 / 清洗后缺失」对比的是清洗前后同一张表，部门那行应是 2 / 0。

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
- `hello_pandas.py`（环境自检）、`excel_roundtrip.py`（pandas + openpyxl 往返）只是能跑通的起点，随便改或删
