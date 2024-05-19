import sys
from tomlr import *

sys.path.append("..")


def main():
    print(
        r"""
  ______                    _____  _            
 |  ____|                  / ____|(_)           
 | |__   __  __ ___  _ __ | |      _  ___   ___ 
 |  __|  \ \/ // _ \| '__|| |     | |/ __| / _ \
 | |____  >  <|  __/| |   | |____ | |\__ \|  __/
 |______|/_/\_\\___||_|    \_____||_||___/ \___|
                                                                          
______________________________________________                                 
    """
    )

    choise = input(
        """
    +============================+
    |        1. 项目详情         |
    |        2. 项目配置         |
    +============================+
        """
    )
    match choise:
        case "1":
            show_project_info()


def show_project_info():
    print(f"项目名: {PROJECT_NAME} ")

    print(f"项目介绍: {PROJECT_DESCRIPTION} ")

    print(f"项目版本: {PROJECT_VERSION} ")

    print(f"项目作者: {PROJECT_AUTHOR} ")

    print(f"项目描述: {PROJECT_DESCRIPTION} ")

    print(f"更新的功能: {NEWS} ")

    input(f"项目源代码: {PROJECT_URL} ")


if __name__ == "__main__":
    main()
