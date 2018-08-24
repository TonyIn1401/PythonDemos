# _*_ coding: utf-8 _*_

import logging
import os

def log_demo():
    logging.basicConfig(level=logging.INFO)
    try:
        s = '0'
        n = int(s)
        logging.info('n = %d' % n)
        print(10 / n)
    except ZeroDivisionError as e:
        logging.error(e)

def dir_l(path):
    return os.listdir(path)

def find_by_name(path, name):
    """
    递归调用查找文件
    """
    for item in os.listdir(path):
        opr_path = os.path.join(path, item)
        if os.path.isdir(item):
            find_by_name(opr_path, name)
        else:
            file_name = os.path.split(item)[1]
            if name.lower() in file_name.lower():
                yield opr_path

    return "done"




if __name__ == "__main__":
    find_by_name('.', 'Leave')
