# 08 · 语料索引：回原文核对

## 一、语料位置

| 位置 | 内容 | 规模 |
| --- | --- | --- |
| `C:\Users\Administrator\Desktop\DanKoe-全集\` | 分类副本（本 skill 的提炼来源） | 557 文件 / 28MB |
| `G:/金句/DanKoe/` | 原始库（含未分类镜像） | 790 md / 550 独立作品 |
| `G:/金句/quotes/database/quotes.json` | 金句库（已评分入册 1,447 条） | 5,818 条 |

### 桌面全集的目录约定
```
01-一人公司与商业模式/ … 09-综合其他/   信件（268 篇；EN- 前缀为未译英文原文）
10-推文合集（X）/                       原创 2021–2026 + 「· 回复」2024–2026
11-视频转写（YouTube）/                 195 篇，按主题子目录
12-短视频（Shorts）/                    84 篇
13-短篇与专题/                          1 篇
00-总目录.html                          可搜索目录
```

## 二、按问题找原文

| 你想查 | 去哪里 |
| --- | --- |
| 某个具体观点出自哪篇 | 桌面全集 `00-总目录.html` 搜关键词 |
| 某条推文的原文/上下文 | `10-推文合集（X）/Dan Koe 推文双语合集 - YYYY.md`，按日期或链接 ID |
| 他的完整理论 | `09-综合其他/01-a-complete-knowledge-base-of-human-30.md` |
| 他的书《专注的艺术》 | `03-专注力与生产力/01-the-art-of-focus-official-book-summary-by-the-author-dan-koe.md` |
| 一人公司打法 | `01-一人公司与商业模式/12-…productize-yourself.md` + `16-…3-stages-of-monetization.md` |
| 写作方法 | `02-创作者经济与个人品牌/21-the-writing-habit-that-saved-my-brain.md` |
| 视频里的说法 | `11-视频转写（YouTube）/`，按主题子目录 |

## 三、命令行检索（Windows / Git Bash）

```bash
# 全库关键词（含中英）
cd "C:/Users/Administrator/Desktop/DanKoe-全集" && grep -rn "反利基\|anti-niche" . --include=*.md | head -20

# 只看信件
grep -rn "MVO\|最小可行" "01-一人公司与商业模式" | head

# 按推文 ID 找
grep -rn "2049864029032894649" "10-推文合集（X）"
```

## 四、引用规范

1. **推文**：`https://x.com/thedankoe/status/<id>`（每条合集里都有）。
2. **信件**：写标题 + 路径，例如「《The One-Person Business Model》」，路径见文件头 `> 原文：`。
3. **视频**：写 YouTube 链接（转写文件头有）。
4. 本 skill 里的中文多为库内译文，**引用英文原句时以 `【EN】` 段为准**。

## 五、更新语料

- 新增推文/文章：跑 `G:/金句/work/x-collect/` 下的 `collect_x.py`（X）、`fetch_site.py`（官网）、`fetch_shorts.py`（Shorts）。
- 重建桌面副本：`build_desktop.py`；重建目录 HTML：`make_index_html.py`。
- 语料更新后，本 skill 的模型与语录不需要重写；只需在 `07-quote-bank.md` 里补新条目。
