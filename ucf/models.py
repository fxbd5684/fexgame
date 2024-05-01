import sys

sys.path.append("..")

from fexdb import Fexdb
from dataclasses import dataclass


@dataclass
class User:
    """
    这是用户模型
    name在数据库中是主键

    有以下属性：
    名字
    密码
    金币
    经验值
    生命值
    攻击力
    防御率
    暴击率
    技能{火系：攻击力，水系：攻击力，木系：攻击力，体术：攻击力}
    装备[装备名称，...]
    战斗积分
    """

    name: str
    password: str
    gold: int
    exp: int
    hp: int
    attack: int
    defense: float
    crit_rate: float
    skills: dict
    equipments: list
    battle_points: int


default_user = User(
    name="default",
    password="password",
    gold=10,
    exp=0,
    hp=20,
    attack=10,
    defense=1.0,
    crit_rate=0.01,
    skills={"fire": 10, "water": 10, "wood": 10, "body": 10},
    equipments=[],
    battle_points=0,
)

if __name__ == "__main__":
    db = Fexdb("ucf.fexdb")

    user_a = default_user
    user_a.name = "user_a"
    db.add(user_a.name, user_a)
    print(db.get("user_a").password)
