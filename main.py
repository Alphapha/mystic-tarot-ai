"""
Mystic Tarot AI - AI塔罗占卜大师 主程序
基于 rich 的神秘风命令行界面,提供每日运势、单牌占卜、三牌阵占卜等功能
运行:python main.py
"""

import os
import sys
import time
import random
from datetime import date

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt
from rich.box import ROUNDED
from rich.markdown import Markdown

import tarot_engine as te
import astrology as ast
import ai_advisor as ai


console = Console()

# 神秘主题配色
THEME = {
    "primary": "bold magenta",
    "secondary": "gold1",
    "accent": "cyan",
    "muted": "grey50",
    "good": "green3",
    "warn": "orange3",
    "bad": "red3",
}

BANNER = r"""
 __  __ _   _ ____ ___ _   _ ____    __   ____ ___ _____   ____   ___   ___ ___
|  \/  | | | / ___|_ _| \ | / ___|   \ \ / / ___|_   _\ \ / / |  / _ \ / __|_ _|
| |\/| | | | \___ \| ||  \| \___ \    \ V / |     | |  \ V /| | | | | | |_ | |
| |  | | |_| |___) | || |\  |___) |    | || |___  | |   | | | |__| |_| |__|| |
|_|  |_|\___/|____/___|_| \_|____/     | | \____| |_|   |_| |_|\____/\___|  |___|
                                        \_\
"""


def sleep_pause(seconds=0.6):
    """短暂的停顿,营造仪式感"""
    time.sleep(seconds)


def print_banner():
    """打印启动 Banner 与欢迎语"""
    console.print(BANNER, style=THEME["secondary"])
    console.print(
        Align.center(
            Text("✨ 一手牌,一段命运。让塔罗为你照见此刻 ✨", style=THEME["primary"])
        )
    )
    if ai.is_ai_available():
        console.print(Align.center(Text(f"[AI 解读已启用 · 模型 {ai.OPENAI_MODEL}]", style=THEME["accent"])))
    else:
        console.print(Align.center(Text("[本地解读模式 · 配置 .env 可启用 AI 解读]", style=THEME["muted"])))
    console.print()


def print_card_panel(card, position=None):
    """以卡片样式渲染单张塔罗牌"""
    orientation = "逆位 ⮌" if card.get("is_reversed") else "正位 ⮞"
    arcana_label = "大阿尔卡那" if card["arcana"] == "major" else f"小阿尔卡那 · {card['suit']}"
    interp = te.interpret_card(card)

    title = f"{card['name_cn']}  ·  {card['name_en']}"
    if position:
        title = f"[{position}]  " + title

    body = Table.grid(padding=(0, 1))
    body.add_column(style=THEME["secondary"], justify="right")
    body.add_column()
    body.add_row("牌组:", arcana_label)
    body.add_row("朝向:", orientation)
    body.add_row("元素:", card.get("element", "—"))
    body.add_row("对应:", card.get("astrology", "—"))
    body.add_row("关键字:", interp["keywords"])
    body.add_row(Text("含义:", style=THEME["accent"]), Text(interp["meaning"]))

    border_style = "magenta" if card["arcana"] == "major" else "gold1"
    console.print(Panel(body, title=title, title_align="left", border_style=border_style, box=ROUNDED, padding=(1, 2)))


def menu():
    """渲染主菜单"""
    options = [
        ("1", "今日运势", "星座运势 + 幸运色 / 数字"),
        ("2", "每日一牌", "抽一张牌作为今日指引"),
        ("3", "三牌阵占卜", "过去 · 现在 · 未来"),
        ("4", "查看历史", "回看你的占卜记录"),
        ("5", "清空历史", "清除全部占卜记录"),
        ("0", "退出", "关闭程序"),
    ]
    table = Table.grid(padding=(0, 2))
    table.add_column(style=THEME["secondary"], justify="right")
    table.add_column(style=THEME["primary"])
    table.add_column(style=THEME["muted"])
    for key, name, desc in options:
        table.add_row(key, name, desc)
    console.print(Panel(table, title="✦ 占卜菜单 ✦", title_align="center", border_style=THEME["primary"], box=ROUNDED))


def handle_daily_fortune():
    """每日运势"""
    console.print(Panel("[bold]请输入你的星座或生日[/bold]\n示例:狮子座 / 1995-08-15", border_style=THEME["accent"]))
    user_input = Prompt.ask("输入").strip()

    sign = None
    if "-" in user_input and len(user_input.split("-")) == 3:
        try:
            sign = ast.get_zodiac_by_date(user_input)
        except ValueError:
            pass
    else:
        for s in ast.ZODIAC_SIGNS:
            if user_input == s["sign"] or user_input in s["sign"]:
                sign = s["sign"]
                break

    if not sign:
        console.print("[red]无法识别星座或生日,请重试。[/red]")
        return

    console.print(f"\n[bold magenta]正在为 {sign} 凝视今日星轨...[/bold magenta]")
    sleep_pause(0.8)

    fortune = ast.generate_daily_fortune(sign)
    info = ast.get_sign_info(sign)

    # 顶部信息
    head = Table.grid(padding=(0, 2))
    head.add_column(style=THEME["secondary"])
    head.add_column()
    head.add_row("星座:", f"{sign} ({info['element']} · 守护星 {info['ruler']})")
    head.add_row("日期:", fortune["date"])
    head.add_row("特质:", info["trait"])
    console.print(Panel(head, title="★ 今日运势 ★", title_align="center", border_style=THEME["primary"], box=ROUNDED))

    # 各维度评分
    dims_table = Table(title="运势维度", box=ROUNDED, border_style=THEME["accent"])
    dims_table.add_column("维度", style=THEME["secondary"])
    dims_table.add_column("评分", justify="center")
    for dim, score in fortune["dimensions"].items():
        stars = "★" * score + "☆" * (5 - score)
        color = THEME["good"] if score >= 4 else THEME["warn"] if score >= 3 else THEME["bad"]
        dims_table.add_row(dim, Text(stars, style=color))
    dims_table.add_row("综合", Text(f"{fortune['overall_score']} / 5.0", style=THEME["primary"]))
    console.print(dims_table)

    # 幸运信息
    lucky = Table.grid(padding=(0, 2))
    lucky.add_column(style=THEME["secondary"])
    lucky.add_column()
    lucky.add_row("幸运色:", f"{fortune['lucky_color']}({fortune['color_meaning']})")
    lucky.add_row("幸运数字:", str(fortune["lucky_number"]))
    lucky.add_row("幸运方位:", fortune["lucky_direction"])
    console.print(Panel(lucky, title="✦ 幸运指引 ✦", border_style=THEME["secondary"], box=ROUNDED))

    console.print(Panel(fortune["mood_quote"], title="今日寄语", border_style=THEME["accent"], box=ROUNDED))

    te.save_history({
        "type": "daily_fortune",
        "sign": sign,
        "fortune": fortune,
    })
    console.print("\n[dim]记录已保存到 history.json[/dim]\n")


