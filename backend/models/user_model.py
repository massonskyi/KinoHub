from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean

from models.base import Base


class Role(Base):
    __tablename__: str = 'role'
    id: Column = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Column = Column(String, nullable=False)


class User(Base):
    __tablename__: str = "user"
    id: Column = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Column = Column(String, nullable=False)
    email: Column = Column(String, nullable=False)
    username: Column = Column(String, nullable=False)
    hashed_password: Column = Column(String, nullable=False)
    registered_at: Column = Column(TIMESTAMP, default=datetime.utcnow)
    phone: Column = Column(String, nullable=False)
    search_movies: Column = Column(String, nullable=False)
    role_id: Column = Column(Integer, ForeignKey(Role.id))
    is_active: Column = Column(Boolean, default=True, nullable=False)
    is_superuser: Column = Column(
        Boolean, default=False, nullable=False
    )
    is_verified: Column = Column(
        Boolean, default=False, nullable=False
    )
