import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    favorite = relationship('Favorite')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    gender = Column(String(15), nullable=True)
    eye_color = Column(String(100))
    description = Column(String(500), nullable=False)
    favorite = relationship('Favorite')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(500), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(50))
    favorite = relationship('Favorite')
    

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    model = Column(String(100))
    description = Column(String(500), nullable=False)
    capacity = Column(Integer, nullable=False)
    favorite = relationship('Favorites')        

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet = relationship(Planet)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle = relationship(Vehicle)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