def handle_single_card():
    """每日一牌"""
    question = Prompt.ask("\n[bold]心中所问(可直接回车跳过)[/bold]", default="今日指引").strip()
    console.print("\n[bold magenta]闭眼,呼吸,洗牌中...[/bold magenta]")
    sleep_pause(1.0)
    card = te.draw_single()
    print_card_panel(card)

    interp_text = ai.ai_interpret(question, [card]) or ai.local_interpret(question, [card])
    console.print(Panel(interp_text, title="✦ 占卜师解读 ✦", border_style=THEME["accent"], box=ROUNDED))

    te.save_history({
        "type": "single_card",
        "question": question,
        "card": {k: v for k, v in card.items() if k != "position"},
    })
    console.print("\n[dim]记录已保存到 history.json[/dim]\n")


def handle_three_card():
    """三牌阵占卜"""
    question = Prompt.ask("\n[bold]你的问题(可直接回车跳过)[/bold]", default="我的近期运势如何").strip()
    console.print("\n[bold magenta]凝神聚气,展开三牌阵...[/bold magenta]")
    sleep_pause(1.2)

    cards = te.draw_three_card_spread()
    for c in cards:
        print_card_panel(c, position=c["position"])
        sleep_pause(0.3)

    # 综合解读
    spread_text = te.interpret_spread(cards)
    console.print(Panel(spread_text, title="✦ 牌阵解读 ✦", border_style=THEME["secondary"], box=ROUNDED))

    # AI 个性化解读
    ai_text = ai.ai_interpret(question, cards)
    if ai_text:
        console.print(Panel(ai_text, title="✦ AI 占卜师私语 ✦", border_style=THEME["accent"], box=ROUNDED))

    te.save_history({
        "type": "three_card_spread",
        "question": question,
        "cards": [{k: v for k, v in c.items()} for c in cards],
    })
    console.print("\n[dim]记录已保存到 history.json[/dim]\n")


def handle_view_history():
    """查看历史"""
    history = te.load_history()
    if not history:
        console.print(Panel("[dim]还没有任何占卜记录。[/dim]", title="历史记录", border_style=THEME["muted"]))
        return

    table = Table(title="占卜历史(最近 100 条)", box=ROUNDED, border_style=THEME["primary"])
    table.add_column("#", style=THEME["muted"], justify="right")
    table.add_column("时间", style=THEME["secondary"])
    table.add_column("类型", style=THEME["accent"])
    table.add_column("摘要")
    for i, rec in enumerate(reversed(history[-20:]), 1):
        rtype = rec.get("type", "—")
        ts = rec.get("timestamp", "—")
        if rtype == "daily_fortune":
            summary = f"{rec['sign']} 综合 {rec['fortune']['overall_score']}"
        elif rtype == "single_card":
            card = rec["card"]
            summary = f"{card['name_cn']}({'逆' if card.get('is_reversed') else '正'})"
        elif rtype == "three_card_spread":
            names = " → ".join(c["name_cn"] for c in rec["cards"])
            summary = names
        else:
            summary = "—"
        table.add_row(str(i), ts, rtype, summary)
    console.print(table)


def handle_clear_history():
    """清空历史"""
    confirm = Prompt.ask("[red]确定清空全部历史记录?[/red]", choices=["y", "n"], default="n")
    if confirm == "y":
        te.clear_history()
        console.print("[green]历史已清空。[/green]")
    else:
        console.print("[dim]已取消。[/dim]")


def main():
    """主循环"""
    print_banner()
    while True:
        menu()
        choice = Prompt.ask("\n[bold]选择[/bold]", choices=["0", "1", "2", "3", "4", "5"], default="1")
        console.print()
        if choice == "0":
            console.print(Align.center(Text("愿星光照亮你的来路。再见。", style=THEME["primary"])))
            break
        elif choice == "1":
            handle_daily_fortune()
        elif choice == "2":
            handle_single_card()
        elif choice == "3":
            handle_three_card()
        elif choice == "4":
            handle_view_history()
        elif choice == "5":
            handle_clear_history()
        console.print("[dim]" + "─" * 60 + "[/dim]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[dim]已退出。[/dim]")
        sys.exit(0)
