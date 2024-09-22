# %%
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@localhost/car_rental")

Base = declarative_base()


class Photo(Base):
    __tablename__ = "Photo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(120))
    description = Column(String(250))
    privacy = Column(String(20))
    Upload_data = Column(Date)
    view = Column(Integer)


class Location(Base):
    __tablename__ = "Location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    shortname = Column(String(50))


class Member(Base):
    __tablename__ = "Member"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250))
    poto_num = Column(String(20))
    email = Column(String(200))
    address = Column(String(250))


class Album(Base):
    __tablename__ = "Album"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(120))
    description = Column(Integer)
    view = Column(Integer)


class Tag(Base):
    __tablename__ = "Tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Integer)


Base.metadata.create_all(engine)

# %%



