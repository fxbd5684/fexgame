import sys
import cmd
import os
from hashlib import sha1


sys.path.append("..")

import ucf


def encrypt_password(password):
    # 返回加密后的密码
    return sha1(password.encode("utf-8")).hexdigest()


def match_err(fun):
    def wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)  # 返回包装函数的结果
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"{fun.__name__} 执行失败:{e}")

    return wrapper  # 返回包装函数


#################################################################


class AddSomeThingToolBox:
    @match_err
    def add_exp(self, how_many: int):
        userobj = ucf.read_user_from_db()
        userobj.exp += how_many
        ucf.write_user_to_db(userobj)
        return userobj  # 返回操作结果


class Developer(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "developer> "
        self.intro = (
            "请注意,这是开发者模式!\n你的每一次操作都可能会影响游戏体验\n请谨慎使用"
        )
        self.password_is_true = False

    def do_password(self, password):
        """
        输入密码
        """
        if encrypt_password(password) == "a9cdf1f4031f63077c1ee90c79376abed7af4e20":
            os.system("cls")
            print("密码正确,进入开发者模式")
            self.password_is_true = True
        else:
            print("密码错误")

    def do_add(self, arg):
        """
        添加属性

        示例: add exp 10

        注意,有更好的方法
        """
        if not self.password_is_true:
            print("请先输入正确的密码")
            return

        args = arg.split()  # 将参数分隔成列表
        if len(args) != 2:
            print("参数错误")
            return

        what, how_many = args
        try:
            how_many = int(how_many)  # 尝试将 how_many 转换为整数
            if how_many < 0:
                print("how_many 参数不能为负数")
                return
        except ValueError:
            print("how_many 参数必须为整数")
            return

        if what == "exp":
            toolbox = AddSomeThingToolBox()
            result = toolbox.add_exp(how_many)  # 调用方法并获取结果
            if result:
                print("添加成功")
            else:
                print("添加失败")
        else:
            print("不支持的属性")

    def do_resetinfo(self, arg):
        """
        重置用户

        示例: resetinfo
        """
        if not self.password_is_true:
            print("请先输入正确的密码")
            return

        if input("确认重置?(y/n)") == "y":
            ucf.reset_user()
            print("删除成功")
            print("请退出游戏并重新登录,谢谢")
        else:
            print("取消删除")

    def do_set(self, arg):
        """
        设置属性值

        示例: set exp 10
        """
        if not self.password_is_true:
            print("请先输入正确的密码")
            return

        args = arg.split()  # 将参数分隔成列表
        if len(args) != 2:
            print("参数错误")
            return

        what, value = args

        try:
            value = float(value)  # 尝试将 value 转换为浮点数
            userobj = ucf.read_user_from_db()
            userobj.__setattr__(what, value)
            ucf.write_user_to_db(userobj)
            print("设置成功")

        except ValueError:
            print("value 参数必须为浮点数")
            return
        except AttributeError:
            print("不支持的属性")
            return

    def do_exit(self, arg):
        """
        退出
        """
        input("[按回车键退出]")
        return True


def main() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print(
        r"""
      _                    _                           
     | |                  | |                          
   __| |  ___ __   __ ___ | |  ___   _ __    ___  _ __ 
  / _` | / _ \\ \ / // _ \| | / _ \ | '_ \  / _ \| '__|
 | (_| ||  __/ \ V /|  __/| || (_) || |_) ||  __/| |   
  \__,_| \___|  \_/  \___||_| \___/ | .__/  \___||_|   
                                    | |                
                                    |_|    
____________________________________________________________                            
    """
    )
    Developer().cmdloop()


if __name__ == "__main__":
    main()
