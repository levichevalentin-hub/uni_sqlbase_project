from sqlalchemy import Column, Integer, String, Enum, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
import enum

from database.tables.base import Base

class EntityType(enum.Enum):
    student = "student"
    teacher = "teacher"

class Role(enum.Enum):
    user = "user"
    admin = "admin"

class Auth(Base):
    __tablename__ = 'auth'

    external_id = Column(Integer, nullable=False)
    entity_type = Column(Enum(EntityType), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(Role), default=Role.user)

    __table_args__ = (
        PrimaryKeyConstraint('external_id', 'entity_type'),
    )