# !*/user/bin/python3
# -*- coding: utf-8 -*-
"""create module"""
from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from connect import Base

"""再次强调，我们用类来表示数据库里面的表！！！
这些表的类都继承于我们的Base基类。
在类里面我们定义一些属性，这个属性通过映射，就对应表里面的字段"""

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True,autoincrement = True)
    username = Column(String(20),nullable = False)
    password = Column(String(50))
    creatime = Column(DateTime,default = datetime.now())
    _locked = Column(Boolean,default = False,nullable = False)


if __name__ == "__main":
    Base.metadata.create_all()   #创建表，如果表存在，则不会更改