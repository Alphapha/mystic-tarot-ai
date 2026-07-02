"""
塔罗牌数据库模块
包含完整的 78 张塔罗牌信息(22 张大阿尔卡那 + 56 张小阿尔卡那)
每张牌包含:中英文名、正逆位关键字、正逆位含义、元素/星座对应
"""


# 大阿尔卡那 22 张(0-21)
MAJOR_ARCANA = [
    {
        "id": 0, "name_cn": "愚者", "name_en": "The Fool", "arcana": "major", "suit": "major",
        "element": "风", "astrology": "天王星",
        "keywords_upright": "新开始 天真 冒险 自由",
        "keywords_reversed": "鲁莽 轻率 风险 无谋",
        "meaning_upright": "你正站在新旅程的起点,带着孩童般的好奇与勇气跃入未知。宇宙在保护这个天真的灵魂,请相信直觉。",
        "meaning_reversed": "冲动行事可能带来隐患,先停下来想想再做决定。冒险精神值得赞许,但盲目的跳跃会让你摔得很重。",
    },
    {
        "id": 1, "name_cn": "魔术师", "name_en": "The Magician", "arcana": "major", "suit": "major",
        "element": "水星", "astrology": "双子座/处女座",
        "keywords_upright": "显化 创造力 技能 专注",
        "keywords_reversed": "操纵 欺骗 未发挥 滥用",
        "meaning_upright": "你拥有把想法变成现实的所有工具——风火水土俱备。明确意图,专注行动,奇迹即将被你创造。",
        "meaning_reversed": "天赋被搁置或被用于不当目的。警惕花言巧语者,也反省自己是否在自欺欺人。",
    },
    {
        "id": 2, "name_cn": "女祭司", "name_en": "The High Priestess", "arcana": "major", "suit": "major",
        "element": "月亮", "astrology": "巨蟹座",
        "keywords_upright": "直觉 神秘 潜意识 内省",
        "keywords_reversed": "秘密 压抑 失联 表面化",
        "meaning_upright": "答案藏在静默之中。倾听内心那道轻柔的声音,梦境与直觉正在向你传递重要信息。",
        "meaning_reversed": "你忽略了内在的智慧,或被外界的喧嚣淹没。是时候关掉噪音,重新与自己对话。",
    },
    {
        "id": 3, "name_cn": "皇后", "name_en": "The Empress", "arcana": "major", "suit": "major",
        "element": "金星", "astrology": "金牛座/天秤座",
        "keywords_upright": "丰饶 母性 创造 滋养",
        "keywords_reversed": "依赖 窒息 创造阻塞 忽视自我",
        "meaning_upright": "丰盛正在涌入你的生命。无论是创意、感情还是物质,都将迎来蓬勃生长。拥抱大地之母的恩赐。",
        "meaning_reversed": "过度付出让你枯竭,或被他人过度依赖所窒息。先照顾好自己,才能持续给予。",
    },
    {
        "id": 4, "name_cn": "皇帝", "name_en": "The Emperor", "arcana": "major", "suit": "major",
        "element": "火", "astrology": "白羊座",
        "keywords_upright": "权威 结构 控制 领导",
        "keywords_reversed": "专制 僵化 滥权 失控",
        "meaning_upright": "你正处于建立秩序与掌控全局的位置。用清晰的规则和坚定的意志,把愿景落地为现实。",
        "meaning_reversed": "过于强硬或彻底失控。在权威与柔韧之间找到平衡,别让控制欲摧毁关系。",
    },
    {
        "id": 5, "name_cn": "教皇", "name_en": "The Hierophant", "arcana": "major", "suit": "major",
        "element": "土", "astrology": "金牛座",
        "keywords_upright": "传统 信仰 指导 仪式",
        "keywords_reversed": "反叛 教条 挑战体制 自由探索",
        "meaning_upright": "向你尊敬的导师或传统智慧寻求指引。仪式感能为生活带来意义与方向。",
        "meaning_reversed": "是时候走出既定框架,走自己的路。质疑权威,寻找属于你的真理。",
    },
    {
        "id": 6, "name_cn": "恋人", "name_en": "The Lovers", "arcana": "major", "suit": "major",
        "element": "风", "astrology": "双子座",
        "keywords_upright": "爱 选择 和谐 价值观契合",
        "keywords_reversed": "失衡 分裂 错误选择 关系危机",
        "meaning_upright": "一段基于心灵契合的关系正在绽放,或你正面临一个关乎价值观的重要选择。听从真心。",
        "meaning_reversed": "关系出现裂痕,或选择偏离了你的本心。重新审视价值观是否对齐。",
    },
    {
        "id": 7, "name_cn": "战车", "name_en": "The Chariot", "arcana": "major", "suit": "major",
        "element": "水", "astrology": "巨蟹座",
        "keywords_upright": "胜利 意志 前进 克服",
        "keywords_reversed": "失控 方向迷失 冲突 滞留",
        "meaning_upright": "凭借坚定意志驾驭相反的力量,你将赢得这场战役。专注目标,全速前进。",
        "meaning_reversed": "力量失控或失去方向。先稳住内在,再谈前进,否则只会原地打转。",
    },
    {
        "id": 8, "name_cn": "力量", "name_en": "Strength", "arcana": "major", "suit": "major",
        "element": "火", "astrology": "狮子座",
        "keywords_upright": "勇气 柔韧 内在力量 驯服",
        "keywords_reversed": "自我怀疑 脆弱 暴怒 失去信心",
        "meaning_upright": "真正的力量来自温柔与坚持。用爱与耐心驯服内心的猛兽,你比想象中更强大。",
        "meaning_reversed": "自我怀疑在侵蚀你,或情绪失控。重新连接内在的勇气,别让恐惧做主。",
    },
    {
        "id": 9, "name_cn": "隐士", "name_en": "The Hermit", "arcana": "major", "suit": "major",
        "element": "土", "astrology": "处女座",
        "keywords_upright": "独处 内省 智慧 寻找",
        "keywords_reversed": "孤立 退缩 拒绝指引 迷失",
        "meaning_upright": "暂时远离喧嚣,独处会带来答案。你提着内在的灯,照亮前行的路。",
        "meaning_reversed": "孤立变成逃避,或你拒绝他人的帮助。独处是滋养,不是隔绝。",
    },
    {
        "id": 10, "name_cn": "命运之轮", "name_en": "Wheel of Fortune", "arcana": "major", "suit": "major",
        "element": "火", "astrology": "木星",
        "keywords_upright": "转机 循环 幸运 命运",
        "keywords_reversed": "逆运 延迟 失控 阻滞",
        "meaning_upright": "命运的齿轮正在转动,转机降临。顺势而为,幸运正在向你靠近。",
        "meaning_reversed": "运势处于低谷,或事情不如预期推进。这是暂时的,保持耐心等风来。",
    },
    {
        "id": 11, "name_cn": "正义", "name_en": "Justice", "arcana": "major", "suit": "major",
        "element": "风", "astrology": "天秤座",
        "keywords_upright": "公正 真相 因果 平衡",
        "keywords_reversed": "不公 偏见 逃避责任 失衡",
        "meaning_upright": "真相将水落石出,付出与回报终将平衡。做出公正的决定,承担属于你的责任。",
        "meaning_reversed": "某种不公正在发生,或你逃避了应承担的后果。诚实面对,才能恢复平衡。",
    },
    {
        "id": 12, "name_cn": "倒吊人", "name_en": "The Hanged Man", "arcana": "major", "suit": "major",
        "element": "水", "astrology": "海王星",
        "keywords_upright": "暂停 牺牲 视角 悬置",
        "keywords_reversed": "停滞 抗拒 踌躇 无谓牺牲",
        "meaning_upright": "换个角度看世界,暂停本身就是一种进展。短暂的牺牲将换来更大的觉醒。",
        "meaning_reversed": "无谓的拖延或抗拒改变。是时候做出决断,而非继续悬在原地。",
    },
    {
        "id": 13, "name_cn": "死神", "name_en": "Death", "arcana": "major", "suit": "major",
        "element": "水", "astrology": "天蝎座",
        "keywords_upright": "结束 转变 重生 释放",
        "keywords_reversed": "抗拒结束 停滞 害怕改变 拖延",
        "meaning_upright": "旧的篇章正在合上,为新生的腾出空间。别害怕结束——它正是重生的开端。",
        "meaning_reversed": "你抗拒着必然的结束,因此被困在原地。放手,才能迎来新生。",
    },
    {
        "id": 14, "name_cn": "节制", "name_en": "Temperance", "arcana": "major", "suit": "major",
        "element": "火", "astrology": "射手座",
        "keywords_upright": "平衡 调和 耐心 整合",
        "keywords_reversed": "失衡 极端 急躁 不调和",
        "meaning_upright": "在不同元素间找到中道,耐心地调和与整合。一切都在恰到好处的节奏中展开。",
        "meaning_reversed": "处于极端或失衡状态。慢下来,重新校准生活节奏。",
    },
    {
        "id": 15, "name_cn": "恶魔", "name_en": "The Devil", "arcana": "major", "suit": "major",
        "element": "土", "astrology": "摩羯座",
        "keywords_upright": "束缚 欲望 执念 物质",
        "keywords_reversed": "解放 觉醒 戒除 摆脱",
        "meaning_upright": "你被某种欲望或执念束缚,但锁链其实并未上锁。看清真相,选择松手。",
        "meaning_reversed": "你正在挣脱枷锁,重获自由。继续前行,别再回头。",
    },
    {
        "id": 16, "name_cn": "塔", "name_en": "The Tower", "arcana": "major", "suit": "major",
        "element": "火", "astrology": "火星",
        "keywords_upright": "突变 崩塌 觉醒 真相暴露",
        "keywords_reversed": "避免灾难 渐变 抗拒觉醒 延迟",
        "meaning_upright": "虚假的结构正在崩塌,虽然剧烈,但这是必要的觉醒。废墟之上才能重建真实。",
        "meaning_reversed": "你预感到危机却试图回避。修补裂痕或主动变革,胜过等待崩塌。",
    },
    {
        "id": 17, "name_cn": "星星", "name_en": "The Star", "arcana": "major", "suit": "major",
        "element": "风", "astrology": "水瓶座",
        "keywords_upright": "希望 灵感 信念 治愈",
        "keywords_reversed": "绝望 失去信心 悲观 断联",
        "meaning_upright": "风暴过后,星光重新照亮夜空。希望已回归,允许自己被治愈与启发。",
        "meaning_reversed": "暂时失去信心或方向。抬头看看星空,光一直都在,只是被云遮住了。",
    },
    {
        "id": 18, "name_cn": "月亮", "name_en": "The Moon", "arcana": "major", "suit": "major",
        "element": "水", "astrology": "双鱼座",
        "keywords_upright": "幻象 直觉 潜意识 不确定",
        "keywords_reversed": "澄清 释放恐惧 真相显现 走出迷雾",
        "meaning_upright": "前方道路朦胧,幻象与真相交织。倾听直觉,谨慎前行,别被恐惧支配。",
        "meaning_reversed": "迷雾正在散去,真相逐渐清晰。你正在走出困惑,迎来澄明。",
    },
    {
        "id": 19, "name_cn": "太阳", "name_en": "The Sun", "arcana": "major", "suit": "major",
        "element": "火", "astrology": "太阳",
        "keywords_upright": "喜悦 成功 活力 真实",
        "keywords_reversed": "暂时阴霾 延迟喜悦 失去热情 浮夸",
        "meaning_upright": "灿烂的阳光照耀着你,喜悦、成功与活力正在到来。展现真实的自己,世界会回应你以温暖。",
        "meaning_reversed": "短暂的乌云遮住阳光,或你忽略了应有的喜悦。调整心态,光就在云后。",
    },
    {
        "id": 20, "name_cn": "审判", "name_en": "Judgement", "arcana": "major", "suit": "major",
        "element": "火", "astrology": "冥王星",
        "keywords_upright": "觉醒 召唤 重生 反思",
        "keywords_reversed": "自我怀疑 错过召唤 严苛 苛责",
        "meaning_upright": "你听到内心的召唤,是时候做出决定性的觉醒与转变。原谅过去,迎接新生。",
        "meaning_reversed": "你忽略了内在的召唤,或对自己过于严苛。放下评判,聆听真实的声音。",
    },
    {
        "id": 21, "name_cn": "世界", "name_en": "The World", "arcana": "major", "suit": "major",
        "element": "土", "astrology": "土星",
        "keywords_upright": "完成 圆满 成就 整合",
        "keywords_reversed": "未完成 拖延 缺失最后一步 临门一脚",
        "meaning_upright": "一个重要的循环正走向圆满。庆祝你的成就,新的世界即将向你展开。",
        "meaning_reversed": "差最后一步就能完成。别在终点前停下,坚持到底。",
    },
]


