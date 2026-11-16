-- 1 先看看表长什么样
SELECT * FROM sales LIMIT 3;
-- 2 筛选 + 排序：金额大于 100 的，从大到小
SELECT 姓名, 部门, 金额 FROM sales WHERE 金额 > 100 ORDER BY 金额 DESC;
-- 3 分组汇总：这条要对上 by_dept.csv
SELECT COALESCE(TRIM(部门), '未分配') AS 部门,
COUNT(*) AS 笔数,
COUNT(金额) AS 有金额笔数,
SUM(金额) AS 合计
FROM sales GROUP BY 1 ORDER BY 合计 DESC;

-- 4 按日汇总：这条要对上 by_day.csv
SELECT 日期, SUM(金额) AS 合计 FROM sales GROUP BY 日期 ORDER BY 日期;
-- 5 缺失体检：一行看清缺了几处
SELECT COUNT(*) AS 总行数, COUNT(日期) AS 有日期, COUNT(金额) AS 有金额 FROM sales;