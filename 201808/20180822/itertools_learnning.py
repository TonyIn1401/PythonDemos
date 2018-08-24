# _*_ coding: utf-8 _*_

import itertools
from functools import reduce

def pi_count(n):
    pi_arry = itertools.count(1, 2)
    pi_top_n = list(itertools.takewhile(lambda x: x <= 2 * n - 1, pi_arry))
    pi_result = reduce(lambda x, y: x + y, map(lambda x: 4 / x * pow(-1, x // 2), pi_top_n))
    return pi_result
