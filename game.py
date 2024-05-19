import ucf
import os
from games import (
    userinfo,
    contest,
    exercise,
    dungeon,
    progress,
    shop,
    developer,
    settings,
)
from tools import return_menu


def main():
    while 1:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            r"""
  ______            _____                         
 |  ____|          / ____|                        
 | |__  ___ __  __| |  __   __ _  _ __ ___    ___ 
 |  __|/ _ \\ \/ /| | |_ | / _` || '_ ` _ \  / _ \
 | |  |  __/ >  < | |__| || (_| || | | | | ||  __/
 |_|   \___|/_/\_\ \_____| \__,_||_| |_| |_| \___|
 
"""
        )
        menu = [
            "1. 信息",
            "2. 战斗",
            "3. 锻炼",
            "4. 副本",
            "5. 提升",
            "6. 商店",
            "7. 设置",
            "8. 退出",
        ]
        print(return_menu(menu,wight=20))
        choice = input('>>> ')
        match choice:
            case "1":
                os.system("cls" if os.name == "nt" else "clear")
                userinfo.main()
            case "2":
                os.system("cls" if os.name == "nt" else "clear")
                contest.main()
            case "3":
                os.system("cls" if os.name == "nt" else "clear")
                exercise.main()
            case "4":
                os.system("cls" if os.name == "nt" else "clear")
                dungeon.main()
            case "5":
                os.system("cls" if os.name == "nt" else "clear")
                progress.main()
            case "6":
                os.system("cls" if os.name == "nt" else "clear")
                shop.main()
            case "8":
                exit()
            case "7":
                os.system("cls" if os.name == "nt" else "clear")
                settings.main()
            case "developer":
                developer.main()
            case _:
                input("没有这个选项~  (╥﹏╥)")


if __name__ == "__main__":
    main()
