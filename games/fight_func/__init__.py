"""
这是战斗函数库
"""

import sys

sys.path.append("../..")
from ucf.models import User, default_user
import random


def up_and_down_by_value(value: int, scope: int, more_than_0: bool = True):
    """
    上下浮动
    """
    if more_than_0:
        returns_value = random.randint(value - scope, value + scope)
        return returns_value if returns_value > 0 else 1
    return random.randint(value - scope, value + scope)


def up_and_down_by_percent(value: int, percent: int, more_than_0: bool = True):
    """
    上下浮动百分比
    """
    scpoe = int(value * percent / 100)
    if more_than_0:
        returns_value = random.randint(value - scpoe, value + scpoe)
        return returns_value if returns_value > 0 else 1
    return up_and_down_by_value(value - scpoe, value + scpoe)


def generate_enemy(userobj: User, names_list: list = ["fexAI陪练"]):
    """
    生成敌人
    """
    enemy_obj = default_user

    enemy_obj.name = random.choice(names_list)
    enemy_obj.hp = up_and_down_by_percent(userobj.hp, 10)
    enemy_obj.attack = up_and_down_by_percent(userobj.attack, 10)
    enemy_obj.defense = up_and_down_by_percent(userobj.defense, 10)
    enemy_obj.skills = {
        "fire": up_and_down_by_percent(userobj.skills["fire"], 10),
        "water": up_and_down_by_percent(userobj.skills["water"], 10),
        "wood": up_and_down_by_percent(userobj.skills["wood"], 10),
        "body": up_and_down_by_percent(userobj.skills["body"], 10),
    }
    return enemy_obj


if __name__ == "__main__":
    print(generate_enemy(default_user))