# 小阿尔卡那四组通用关键字(数字/宫廷牌通用含义)
# Ace: 起源 / 2:抉择 / 3:合作 / 4:稳定 / 5:冲突 / 6:和谐 / 7:反思 / 8:行动 / 9:尾声 / 10:完成
# Page:学习 / Knight:行动 / Queen:内化 / King:掌控

def _minor(suit, suit_cn, element, theme):
    """生成一组小阿尔卡那 14 张牌的通用数据"""
    numbers = [
        ("Ace", "王牌", f"新的{theme}契机,种子萌芽,潜能觉醒", f"{theme}潜能被搁置或滥用,延迟显现"),
        ("2", "二号", f"{theme}中的抉择与平衡,需要做出决定", f"{theme}中摇摆不定,难以抉择"),
        ("3", "三号", f"{theme}中的合作与扩展,初步成果显现", f"{theme}协作受阻,扩展停滞"),
        ("4", "四号", f"{theme}中的稳定与巩固,暂时的栖息", f"{theme}稳定被打破,或过度僵化"),
        ("5", "五号", f"{theme}中的冲突与挑战,需要调整", f"{theme}冲突化解,走出困境"),
        ("6", "六号", f"{theme}中的和谐与给予,助人 or 受助", f"{theme}中失衡,付出与回报不对等"),
        ("7", "七号", f"{theme}中的反思与策略,审视前路", f"{theme}中迷茫,缺乏方向感"),
        ("8", "八号", f"{theme}中的行动与推进,持续努力", f"{theme}中动力不足,停滞不前"),
        ("9", "九号", f"{theme}接近圆满,积淀深厚", f"{theme}中执念过深,需要放手"),
        ("10", "十号", f"{theme}的完成与转化,承担或传承", f"{theme}中负担过重,需要卸下"),
        ("Page", "侍从", f"{theme}中的新消息与学习,好奇心", f"{theme}中浮躁,缺乏深入学习"),
        ("Knight", "骑士", f"{theme}中的行动与追求,冒险前进", f"{theme}中冲动,行动脱离实际"),
        ("Queen", "王后", f"{theme}中的滋养与内化,温柔掌控", f"{theme}中过度情绪化,失去平衡"),
        ("King", "国王", f"{theme}中的成熟与掌控,权威体现", f"{theme}中独断,滥用权威"),
    ]
    cards = []
    for i, (rank_en, rank_cn, up, rev) in enumerate(numbers):
        cards.append({
            "id": 22 + i if suit == "wands" else 36 + i if suit == "cups" else 50 + i if suit == "swords" else 64 + i,
            "name_cn": f"{suit_cn}{rank_cn}",
            "name_en": f"{rank_en} of {suit.capitalize()}",
            "arcana": "minor",
            "suit": suit,
            "element": element,
            "astrology": "—",
            "keywords_upright": up.split(",")[0].strip() if "," in up else up,
            "keywords_reversed": rev.split(",")[0].strip() if "," in rev else rev,
            "meaning_upright": up,
            "meaning_reversed": rev,
        })
    return cards


MINOR_ARCANA = (
    _minor("wands", "权杖", "火", "热情与行动")
    + _minor("cups", "圣杯", "水", "情感与关系")
    + _minor("swords", "宝剑", "风", "思想与挑战")
    + _minor("pentacles", "钱币", "土", "物质与现实")
)


# 完整 78 张牌
ALL_CARDS = MAJOR_ARCANA + MINOR_ARCANA


# 按 ID 索引,便于抽取
CARDS_BY_ID = {c["id"]: c for c in ALL_CARDS}
