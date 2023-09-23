from sqlalchemy import Column, Integer, String, DateTime, Time, Float, JSON

from models.base import Base


class Movie(Base):
    __tablename__: str = "movie"
    id: Column = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Column = Column(String, nullable=False)
    genre: Column = Column(String, nullable=False)
    year: Column = Column(DateTime, nullable=False)
    duration: Column = Column(Time, nullable=False)
    rating: Column = Column(Float, nullable=False)
    budget: Column = Column(Float, nullable=False)
    fees: Column = Column(Float, nullable=False)

    # TODO: create tables add relationship
    director: Column = Column(String, nullable=False)
    screenwriter: Column = Column(String, nullable=False)
    actors: Column = Column(String, nullable=False)
