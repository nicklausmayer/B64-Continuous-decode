#!/bin/env python
import base64

flag = open("theflag", 'r').read()
flag = base64.b64decode(flag).decode('utf-8')

while r'flag{' not in flag:
    flag = base64.b64decode(flag).decode('utf-8')

print(flag)
