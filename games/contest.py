import sys

sys.path.append("..")

from .fight_func import (
    生成敌人,
    获取战力,
    根据技能和基础攻击力_返回攻击值,
    数字与技能映射表,
    计算对手受到的伤害,
    根据暴击率计算暴击伤害,
)
from ucf import read_user_from_db, User, write_user_to_db
from copy import deepcopy
from random import random, randint
from time import sleep as time_sleep
from math import ceil
import os


def main():

    print(
        r"""
   _____            _______          _   
  / ____|          |__   __|        | |  
 | |      ___   _ __  | |  ___  ___ | |_ 
 | |     / _ \ | '_ \ | | / _ \/ __|| __|
 | |____| (_) || | | || ||  __/\__ \| |_ 
  \_____|\___/ |_| |_||_| \___||___/ \__|
        
______________________________________________                                 
    """
    )
    print("正在生成对手")

    enemyobj: User = 生成敌人(read_user_from_db())

    for i in range(12):
        print(str(i) + "/12", end="\r")
        time_sleep(random() / randint(1, 10))

    print("对手生成完毕")

    对手战力 = 获取战力(enemyobj)

    print("对手的战力是： ", 对手战力)
    input("请按回车键开始战斗")
    os.system("cls" if os.name == "nt" else "clear")
    战斗主循环(enemyobj)
    input("[按回车键退出]")


def 战斗主循环(enemyobj: User):
    对手的 = deepcopy(enemyobj)
    用户的: User = deepcopy(read_user_from_db())

    is_player_turn = randint(0, 1) == 0  # 0为玩家先手，1为敌人先手

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        if is_player_turn:
            print(
                f"""
                      你的血量:{ceil(用户的.hp)}
                      敌人的血量:{ceil(对手的.hp)}
                __________________________
                |    请选择你的技能:      |
                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                __________________________
                |    1. 水系技能          | 
                |    2. 火系技能          |
                |    3. 木系技能          |
                |    4. 体术技能          |
                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                  """
            )
            skill_num = input(">>> ")
            skill_name = 数字与技能映射表.get(str(skill_num), "无效技能")
            if skill_name == "无效技能":
                input("没有这个选项")
                continue
            print(f"\n你使用了{skill_name}技能")
            attack_value = 根据技能和基础攻击力_返回攻击值(skill_name, 用户的)
            伤害 = 根据暴击率计算暴击伤害(
                计算对手受到的伤害(attack_value, 对手的.defense),
                用户的.crit_rate,
            )
            input(f"攻击了{对手的.name}，造成了{round(伤害, 2)}点伤害")
            对手的.hp -= 伤害

            if 对手的.hp <= 0:
                userobj = read_user_from_db()
                userobj.battle_points += 获取战力(enemyobj)
                write_user_to_db(userobj)
                # 赢了!!!
                print(
                    f"""
 __          __  _____   _   _   _   _   _ 
 \ \        / / |_   _| | \ | | | | | | | |
  \ \  /\  / /    | |   |  \| | | | | | | |
   \ \/  \/ /     | |   | . ` | | | | | | |
    \  /\  /     _| |_  | |\  | |_| |_| |_|
     \/  \/     |_____| |_| \_| (_) (_) (_)


            {对手的.name}被你击败了！

"""
                )

                break


            is_player_turn = not is_player_turn  # 切换攻击方
        else:
            print("敌人回合\n\n")
            skill_num = randint(1, 4)
            skill_name = 数字与技能映射表.get(str(skill_num), "无效技能")
            if skill_name == "无效技能":
                input("没有这个选项")
                continue
            print(f"\n{对手的.name}使用了{skill_name}技能")
            attack_value = 根据技能和基础攻击力_返回攻击值(skill_name, 对手的)

            伤害 = 根据暴击率计算暴击伤害(
                计算对手受到的伤害(attack_value, 用户的.defense),
                对手的.crit_rate,
            )

            input(f"{对手的.name}攻击了你，造成了{round(伤害, 2)}点伤害")
            用户的.hp -= 伤害

            if 用户的.hp <= 0:
                # 输了!!!
                input(
                    f"""
  ______        _____  _       ______  _____  
 |  ____| /\    |_   _|| |     |  ____||  __ \ 
 | |__   /  \     | |  | |     | |__   | |  | |
 |  __| / /\ \    | |  | |     |  __|  | |  | |
 | |   / ____ \  _| |_ | |____ | |____ | |__| |
 |_|  /_/    \_\|_____||______||______||_____/ 

            {对手的.name}把你击败了！

"""
                )
                userobj = read_user_from_db()
                userobj.battle_points -= 获取战力(enemyobj)
                write_user_to_db(userobj)
                break

            is_player_turn = not is_player_turn  # 切换攻击方

    del 对手的
    del 用户的


if __name__ == "__main__":
    main()
