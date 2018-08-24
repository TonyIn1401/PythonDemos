# _*_ coding: utf-8 _*_

from datetime import datetime as dt

def datetime_demo():
    """
    datetime类试玩
    """
    #获取当前时间
    now = dt.now()
    print(now)

    #手动设置指定时间
    set_time = dt(2018, 8, 21, 14, 0)
    print(set_time)

    #获取时间戳
    stamp_time = set_time.timestamp()
    print(stamp_time)

    #时间戳转换成当地时间
    get_local_time = dt.fromtimestamp(stamp_time)
    print(get_local_time)

    #时间戳转换成标准时间
    get_utc_time = dt.utcfromtimestamp(stamp_time)
    print(get_utc_time)

    #字符串转换成时间
    str_time = "2018-08-21 14:18:21"
    trans_time = dt.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    print(trans_time)


if __name__ == "__main__":
    datetime_demo()
