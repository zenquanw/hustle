-- W2D2 · 两张表对一对
-- 表：dept（部门预算，4 行）  sales（流水，7 行）
-- 注意 sales 灌的是未经清洗的 sample.csv，部门值带前后空格，
-- 所以 JOIN 条件必须写 TRIM(s.部门)，否则 ' 办公室 ' ≠ '办公室' 会匹配不上。

-- ===== 一、三种 JOIN，先看谁被留下（按部门分组后的行数）=====

-- 1 INNER JOIN：只留两张表都有的部门 → 3 行，合计 661
--   技术部（只有预算）、未分配（只有流水）都消失
SELECT d.部门,
       COUNT(s.姓名)           AS 笔数,
       COALESCE(SUM(s.金额),0) AS 实际
FROM dept d JOIN sales s ON d.部门 = TRIM(s.部门)
GROUP BY d.部门
ORDER BY d.部门;

-- 2 dept LEFT JOIN sales：预算表当主表 → 4 行，合计 661
--   技术部留在表里，显示 0 笔 0 元；未分配的 288 元消失
SELECT d.部门,
       d.预算,
       COUNT(s.姓名)           AS 笔数,
       COALESCE(SUM(s.金额),0) AS 实际
FROM dept d LEFT JOIN sales s ON d.部门 = TRIM(s.部门)
GROUP BY d.部门, d.预算
ORDER BY d.预算 DESC;

-- 3 sales LEFT JOIN dept：流水表当主表 → 4 行，合计 949
--   未分配的 288 元回来了；技术部消失（预算表里没有一行流水）
SELECT COALESCE(TRIM(s.部门), '未分配') AS 部门,
       COUNT(*)                AS 笔数,
       COALESCE(SUM(s.金额),0) AS 实际
FROM sales s LEFT JOIN dept d ON d.部门 = TRIM(s.部门)
GROUP BY COALESCE(TRIM(s.部门), '未分配')
ORDER BY 实际 DESC;

-- ===== 二、A 预算 vs 实际（budget_report.py 用的就是这条）=====
-- 执行卡原文按「差额 DESC」排；这里按预算降序，顺序对齐卡片第五节表格，数字不变
SELECT d.部门,
       d.预算,
       COUNT(s.姓名)                              AS 笔数,
       COALESCE(SUM(s.金额),0)                    AS 实际,
       d.预算 - COALESCE(SUM(s.金额),0)           AS 差额,
       ROUND(COALESCE(SUM(s.金额),0) * 100.0 / d.预算, 1) AS 执行率
FROM dept d LEFT JOIN sales s ON d.部门 = TRIM(s.部门)
GROUP BY d.部门, d.预算
ORDER BY d.预算 DESC;

-- ===== 三、子查询：括号里先算，结果喂给外面 =====

-- 先看平均是多少（金额有 6 个非空值，949 / 6 ≈ 158.17）
SELECT ROUND(AVG(金额), 2) AS 均值 FROM sales;

-- 再筛出比平均值高的 → 实际是 2 笔（300、200）
-- 执行卡写「应该出来 4 笔：300 / 200 / 150 / 120.5」，但均值是 158.17，
-- 150 和 120.5 都比均值小，用 > 永远筛不出来。卡片这里和它自己的数字对不上。
-- AVG 会自动跳过 NULL：分母是 6 个有金额的行，不是 7 行。
-- TRIM(姓名) 是因为原始流水里姓名也带空格
SELECT TRIM(姓名) AS 姓名, 金额 FROM sales
WHERE 金额 > (SELECT AVG(金额) FROM sales)
ORDER BY 金额 DESC;

-- 卡片列的那 4 笔其实是「金额最高的 4 笔」，这是另一个问题：
-- 用排序 + LIMIT，而不是跟平均值比
SELECT TRIM(姓名) AS 姓名, 金额 FROM sales
WHERE 金额 IS NOT NULL
ORDER BY 金额 DESC
LIMIT 4;
