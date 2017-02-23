#!/usr/bin/env python3.5
#_*_ coding:utf-8 _*_

import uuid
import hashlib
import time
import os
def create_uuid():
    return str(uuid.uuid1())

def create_md5():
    m=hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()


if __name__ == '__main__':
    print(create_md5(),create_uuid())
