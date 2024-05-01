# 在这里，我要创建一个简易的数据库
# 用pickle模块来存储数据
# 数据库的结构是：
# {
#     主键:dataclass,
#     主键:dataclass,
#    ...
# }
import os
import pickle
from dataclasses import dataclass
from typing import Union


# 定义fexdb类
class Fexdb:
    def __init__(self, filename: str) -> None:
        """
        初始化数据库类

        :param filename: str, 数据库文件名
        """
        self.filename: str = filename
        self.db: dict[str:dataclass] = pickle.load(open(filename, "rb")) if os.path.exists(filename) else {}

    def save(self) -> None:
        """
        保存数据库到文件
        """
        pickle.dump(self.db, open(self.filename, "wb"))

    def add(self, key, value) -> None:
        """
        添加数据到数据库

        :param key: 主键
        :param value: 数据
        """
        self.db[key] = value
        self.save()

    def delete(self, key) -> None:
        """
        从数据库中删除数据

        :param key: 主键
        """
        if key in self.db:
            del self.db[key]
            self.save()

    def get(self, key) -> Union[None, dataclass]:
        """
        从数据库中获取数据

        :param key: 主键
        :return: 数据 | None
        """
        return self.db.get(key)

    def update(self, key, value) -> None:
        """
        更新数据库中的数据

        :param key: 主键
        :param value: 数据
        """
        if key in self.db:
            self.db[key] = value
            self.save()
    
    def reset(self) -> None:
        """
        清空数据库
        """
        self.db = {}
        self.save()

    @property
    def is_empty(self) -> bool:
        """
        判断数据库是否为空

        :return: bool
        """
        return len(self.db) == 0


# 定义一个测试模型
@dataclass
class TestModel:
    name: str
    passwd: str
    money: int = 10


if __name__ == '__main__':
    users = Fexdb("users.db")
    users.add('test', TestModel(name='test', passwd='<PASSWORD>', money=100))
    users.save()
    print(users.db)
