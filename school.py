#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
    选课系统
    角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校，
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里

'''
import uuid
import logging
import pickle
import os
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')


def create_uid():
    return str(uuid.uuid1())

class BaseModel(object):

    def save(self):
        file_path = os.path.join(self.db_path,str(self.uid))
        print(os.getcwd())
        if  not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
        with open(file_path ,'wb') as fp:
            pickle.dump(self,fp)

    @classmethod
    def read_obj(cls):
        ret=[]
        for pk in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path,pk)
            with open(file_path,'rb') as fb:
              ret.append(pickle.load(fb))
        return ret
    pass

class School(BaseModel):
    def __init__(self,city,school_name):
        self.city = city
        self.school_name = school_name
        self.uid = create_uid()
        self.db_path = 'db/school'
        logging.info('create a School : %s %s' % (self.city,self.school_name))
    pass

class Course(object):
    def __init__(self,course_name,period,cost):
        self.course_name = course_name
        self.period = period
        self.cost = cost
    pass

class Class(object):
    def __init__(self,class_name,class_id,course,teacher_name,teacher_id):
        self.class_name = class_name
        self.class_id = class_id
        self.course = course
        self.teacher.name = teacher_name
        self.teacher.id =teacher_id
    pass


class Teacher(object):
    def __init__(self,teacher_name,teacher_id):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id
    pass

class Student(BaseModel):
    pass



def main():
    bj=School('beijing','qinhua')
    sh=School('shanghai','beida')
    bj.save()


    pass



if __name__ == '__main__':
    main()
    pass
