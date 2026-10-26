# -*- coding: utf-8 -*-
"""渲染 dan-koe-thinking 的技能市场预览图（3 张，纯本地绘制，中文逐字可控）。"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
BG = (11, 11, 12)
FG = (243, 240, 232)
MUT = (139, 139, 133)
ACC = (217, 161, 91)
LINE = (42, 42, 42)

EN_B = r"C:\Windows\Fonts\georgiab.ttf"
EN = r"C:\Windows\Fonts\georgia.ttf"
CN_B = r"C:\Windows\Fonts\msyhbd.ttc"
CN = r"C:\Windows\Fonts\msyh.ttc"


def F(path, size):
    return ImageFont.truetype(path, size)


def canvas(w, h):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    # 细网格
    for x in range(0, w, 80):
        d.line([(x, 0), (x, h)], fill=(20, 20, 21))
    for y in range(0, h, 80):
        d.line([(0, y), (w, y)], fill=(20, 20, 21))
    return img, d


def text(d, xy, s, font, fill=FG):
    d.text(xy, s, font=font, fill=fill)


def cover_16x9():
    w, h = 1600, 900
    img, d = canvas(w, h)
    m = 96
    text(d, (m, 78), "SKILL PREVIEW  /  THINKING SYSTEM", F(EN, 22), MUT)
    d.line([(m, 130), (m + 120, 130)], fill=ACC, width=3)

    text(d, (m, 190), "Dan Koe", F(EN_B, 172))
    text(d, (m + 6, 392), "思想操作系统", F(CN_B, 92))
    text(d, (m + 10, 520), "五个底层判断 · 四个模型 · 十条决策启发式 · 三种工作模式", F(CN, 34), MUT)

    d.line([(m, 640), (w - m, 640)], fill=LINE, width=1)
    stats = [("268", "篇官网信件"), ("5,374", "条 X 推文"), ("279", "条视频转写")]
    x = m
    for num, label in stats:
        text(d, (x, 690), num, F(EN_B, 64), FG)
        text(d, (x, 772), label, F(CN, 26), MUT)
        x += 400
    text(d, (m + 1200, 700), "52 条语录", F(CN_B, 30), ACC)
    text(d, (m + 1200, 742), "每条带推文直链", F(CN, 22), MUT)

    # 右侧模型列表
    rx = 1130
    text(d, (rx, 196), "四个模型", F(CN, 26), ACC)
    models = ["专注公式", "HUMAN 3.0", "一人公司", "AQAL 思考法"]
    yy = 250
    for i, name in enumerate(models, 1):
        text(d, (rx, yy), "0%d" % i, F(EN, 26), MUT)
        text(d, (rx + 60, yy - 4), name, F(CN, 34), FG)
        yy += 76
    text(d, (rx, 806), "dan-koe-thinking  ·  v1.0.0", F(EN, 22), MUT)
    img.save(os.path.join(OUT, "01-cover-16x9.png"), optimize=True)
    return "01-cover-16x9.png"


def poster_3x4():
    w, h = 1080, 1440
    img, d = canvas(w, h)
    m = 80
    text(d, (m, 70), "DAN KOE  /  SKILL", F(EN, 20), MUT)
    text(d, (m, 120), "把 5500 条推文", F(CN_B, 64))
    text(d, (m, 200), "变成一套判断", F(CN_B, 64))
    text(d, (m, 300), "不是语录合集，是遇到问题时该调用哪个模型。", F(CN, 26), MUT)
    d.line([(m, 360), (w - m, 360)], fill=LINE, width=1)

    items = [
        ("01", "专注公式", "反愿景 → 愿景 → 目的 → 路径 → 优先级"),
        ("02", "HUMAN 3.0", "心智 / 身体 / 精神 / 事业，四象限定位瓶颈"),
        ("03", "一人公司", "品牌 → 内容 → 产品（MVO）→ 营销"),
        ("04", "AQAL 思考", "个人内在 / 外在，集体内在 / 外在，四视角过一遍"),
    ]
    y = 410
    for num, name, desc in items:
        text(d, (m, y), num, F(EN_B, 34), ACC)
        text(d, (m + 70, y - 6), name, F(CN_B, 40))
        text(d, (m + 70, y + 56), desc, F(CN, 24), MUT)
        y += 168

    d.line([(m, 1105), (w - m, 1105)], fill=LINE, width=1)
    text(d, (m, 1140), "268 篇信件 ｜ 5,374 条推文 ｜ 279 条视频", F(CN, 24), MUT)
    text(d, (m, 1190), "52 条语录带推文直链 · 引用可回溯", F(CN, 24), MUT)
    text(d, (m, 1300), "dan-koe-thinking  ·  v1.0.0", F(EN, 20), MUT)
    img.save(os.path.join(OUT, "02-poster-3x4.png"), optimize=True)
    return "02-poster-3x4.png"


def grid_16x9():
    w, h = 1600, 900
    img, d = canvas(w, h)
    m = 80
    text(d, (m, 56), "FOUR MODELS", F(EN, 20), MUT)
    text(d, (m, 92), "四个可操作模型", F(CN_B, 52))

    cards = [
        ("01  专注公式", ["反愿景：写清不想要什么", "愿景：具体到场景与数字", "目的：最该解决却拖着的问题", "路径 + 今天的 2–4 小时"]),
        ("02  HUMAN 3.0", ["四象限：心智/身体/精神/事业", "三层级：从众→个人→综合", "三相位：失调→不确定→发现", "只修瓶颈象限，90 天"]),
        ("03  一人公司", ["三路径：技能/发展/结合", "四市场：健康·财富·关系·幸福", "四支柱：品牌·内容·产品·营销", "MVO：$500 起，先卖再做"]),
        ("04  AQAL 思考", ["个人内在：价值观与恐惧", "个人外在：技能与行动", "集体内在：文化与期待", "集体外在：系统与趋势"]),
    ]
    cw, ch = 700, 300
    gap = 34
    x0, y0 = m, 190
    for i, (title, bullets) in enumerate(cards):
        cx = x0 + (i % 2) * (cw + gap)
        cy = y0 + (i // 2) * (ch + gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=(17, 17, 18), outline=(38, 38, 38))
        text(d, (cx + 34, cy + 28), title, F(CN_B, 34), FG)
        d.line([(cx + 34, cy + 84), (cx + cw - 34, cy + 84)], fill=(38, 38, 38))
        yy = cy + 108
        for b in bullets:
            text(d, (cx + 34, yy), "·", F(CN_B, 24), ACC)
            text(d, (cx + 58, yy), b, F(CN, 24), MUT)
            yy += 46
    text(d, (m, h - 52), "dan-koe-thinking  ·  references/01–04", F(EN, 20), MUT)
    img.save(os.path.join(OUT, "03-models-16x9.png"), optimize=True)
    return "03-models-16x9.png"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn in (cover_16x9(), poster_3x4(), grid_16x9()):
        p = os.path.join(OUT, fn)
        print(fn, "%.1f KB" % (os.path.getsize(p) / 1024))
