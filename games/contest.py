import sys

sys.path.append("..")

from .fight_func import generate_enemy
from ucf import read_user_from_db,User
from math import floor as math_floor


def get_combat_power_by_obj(enemyobj:User):
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


def main():

    input(
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
    enemyobj:User = generate_enemy(read_user_from_db())
    print("对手生成完毕")

    combat_power = get_combat_power_by_obj(enemyobj)

    print("对手的战力是： ", combat_power)
    input("请按回车键开始战斗")
    fight_main(enemyobj)
    input("[按回车键退出]")


def fight_main(enemyobj:User):
    while True:
        pass

if __name__ == "__main__":
    main()
