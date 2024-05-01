# -*- coding: utf-8 -*-
import ucf
import os
from hashlib import sha1


def encrypt_password(password):
    # 返回加密后的密码
    return sha1(password.encode('utf-8')).hexdigest()


def clear_terminal():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    if ucf.is_new_user():
        register()
    else:
        login()


def register():
    # code for registration
    while 1:
        print(r"""
   _____  _                _    _        
  / ____|(_)              | |  | |       
 | (___   _   __ _  _ __  | |  | | _ __  
  \___ \ | | / _` || '_ \ | |  | || '_ \ 
  ____) || || (_| || | | || |__| || |_) |
 |_____/ |_| \__, ||_| |_| \____/ | .__/ 
              __/ |               | |    
             |___/                |_|  
             
_________________________________________________
        """)

        name = input('欢迎来到 FexGame ! \n请告诉我你的名字:  ')
        password = input('设置密码:  ')
        retype_password = input('再次输入密码:  ')

        password_is_true = encrypt_password(password) == encrypt_password(retype_password)

        if password_is_true:
            ucf.create_user(name, encrypt_password(password))
            print('注册成功！')
            break
        else:
            print('两次输入的密码不一致，请重新输入！')


pass


def login():
    print('loading...')
    clear_terminal()
    print(r"""
  _                    _____        
 | |                  |_   _|       
 | |      ___    __ _   | |   _ __  
 | |     / _ \  / _` |  | |  | '_ \ 
 | |____| (_) || (_| | _| |_ | | | |
 |______|\___/  \__, ||_____||_| |_|
                 __/ |              
                |___/      
__________________________________________
                    """)

    user_obj = ucf.read_user_from_db()
    print("你好", user_obj.name)

    while 1:
        password = input('请输入密码:  ')
        if user_obj.password == encrypt_password(password):
            input("登录成功")
            break
        else:
            print("密码错误，请重新输入")
            continue
    pass


if __name__ == '__main__':
    main()
