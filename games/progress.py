import sys

sys.path.append("..")

import ucf
from random import randint
import os


def main():
    # 提升
    print(
        r"""
  _____               _____                      
 |  __ \             / ____|                     
 | |__) |_ __  ___  | |  __  _ __  ___  ___  ___ 
 |  ___/| '__|/ _ \ | | |_ || '__|/ _ \/ __|/ __|
 | |    | |  | (_) || |__| || |  |  __/\__ \\__ \
 |_|    |_|   \___/  \_____||_|   \___||___/|___/
                                                 
__________________________________________________   
    """
    )
    userobj = ucf.read_user_from_db()

    hp_up = randint(3, 10)
    attack_up = randint(1, 8)
    defense_up = randint(1, 10)
    crit_rate_up_100 = randint(1, 5)

    while 1:
        chose = input(
            f"""
    请问您想提升哪一项能力？

    1. 生命值 ({userobj.hp//5}金币)
    {userobj.hp} => {userobj.hp + hp_up}
            
    2. 攻击力 ({userobj.attack//2}金币)
    {userobj.attack} => {userobj.attack + attack_up}
            
    3. 防御力 ({userobj.defense//4}金币)
    {userobj.defense} => {userobj.defense + defense_up}

    4. 暴击率 ({round(userobj.crit_rate*250)}金币)

    {userobj.crit_rate*100}% => {userobj.crit_rate*100 + crit_rate_up_100}%

    
    5. 退出

>>>"""
        )
        match chose:
            case "1":
                if userobj.gold >= hp_up:
                    userobj.hp += hp_up
                    userobj.gold -= hp_up
                    input(f"恭喜！您成功提升生命值到{userobj.hp}！")

                else:
                    input("金币不足！")
            case "2":
                if userobj.gold >= attack_up:
                    userobj.attack += attack_up
                    userobj.gold -= attack_up
                    input(f"恭喜！您成功提升攻击力到{userobj.attack}！")

                else:
                    input("金币不足！")
            case "3":
                if userobj.gold >= defense_up:
                    userobj.defense += defense_up
                    userobj.gold -= defense_up
                    input(f"恭喜！您成功提升防御力到{userobj.defense}！")

                else:
                    input("金币不足！")
            case "4":
                升级暴击花费 = crit_rate_up_100 * 2.5
                if userobj.gold >= 升级暴击花费:
                    userobj.crit_rate += crit_rate_up_100 / 100
                    userobj.gold -= crit_rate_up_100 * 250
                    input(f"恭喜！您成功提升暴击率到{userobj.crit_rate*100}%！")
                else:
                    input("金币不足！" + str(升级暴击花费))

            case "5":
                break
            case _:
                input("输入错误！")

        os.system("cls" if os.name == "nt" else "clear")

    ucf.write_user_to_db(userobj)


if __name__ == "__main__":
    main()
