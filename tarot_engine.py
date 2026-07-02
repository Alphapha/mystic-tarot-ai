"""
塔罗占卜引擎模块
负责洗牌、抽牌、牌阵解析、占卜历史记录管理
支持的单牌占卜与三牌阵(过去-现在-未来)
"""

import json
import os
import random
from datetime import datetime

from tarot_data import ALL_CARDS, CARDS_BY_ID


HISTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "history.json")


def shuffle_and_draw(count=1, allow_reversed=True, seed=None):
    """
    洗牌并抽取指定数量的牌
    :param count: 抽牌数量
    :param allow_reversed: 是否允许逆位
    :param seed: 随机种子(传入相同种子可复现结果)
    :return: 抽到的牌字典列表,每个字典附带 is_reversed 字段
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    drawn = rng.sample(ALL_CARDS, k=min(count, len(ALL_CARDS)))
    result = []
    for card in drawn:
        c = dict(card)
        c["is_reversed"] = allow_reversed and rng.random() < 0.5
        result.append(c)
    return result


def draw_single(seed=None):
    """抽取单张牌用于「每日一牌」或快速占卜"""
    return shuffle_and_draw(count=1, seed=seed)[0]


def draw_three_card_spread(seed=None):
    """
    抽取三牌阵:过去 - 现在 - 未来
    :return: 长度 3 的列表,并附带 position 字段
    """
    cards = shuffle_and_draw(count=3, seed=seed)
    positions = ["过去", "现在", "未来"]
    for card, pos in zip(cards, positions):
        card["position"] = pos
    return cards


def interpret_card(card):
    """
    根据正逆位返回该牌的关键字与含义
    :param card: 牌字典,需包含 is_reversed 字段
    """
    if card.get("is_reversed"):
        return {
            "orientation": "逆位",
            "keywords": card["keywords_reversed"],
            "meaning": card["meaning_reversed"],
        }
    return {
        "orientation": "正位",
        "keywords": card["keywords_upright"],
        "meaning": card["meaning_upright"],
    }


def interpret_spread(cards):
    """对三牌阵进行综合解读,返回拼接的解读文本"""
    parts = []
    for c in cards:
        interp = interpret_card(c)
        parts.append(
            f"【{c['position']}】{c['name_cn']}({interp['orientation']})\n"
            f"  关键字:{interp['keywords']}\n"
            f"  含义:{interp['meaning']}"
        )
    summary = "过去塑造了你现在的处境,当下的选择将决定未来的走向。三张牌连成一条时间线,提醒你以觉察之心回应每个时刻。"
    return "\n".join(parts) + "\n\n【综合】" + summary


def save_history(record):
    """将一次占卜记录追加到本地 history.json"""
    history = load_history()
    record["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(record)
    # 仅保留最近 100 条,避免无限增长
    history = history[-100:]
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    return record


def load_history():
    """读取本地历史占卜记录,文件不存在时返回空列表"""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def clear_history():
    """清空历史记录文件"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False)
    return True


def get_card_by_id(card_id):
    """通过牌 ID 获取牌信息"""
    return CARDS_BY_ID.get(card_id)
