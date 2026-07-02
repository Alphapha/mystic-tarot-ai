"""
AI 解读模块
可选功能:接入 OpenAI 大模型为塔罗占卜结果生成更具个性化的解读
所有敏感信息(API Key)从 .env 读取,绝不硬编码
未配置 API Key 时自动降级为本地解读,保证 Demo 始终可用
"""

import os
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
    _HAS_DOTENV = True
except ImportError:
    _HAS_DOTENV = False


def _get_env(key, default=None):
    """从环境变量读取配置(若 python-dotenv 可用则自动加载 .env)"""
    return os.environ.get(key, default)


# 是否启用 AI 解读
AI_ENABLED = _get_env("AI_ENABLED", "false").lower() in ("1", "true", "yes", "on")
OPENAI_API_KEY = _get_env("OPENAI_API_KEY", "")
OPENAI_BASE_URL = _get_env("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = _get_env("OPENAI_MODEL", "gpt-4o-mini")


def is_ai_available() -> bool:
    """判断 AI 解读是否真正可用(开关打开 且 API Key 已配置)"""
    return AI_ENABLED and bool(OPENAI_API_KEY)


def build_prompt(question: Optional[str], cards: list) -> str:
    """
    根据用户提问与抽到的牌构造给大模型的提示词
    :param question: 用户的占卜问题(可为空)
    :param cards: 抽到的牌列表(来自 tarot_engine)
    """
    question_part = f"用户的问题:{question}" if question else "用户没有具体问题,请做一次通用运势占卜。"
    cards_desc = []
    for c in cards:
        orientation = "逆位" if c.get("is_reversed") else "正位"
        position = c.get("position", "—")
        cards_desc.append(
            f"- 位置:{position} | 牌:{c['name_cn']}({c['name_en']}) | 朝向:{orientation} | "
            f"关键字:{c['keywords_reversed'] if c.get('is_reversed') else c['keywords_upright']}"
        )
    cards_text = "\n".join(cards_desc)

    prompt = (
        "你是一位温柔而富有洞察力的塔罗占卜师,请基于以下抽牌结果,为用户写一段 200 字以内的解读。"
        "语气神秘但有温度,结尾给出一句可操作的行动建议。\n\n"
        f"{question_part}\n\n抽到的牌:\n{cards_text}\n\n请用中文输出解读:"
    )
    return prompt


def ai_interpret(question: Optional[str], cards: list) -> str:
    """
    调用 OpenAI 接口生成个性化解读
    若未配置 Key 或调用失败,返回 None,由调用方降级到本地解读
    """
    if not is_ai_available():
        return None

    try:
        # 优先使用官方 openai SDK
        try:
            from openai import OpenAI
        except ImportError:
            return None

        client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
        prompt = build_prompt(question, cards)
        resp = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "你是一位资深的塔罗占卜师,擅长用富有诗意又接地气的语言解读牌意。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
            max_tokens=400,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        # 任何异常都不阻断主流程,降级到本地解读
        print(f"[AI 解读失败,已降级为本地解读] {e}")
        return None


def local_interpret(question: Optional[str], cards: list) -> str:
    """本地降级解读:整合各牌含义与用户问题,生成一段温和的文字"""
    from tarot_engine import interpret_card

    question_part = f"针对你的问题「{question}」," if question else ""
    parts = []
    for c in cards:
        interp = interpret_card(c)
        position = c.get("position", "")
        prefix = f"[{position}] " if position else ""
        parts.append(f"{prefix}{c['name_cn']}({interp['orientation']}):{interp['meaning']}")

    cards_text = " ".join(parts)
    closing = "请在接下来的三天里,留意生活中与这张牌呼应的微小信号。"
    return f"{question_part}塔罗给出这样的回响——{cards_text} {closing}"
