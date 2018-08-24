# _*_ coding: utf-8_*_
import hashlib, random
from hashlib import md5

DB = {}
SALT = ''.join([chr(random.randint(48, 122)) for i in range(20)])  

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
     
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = get_md5(password + SALT)

    def regist(self):
        if self.user_name in DB.keys():
            return False
        else:
            DB[self.user_name]= get_md5(self.password + SALT)
            return True

    def login(self):
        if DB[self.user_name] == get_md5(self.password + SALT):
            return True
        return False

def exer_1():
    """
    练习MD5加密
    """
    # 测试:
    user1 = User('michael', '123456')
    assert user1.regist()
    assert user1.login()

    user2 = User('michael', '123')
    assert not user2.regist()
    assert not user2.login()

    print('ok')


if __name__ == "__main__":
    exer_1()