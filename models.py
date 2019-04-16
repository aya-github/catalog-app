from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), index=True, unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password_hash = Column(String(64))
    picture = Column(String(250))

    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'id': self.id,
        'name': self.name,
        'email': self.email,
        'password_hash': self.password_hash,
        }


class Category(Base):
    __tablename__ = 'category'

    #id = Column(Integer, primary_key=True)
    name = Column(String(80), primary_key=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        #'id': self.id,
        'name': self.name,
        }


class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    category_name = Column(String, ForeignKey('category.name'))
    category = relationship(Category, cascade="all, delete-orphan", single_parent=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'created': self.created,
        }


engine = create_engine('sqlite:///catalog.db')


Base.metadata.create_all(engine)
