# hustle · 作品陈列架

一个公开的作品柜：任何人打开这个链接，都能看到我做过什么。

## 作品列表

| 作品 | 做了什么 | 用到的工具 | 状态 |
| --- | --- | --- | --- |
| _示例：Excel 数据整理_ | 读取表格、清洗数据、生成汇总报表 | Python · pandas · openpyxl | 示例中，请替换 |

> 第一行只是格式示范，换成自己的作品即可。说明文档放 `projects/`，截图放 `assets/`。

## 目录

```
projects/   每个作品一个文件夹，内含 README.md
practice/   平时练习的代码（.py / .ipynb）
assets/     截图、图片等素材
tools/      sync.ps1 一键推送脚本
.vscode/    本仓库的 VSCode 配置（提交后自动 push）
```

## 在 VSCode 里练习，代码自动进 GitHub

**前提**：用 VSCode 打开**整个 `hustle` 文件夹**（不是单个 .py 文件），Git 才会接管它。
路径：`C:\Users\86158\WorkBuddy\内存清理\hustle`

**方式 A：提交即自动推送（已配好，日常推荐）**

1. 在 `practice/` 里写代码，保存
2. `Ctrl + Shift + G` 打开源代码管理
3. 消息框写一句这次练了什么，点 **✓ 提交**
4. VSCode 会**自动 push**，刷新本页就能看到

**方式 B：一键推送（`Ctrl + Shift + B`）**

按 `Ctrl + Shift + B` → 输入一句说明（直接回车用时间戳）→ 脚本自动完成 `add` / `commit` / `push`。
新建了文件、一次改了好几处、或不想点面板时用这个最省事。

> 两种方式都是同步整个仓库，不限于 `practice/`。
> 想做到「一保存就立刻推」需要额外装自动保存触发插件，日常不建议：会产生大量零碎提交，误写的密钥也会立刻公开。

## 添加新作品

1. 在 `projects/` 下新建文件夹，例如 `projects/first-work/`
2. 写一份 `README.md`：解决什么问题、怎么运行、效果截图
3. 回到本页「作品列表」补一行
4. 提交：

```bash
git add .
git commit -m "add: 新作品"
git push
```

## 本地信息

- 仓库位置：`C:\Users\86158\WorkBuddy\内存清理\hustle`
- Python 环境：conda `hustle`（Python 3.11 · pandas · openpyxl · Jupyter）

---

公开仓库，请勿提交密码、密钥或个人信息。
