"""
这是战斗函数库
"""

import sys

sys.path.append(".")
from ucf.models import User, default_user
from ucf import read_user_from_db
import random
from math import floor as math_floor
import os
from math import log as math_log

数字与技能映射表 = {
    "1": "water",
    "2": "fire",
    "3": "wood",
    "4": "body",
}


def 获取战力(enemyobj: User):
    return math_floor(
        (
            enemyobj.attack
            + enemyobj.skills["water"]
            + enemyobj.skills["fire"]
            + enemyobj.skills["wood"]
            + enemyobj.skills["body"]
            + enemyobj.defense
            + enemyobj.hp
        )
        ** (1 / 2)
    )


def 根据值上下浮动(value: int, scope: int, more_than_0: bool = True):
    """
    上下浮动
    """
    if more_than_0:
        returns_value = random.randint(round(value - scope), round(value + scope))
        return returns_value if returns_value > 0 else 1
    return random.randint(round(value - scope), round(value + scope))


def 根据百分比上下浮动(value: int, percent: int, max_alpha=2, more_than_0: bool = True):
    """
    上下浮动百分比
    """
    scpoe = int(value * percent / 100)
    if more_than_0:
        returns_value = random.randint(
            round(value - scpoe), round(value + scpoe // max_alpha)
        )
        return returns_value if returns_value > 0 else 1
    return 根据值上下浮动(round(value - scpoe), round(value + scpoe))


def 根据上下限上下浮动(value, max_, min_, more_than_0: bool = True):
    """
    上下限浮动

    """
    if more_than_0:
        returns_value = random.randint(round(value - min_), round(value + max_))
        return returns_value if returns_value > 0 else 1
    return random.randint(value - min_, value + max_)


def 根据上下百分比上下浮动(
    value: int, prc_min: int, prc_max: int, more_than_0: bool = True
):
    """
    上下百分比浮动
    """
    scope_max = int(value * prc_max / 100)
    scope_min = int(value * prc_min / 100)
    if more_than_0:
        returns_value = random.randint(
            round(value - scope_min), round(value + scope_max)
        )
        return returns_value if returns_value > 0 else 1
    return random.randint(round(value - scope_min), round(value + scope_max))


def 生成敌人(userobj: User, names_list: list = ["fexAI陪练"]):
    """
    生成敌人
    """
    fb = lambda x: 根据上下百分比上下浮动(x, 25, 12)

    enemy_obj = default_user

    enemy_obj.name = random.choice(names_list)
    enemy_obj.hp = fb(userobj.hp)
    enemy_obj.attack = fb(userobj.attack)
    enemy_obj.defense = fb(userobj.defense)
    enemy_obj.crit_rate = userobj.crit_rate
    enemy_obj.skills = {
        "fire": fb(userobj.skills["fire"]),
        "water": fb(userobj.skills["water"]),
        "wood": fb(userobj.skills["wood"]),
        "body": fb(userobj.skills["body"]),
    }
    return enemy_obj


def 根据技能和基础攻击力_返回攻击值(
    技能名: str,
    模型: User,
) -> int:
    user_obj = read_user_from_db()
    skill_dict: dict = user_obj.skills

    skill_attack = skill_dict[技能名]
    return skill_attack * 模型.attack


def 计算对手受到的伤害(
    伤害值: float,  # 伤害值
    对方防御值: int,  # 对手防御值
    alpha: float = 0.06,  # 伤害缩放系数
) -> float:
    """
    计算对手受到的伤害
    """
    无法防御比 = 1 - (对方防御值 / 100)  # 无法防御的比例
    最终伤害 = 伤害值 * alpha * 无法防御比
    return 最终伤害


def 根据暴击率计算暴击伤害(
    基础伤害: int,  # 基础伤害
    暴击率: float,  # 暴击率
    alpha: float = 1.5,  # 暴击伤害是原伤害的百分比
) -> float:
    """
    根据暴击率计算暴击伤害
    """
    暴击值 = round(暴击率 * 100)

    k = random.randint(1, 100)
    if k <= int(暴击值):
        print("暴击！")
        return float(基础伤害 * alpha)

    return float(基础伤害)


if __name__ == "__main__":
    # 计算对手受到的伤害(100, 50)
    # while 1:
    #     print(根据暴击率计算暴击伤害(100, 0.01))
    print(根据上下百分比上下浮动(100, 20, 10))
