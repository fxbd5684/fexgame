import sys

sys.path.append("..")

import ucf


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
    while 1:
        chose = input(
            f"""
    请问您想提升哪一项能力？

    1. 生命值 ({userobj.hp//5}金币)
    {userobj.hp} => {userobj.hp+5}
            
    2. 攻击力 ({userobj.attack//2}金币)
    {userobj.attack} => {userobj.attack+2}
            
    3. 防御力 ({userobj.defense//3}金币)
    {userobj.defense} => {userobj.defense+3}

    
    4. 退出

>>>"""
        )
        match chose:
            case "1":
                if userobj.gold >= 5:
                    userobj.hp += 5
                    userobj.gold -= 5
                    input(f"恭喜！您成功提升生命值到{userobj.hp}！")
                    break
                else:
                    input("金币不足！")
            case "2":
                if userobj.gold >= 2:
                    userobj.attack += 2
                    userobj.gold -= 2
                    input(f"恭喜！您成功提升攻击力到{userobj.attack}！")
                    break
                else:
                    input("金币不足！")
            case "3":
                if userobj.gold >= 3:
                    userobj.defense += 3
                    userobj.gold -= 3
                    input(f"恭喜！您成功提升防御力到{userobj.defense}！")
                    break
                else:
                    input("金币不足！")
            case "4":
                break
            case _:
                input("输入错误！")

    ucf.write_user_to_db(userobj)


if __name__ == "__main__":
    main()
