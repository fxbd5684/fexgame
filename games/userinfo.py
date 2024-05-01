import sys

sys.path.append("..")
import ucf
from math import log as math_log
from math import floor as math_floor


def main():
    info = ucf.read_user_from_db()

    level = math_log(int(info.exp + 1), 1.2)
    combat_power = math_floor(
        (
            info.attack
            + info.skills["water"]
            + info.skills["fire"]
            + info.skills["wood"]
            + info.skills["body"]
            + info.defense
            + info.hp
        )
        ** (1 / 2)
    )

    user_info_str = rf"""
  _    _                 _____          __       
 | |  | |               |_   _|        / _|      
 | |  | | ___   ___  _ __ | |   _ __  | |_  ___  
 | |  | |/ __| / _ \| '__|| |  | '_ \ |  _|/ _ \ 
 | |__| |\__ \|  __/| |  _| |_ | | | || | | (_) |
  \____/ |___/ \___||_| |_____||_| |_||_|  \___/ 
  
___________________________________________________    

    你好 {info.name} !
    欢迎来到 FexGame !

    你现在有 {info.gold} 枚金币
    你的有 {info.exp} 点经验值
    你现在是 {math_floor(level)} 级
    你的战斗力为 {combat_power}
    你的战斗积分有 {info.battle_points} 分

    你的各项属性如下：
        生命值：{info.hp}
        攻击力：{info.attack}
        防御力：{info.defense}
        暴击率：{info.crit_rate*100}%
    
    技能攻击力如下：
        水系技能： {info.skills['water']}
        火系技能： {info.skills['fire']}
        木系技能： {info.skills['wood']}
        体术技能： {info.skills['body']}
    

[按下回车回到主菜单] """

    input(user_info_str)


if __name__ == "__main__":
    main()
