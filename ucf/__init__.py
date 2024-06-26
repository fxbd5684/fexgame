import sys
from typing import NoReturn

sys.path.append("..")

from fexdb import Fexdb
from ucf.models import User, default_user

database = Fexdb("ucf.fexdb")


def write_user_to_db(user: User, db: Fexdb = database) -> None:
    """
    Write the user to the db.
    :param db:
    :param user:
    :return:
    """
    db.update(user.name, user)


def create_user(name: str, password: str, db: Fexdb = database) -> None:
    """
    Create a new user in the db.
    注意，这个函数只允许数据库里面有一个用户存在
    :param db:
    :param name:
    :param password:
    :return:
    """
    user = default_user
    user.name = name
    user.password = password
    if db.is_empty:
        db.add(user.name, user)
    else:
        raise ValueError("这个数据库里面已经有用户了，不能再创建新用户了。")


def read_user_from_db(db: Fexdb = database) -> User | NoReturn:
    """
    Read the user from the db.

    注意： 如果没有用户，会抛出异常。
    :param db:
    :return: User
    :raises: StopIteration
    """
    return next(iter(db.db.values()))  # 获取字典中的第一个value


def change_user_attr(attr_name, new_value, db: Fexdb = database):
    """
    修改用户属性
    :param attr_name:
    :param new_value:
    :param db:
    :return:
    """
    user = read_user_from_db(db)
    setattr(user, attr_name, new_value)
    write_user_to_db(user)


def sub_user_attr(attr_name, sub_value: float, db: Fexdb = database):
    """
    减少用户属性
    :param attr_name:
    :param sub_value:
    :param db:
    :return:
    """
    user = read_user_from_db(db)
    setattr(user, attr_name, getattr(user, attr_name) - sub_value)
    write_user_to_db(user)


def add_user_attr(attr_name, add_value: float, db: Fexdb = database):
    """
    增加用户属性
    :param attr_name:
    :param add_value:
    :param db:
    :return:
    """
    user = read_user_from_db(db)
    setattr(user, attr_name, getattr(user, attr_name) + add_value)
    write_user_to_db(user)


# noinspection PyShadowingNames
def is_new_user(db: Fexdb = database) -> bool:
    """

    :type db: Fexdb
    :return: bool
    """
    try:
        read_user_from_db(db)
        return False
    except StopIteration:
        return True


def reset_user(db: Fexdb = database) -> None:
    """
    Reset the user in the db.
    :param db:
    :return:
    """
    db.reset()


if __name__ == "__main__":
    change_user_attr("gold", 10)
