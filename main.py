"""
DATE: 2024-4-14
AUTHOR: fxbd5684
"""

import login
import game
import os


def main():
    login.main()
    os.system('cls' if os.name == 'nt' else 'clear')
    game.main()



if __name__ == '__main__':
    main()
