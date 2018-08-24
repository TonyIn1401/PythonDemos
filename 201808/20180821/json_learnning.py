# _*_ coding: utf-8 _*_
import json
import subprocess


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
c = json.loads(s)
print(c)

