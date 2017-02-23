#!/usr/bin/env python3.5
#_*_ coding:utf-8 _*_

import os
import pickle
import uuid
import logging
from settings import *

logging.basicConfig(level=logging.INFO)


def load_date(db_path):
    rst = []
    for pk in os.listdir(db_path):
        file = os.path.join(db_path,pk)
        with open(file, 'rb') as fb:
            date = pickle.load(fb)
            rst.append(date)
    print(rst[0].name)



pass

class BaseModel(object):
    def __init__(self):
        self.uuid = str(uuid.uuid1())

    def save(self):
        self.db_path
        if  not os.path.exists(self.db_path):
            os.mkdir(self.db_path)
        file_path = os.path.join(self.db_path,self.uuid)
        with open(file_path,'wb') as fb:
            pickle.dump(self,fb)
            logging.info('%s  %s saved success!' % (self.__class__.__name__,self.name))



class School(BaseModel):
    def __init__(self,name,addr):
        super(School,self).__init__()
        self.db_path=school_path
        self.name = name
        self.addr = addr
    pass

class Classes(BaseModel):
    pass

class Course(BaseModel):
    pass

class Teacher(BaseModel):
    pass

class Student(BaseModel):
    pass


if __name__ ==  '__main__':
    # s1=School('qinghua','beijing')
    # s1.save()
    # s2=School('shifan','chongqing')
    # s2.save()
    load_date(school_path)