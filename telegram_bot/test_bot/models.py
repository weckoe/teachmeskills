from db import engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey, )

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(15), nullable=True)
    user_surname = Column(String(15), nullable=True)
    age = Column(Integer, nullable=False)
    todo_users = relationship("Users_todo", backref="user")

    def __str__(self):
        return f"Пользователь: {self.user_name} {self.user_surname} {self.age}"


class Users_todo(Base):
    __tablename__ = "users_todo"
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    user_todo = Column(String(length=None), nullable=True)
    todo_date = Column(String)

    def __str__(self):
        return f"Todo: {self.todo_date} {self.user_todo}"


Base.metadata.create_all(engine)
