"""
这是战斗函数库
"""

import sys

sys.path.append("../..")
from ucf.models import User, default_user
from ucf import read_user_from_db
import random
from math import floor as math_floor
import os

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


def 根据百分比上下浮动(value: int, percent: int, more_than_0: bool = True):
    """
    上下浮动百分比
    """
    scpoe = int(value * percent / 100)
    if more_than_0:
        returns_value = random.randint(round(value - scpoe), round(value + scpoe))
        return returns_value if returns_value > 0 else 1
    return 根据值上下浮动(round(value - scpoe), round(value + scpoe))


def 生成敌人(userobj: User, names_list: list = ["fexAI陪练"]):
    """
    生成敌人
    """
    enemy_obj = default_user

    enemy_obj.name = random.choice(names_list)
    enemy_obj.hp = 根据百分比上下浮动(userobj.hp, 10)
    enemy_obj.attack = 根据百分比上下浮动(userobj.attack, 10)
    enemy_obj.defense = 根据百分比上下浮动(userobj.defense, 10)
    enemy_obj.skills = {
        "fire": 根据百分比上下浮动(userobj.skills["fire"], 10),
        "water": 根据百分比上下浮动(userobj.skills["water"], 10),
        "wood": 根据百分比上下浮动(userobj.skills["wood"], 10),
        "body": 根据百分比上下浮动(userobj.skills["body"], 10),
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
    alpha: float = 0.1,  # 伤害缩放系数
) -> float:
    """
    计算对手受到的伤害
    """
    无法防御比 = 1 - (对方防御值 / 100)  # 无法防御的比例
    最终伤害 = 伤害值 * alpha * 无法防御比
    return 最终伤害


if __name__ == "__main__":
    # 计算对手受到的伤害(100, 50)
    pass
