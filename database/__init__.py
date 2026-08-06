import builtins

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

builtins.Base = Base