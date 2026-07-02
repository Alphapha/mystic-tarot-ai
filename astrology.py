"""
星座运势模块
提供 12 星座的基础信息、每日运势生成、幸运色 / 幸运数字 / 幸运方位等娱乐性占卜数据
注:本模块所有内容均为娱乐向随机生成,不代表真实天文学或占星学结论
"""

import hashlib
import random
from datetime import datetime, date


# 12 星座基础数据(日期范围以公历近似为准)
ZODIAC_SIGNS = [
    {"sign": "白羊座", "element": "火", "ruler": "火星", "date_range": "3.21-4.19", "trait": "冲动 热情 先锋"},
    {"sign": "金牛座", "element": "土", "ruler": "金星", "date_range": "4.20-5.20", "trait": "稳定 务实 享乐"},
    {"sign": "双子座", "element": "风", "ruler": "水星", "date_range": "5.21-6.21", "trait": "机敏 好奇 多变"},
    {"sign": "巨蟹座", "element": "水", "ruler": "月亮", "date_range": "6.22-7.22", "trait": "温柔 顾家 敏感"},
    {"sign": "狮子座", "element": "火", "ruler": "太阳", "date_range": "7.23-8.22", "trait": "自信 慷慨 王者"},
    {"sign": "处女座", "element": "土", "ruler": "水星", "date_range": "8.23-9.22", "trait": "细致 完美 务实"},
    {"sign": "天秤座", "element": "风", "ruler": "金星", "date_range": "9.23-10.23", "trait": "优雅 犹豫 和谐"},
    {"sign": "天蝎座", "element": "水", "ruler": "冥王星", "date_range": "10.24-11.22", "trait": "深邃 神秘 执着"},
    {"sign": "射手座", "element": "火", "ruler": "木星", "date_range": "11.23-12.21", "trait": "自由 乐观 哲思"},
    {"sign": "摩羯座", "element": "土", "ruler": "土星", "date_range": "12.22-1.19", "trait": "坚毅 务实 雄心"},
    {"sign": "水瓶座", "element": "风", "ruler": "天王星", "date_range": "1.20-2.18", "trait": "独立 创新 叛逆"},
    {"sign": "双鱼座", "element": "水", "ruler": "海王星", "date_range": "2.19-3.20", "trait": "浪漫 共情 梦幻"},
]


# 幸运色库(每个色附带情绪寓意)
LUCKY_COLORS = [
    ("赤红", "热情与行动力"),
    ("琥珀金", "财富与自信"),
    ("日光黄", "活力与明朗"),
    ("森绿", "生长与平衡"),
    ("海蓝", "宁静与沟通"),
    ("深夜紫", "神秘与灵感"),
    ("月白", "纯净与直觉"),
    ("玫瑰粉", "柔情与桃花"),
    ("曜石黑", "守护与沉稳"),
    ("雾灰", "中性与思考"),
]

# 心情 / 提示语库
MOOD_QUOTES = [
    "今日适合给自己泡一杯热茶,静坐十分钟。",
    "把搁置的小事完成一件,宇宙会回赠你惊喜。",
    "给久未联系的朋友发条消息,会有意外的回响。",
    "穿一件你最喜欢的颜色出门,运气会变好。",
    "今晚早点睡,明天的灵感会自己来找你。",
    "做一件让自己开心但不必要的事,纯粹地享受它。",
    "把心里那句话写下来,不必寄出,写下即是疗愈。",
    "今日适合整理一个角落,物理空间的清理会带来心境的清明。",
    "听一首老歌,让记忆温柔地流过你。",
    "走一条没走过的路回家,世界会因此多一种颜色。",
]

# 综合运势打分维度
DIMENSIONS = ["整体", "爱情", "事业", "财运", "健康"]


def get_zodiac_by_date(birth_date):
    """根据生日(yyyy-mm-dd 字符串或 date 对象)返回星座名"""
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    m, d = birth_date.month, birth_date.day
    # 用 月*100+日 组成一个可比较的整数,按星座分界判断
    md = m * 100 + d
    if md <= 119 or md >= 1222:
        return "摩羯座"
    elif md <= 218:
        return "水瓶座"
    elif md <= 320:
        return "双鱼座"
    elif md <= 419:
        return "白羊座"
    elif md <= 520:
        return "金牛座"
    elif md <= 621:
        return "双子座"
    elif md <= 722:
        return "巨蟹座"
    elif md <= 822:
        return "狮子座"
    elif md <= 922:
        return "处女座"
    elif md <= 1023:
        return "天秤座"
    elif md <= 1122:
        return "天蝎座"
    else:
        return "射手座"


def get_sign_info(sign_name):
    """根据星座名返回基础信息字典"""
    for s in ZODIAC_SIGNS:
        if s["sign"] == sign_name:
            return s
    return None


def _daily_seed(sign_name, target_date=None):
    """基于星座名 + 日期生成稳定的种子,保证同一天同一星座运势一致(跨进程稳定)"""
    if target_date is None:
        target_date = date.today()
    seed_str = f"{sign_name}-{target_date.isoformat()}"
    # 使用 md5 生成稳定整数,避免内置 hash 受 PYTHONHASHSEED 影响
    digest = hashlib.md5(seed_str.encode("utf-8")).hexdigest()
    return int(digest[:8], 16)


def generate_daily_fortune(sign_name, target_date=None):
    """
    生成某星座在某日的运势
    返回字典:score(1-5)、dimensions(各维度评分)、lucky_color、lucky_number、lucky_direction、mood_quote、summary
    """
    info = get_sign_info(sign_name)
    if info is None:
        raise ValueError(f"未知星座:{sign_name}")
    if target_date is None:
        target_date = date.today()

    rng = random.Random(_daily_seed(sign_name, target_date))

    # 各维度评分(1-5 星)
    dims = {dim: rng.randint(2, 5) for dim in DIMENSIONS}
    overall = round(sum(dims.values()) / len(dims), 1)

    color = rng.choice(LUCKY_COLORS)
    lucky_number = rng.randint(1, 99)
    directions = ["东", "南", "西", "北", "东南", "西南", "东北", "西北"]
    lucky_direction = rng.choice(directions)
    mood_quote = rng.choice(MOOD_QUOTES)

    # 综合运势文案
    if overall >= 4:
        summary = f"今日{sign_name}运势上扬,{dims['爱情']}星爱情、{dims['事业']}星事业。{mood_quote}"
    elif overall >= 3:
        summary = f"今日{sign_name}运势平稳,{mood_quote}"
    else:
        summary = f"今日{sign_name}需要多一点耐心,{mood_quote}"

    return {
        "sign": sign_name,
        "date": target_date.isoformat(),
        "overall_score": overall,
        "dimensions": dims,
        "lucky_color": color[0],
        "color_meaning": color[1],
        "lucky_number": lucky_number,
        "lucky_direction": lucky_direction,
        "mood_quote": mood_quote,
        "summary": summary,
        "element": info["element"],
        "ruler": info["ruler"],
    }
