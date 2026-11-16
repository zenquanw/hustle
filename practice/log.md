2026-11-10
1. 今天做的：环境 + hello.py 跑通 + 第一次提交
2. 卡住的：文件没加 .py 后缀，Code Runner 去调 swift 了
3. 明天第一件事：写 funcs.py 的第 1 个函数
4. 实际投入：约 120 分钟
5. 产物：github.com/zenquanw/hustle

2026-11-11
1. 今天做的：十个函数练习并提交github
2. 卡住的：对函数的实际理解还是不明白，很多细节没到位
3. 明天第一件事：写读一张真表格
4. 实际投入：约100分钟
5. 实际产物：github.com/zenquanw/hustle

2026-11-12
1. 今天做的：读一张真表格，连出错也要能应付
2. 卡住的：在报错时无法准确的找到错误代码
3. 明天第一件事：把脚本变成工具
4. 实际投入30分钟
5. 实际产物：github.com/zenquanw/hustle

2026-11-13
1. 今天做的：把脚本变成工具
2. 卡住的：对长代码练习不熟练
3. 明天第一件事：让别人也能看懂
4. 实际投入120分钟
5. 实际产物：github.com/zenquanw/hustle

2026-11-14
1. 今天做的：clean.py 补上主入口，串起「读表 → 清洗 → 出三张汇总表」，修掉 5 处 API 笔误（srtip / drop_duplicate / utf-6-sig / dt.data / 金额.str）
2. 卡住的：只写 def 没有调用，脚本不报错也不生成文件；.str 只能用在文字列，金额列是数字不能用
3. 明天第一件事：把 sample.csv 灌进 SQLite，用 SQL 重算 by_dept
4. 实际投入：待补（当天没有单独计时）
5. 实际产物：by_dept.csv、by_day.csv、quality.csv，github.com/zenquanw/hustle

复盘（W1 收尾）
- 交付了什么：一条能重复跑出三张汇总表的流水线，不是只在我自己电脑上能跑的一次性代码
- 卡在哪：路径依赖当前目录、函数定义了却没调用、pandas 的 API 名字记不准
- 下周少做什么：少手敲长串 API 和路径，先跑通最小一段再往上加；出错先打印变量确认，不要反复猜
- 投入几小时：待补

2026-11-16
1. 今天做的：SQL 第一次上手。load_db.py 建好 practice/data/hustle.db，sales 表 7 行；五条查询全部出数；部门汇总 4 行合计 949，和 by_dept.csv 一致
2. 卡住的：SQL 按日汇总出 7 行 949，pandas 只有 6 行 649 —— 差的 300 是六赵那条没日期的记录，SQL 把 NULL 单独成组，pandas 默认丢掉
3. 明天第一件事：学 JOIN 和子查询，用两张表做关联
4. 实际投入：待补
5. 实际产物：hustle.db、load_db.py、query.sql，github.com/zenquanw/hustle